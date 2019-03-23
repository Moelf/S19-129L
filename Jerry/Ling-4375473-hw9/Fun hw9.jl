
import StatsBase
using DataFrames, Gadfly, CSV, Flux, Cairo

function reysum(xs, ys)
    local area = 0
    for i=2:length(xs)
        dx = abs(xs[i] - xs[i-1])
        y = (ys[i] + ys[i-1])/2
        area += dx*y
    end
    return round(area, digits=2)
end

df = CSV.File("./data_fourtop.csv") |> DataFrame
# shuffle
df = df[StatsBase.shuffle(1:size(df, 1)),:]
first(df,3)

histnb = plot(df, x=:nbtags, color=:signal, Geom.histogram, style(bar_spacing=1mm),Coord.cartesian(xmin=0.5, xmax=5.5),Scale.color_discrete_hue)
histnjets = plot(df, x=:njets, color=:signal, Geom.histogram, style(bar_spacing=1mm), Coord.cartesian(xmin=1.5, xmax=7),Scale.color_discrete_hue)
histnb_density = plot(df, x=:nbtags, color=:signal, Geom.histogram, Coord.cartesian(xmin=1, xmax=5),Scale.color_discrete_hue)
histnweights = plot(df, x=:weight, color=:signal,Geom.density(), Coord.cartesian(xmin=0, xmax=0.016),Scale.color_discrete_hue)

set_default_plot_size(10inch, 6inch)
gridstack([histnb histnjets; histnb_density histnweights])

# 80% train
# 20% test
df_train = df[1:round(Int, size(df,1)*0.8),:]
df_test = df[round(Int,size(df,1)*0.8+1):end,:]

# re-balance train set, match length of signals
df_balanced = df_train[df_train.signal .== 1.0,:]
bkg_rows = df_train[df_train.signal .== 0.0,:]
bkg_rows = bkg_rows[1:size(df_balanced,1),:]
append!(df_balanced, bkg_rows);

# shuffle
df_balanced = df_balanced[StatsBase.shuffle(1:size(df_balanced, 1)),:]

xs_train = convert(Matrix, df_balanced[1:end,4:13])
ys_train = df_balanced.signal
xs_test = convert(Matrix, df_balanced[1:end,4:13])
ys_test = df_balanced.signal

# make the tag one-hot
ys_train = [Flux.onehot(i, [1,0]) for i in ys_train]
# zip xs_train and ys_train together
data = collect(zip(eachrow(xs_train), ys_train));

# Dense layer is linear, sigma is identity
# softmax gives you normalized vector (sort of)
m = Chain(Dense(10,2), softmax)

# cross entropy is natual choice for onehot data, since we only have 1 or 0, this is basically -p*log(q)
loss(x, y) = Flux.crossentropy(m(x), y)

# ADAM optimizer https://arxiv.org/abs/1412.6980v8
opt = ADAM(0.001, (0.9, 0.999))

# make two sets for visualization the train model compare before & after
xs_test = convert(Matrix, df_test[1:end,4:13])
df_balanced[:model_predict] = [m(xs_train[i,:]).data[1] for i=1:length(xs_train[:,1])]
df_test[:model_predict] = [m(xs_test[i,:]).data[1] for i=1:length(xs_test[:,1])]
fake_before = plot(df_balanced, x=:model_predict, color=:signal, Guide.Title("Train set, untrain"), Geom.density(bandwidth=0.05))
real_before = plot(df_test, x=:model_predict, Guide.Title("Test set, untrain"), color=:signal, Geom.density(bandwidth=0.05));
set_default_plot_size(8inch, 3inch);
gridstack([fake_before real_before])

# train 4 times over our data
Flux.@epochs 8 Flux.train!(loss, params(m), data, opt)

df_balanced[:model_predict] = [m(xs_train[i,:]).data[1] for i=1:length(xs_train[:,1])]
df_test[:model_predict] = [m(xs_test[i,:]).data[1] for i=1:length(xs_test[:,1])]

fake_after = plot(df_balanced, x=:model_predict, color=:signal, Guide.Title("Train set, trained"), Geom.density(bandwidth=0.05))
real_after = plot(df_test, x=:model_predict, color=:signal, Guide.Title("Test set, trained"), Geom.density(bandwidth=0.05))
set_default_plot_size(8inch, 3inch);
gridstack([fake_after real_after])

df_AUC = DataFrame()
# https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc
TPR, FPR = [], []
TPR2, FPR2 = [], []
for i=0:0.001:1
    TP  = sum((df_test.signal .== 1.0) .& (df_test.model_predict .> i))
    FP = sum((df_test.signal .== 0.0) .& (df_test.model_predict .> i))
    TN = sum((df_test.signal .== 0.0) .& (df_test.model_predict .< i))
    FN = sum((df_test.signal .== 1.0) .& (df_test.model_predict .< i))
    push!(TPR, TP/(TP+FN))
    push!(FPR, FP/(FP+TN))
    TP2 = sum((df_balanced.signal .== 1.0) .& (df_balanced.model_predict .> i))
    FP2 = sum((df_balanced.signal .== 0.0) .& (df_balanced.model_predict .> i))
    TN2 = sum((df_balanced.signal .== 0.0) .& (df_balanced.model_predict .< i))
    FN2 = sum((df_balanced.signal .== 1.0) .& (df_balanced.model_predict .< i))
    push!(TPR2, TP2/(TP2+FN2))
    push!(FPR2, FP2/(FP2+TN2))
end
df_AUC[:FPR] = FPR
df_AUC[:TPR] = TPR
df_AUC[:FPR2] = FPR2
df_AUC[:TPR2] = TPR2
test_area = reysum(FPR, TPR)
train_area = reysum(FPR2, TPR2)


test_ROC = layer(df_AUC, x=:FPR, y=:TPR, Geom.line)
train_ROC = layer(df_AUC, x=:FPR2, y=:TPR2, Geom.line, Theme(default_color="orange"))
set_default_plot_size(8inch, 5inch)
plot(test_ROC, train_ROC, Guide.Title("ROC Curve"), Guide.manual_color_key("Type", ["Test area: $(test_area)", " Train area: $(train_area)"], ["deepskyblue", "orange"]))
