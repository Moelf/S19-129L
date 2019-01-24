import math

#this helper function returns primitivity
def isPrime(num):
    flag = True
    for k in range(2,int(math.sqrt(num)+1)):
        if num%k == 0:
            flag = False
            break
    return flag

#this helper function will list primes in range 2 to upper
def findPrimes(upper):
    rel = []
    for i in range(2,upper+1):
        if isPrime(i): rel.append(i)
    return rel

try:
    largeNum = int(input("Please just give me a normal >1 number to do prime factoriztaion: "))
except:
    print("Sorry that's not an integer")

largeNum = abs(largeNum)
if largeNum == 1: print("Sorry 1 won't work")
primeList = findPrimes(largeNum)
countDict = dict()


power = 0
for i in primeList:
    if largeNum % i != 0: continue
    while largeNum % i == 0:
        power+=1
        largeNum /= i
    if power > 0:
        countDict[i] = power
        power = 0

for key in countDict.keys():
    print(key, "to the power of", countDict[key])
