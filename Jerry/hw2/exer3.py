rawIn = input("Please just enter a sentence:")
import re
wordList= re.findall(r'\w+', rawIn)
#because we want ordered words so we can't use list(dict.fromkeys(wordList))
res = []
for each in wordList:
    if each not in res:
        res.append(each)

print(" ".join(res))
