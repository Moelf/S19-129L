import time
try:
    largeNum = abs(int(input("Please just give me a normal >1 number to do prime factoriztaion: ")))
except:
    print("Sorry that's not an integer")
if largeNum <= 1: print("Sorry 0 or 1 won't work.")

start = time.time()
i=2
# countDict = dict()
res = []
while largeNum > 1:
    while largeNum%i == 0:
        largeNum/=i
        res.append(i)
    i+=1
timeer = time.time() - start
print("%s seconds" %(timeer))
# for key in countDict.keys():
#     print(key, "to the power of", countDict[key])
print(res)
