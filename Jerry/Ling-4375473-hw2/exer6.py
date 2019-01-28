try:
    largeNum = abs(int(input("Please just give me a normal >1 number to do prime factoriztaion: ")))
except:
    print("Sorry that's not an integer")
if largeNum <= 1: print("Sorry 0 or 1 won't work.")

i=2
countDict = dict()
while largeNum > 1:
    while largeNum%i == 0:
        largeNum/=i
        if i in countDict.keys():
            countDict[ i ] += 1
        else:
            countDict[ i ] = 1
    i+=1

for key in countDict.keys():
    print(key, "to the power of", countDict[key])
