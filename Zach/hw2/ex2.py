#!/usr/bin/env python3

sent=input("Please input a sentence: ")

list1=[len(x) for x in sent.split()]

sent=sent.replace(',',' ') #separates words by commas
sent=sent.replace(';',' ')
sent=sent.replace(':',' ')
sent=sent.replace('.',' ')
sent=sent.replace('/',' ')
sent=sent.replace('\\',' ')
sent=sent.replace('-',' ')
sent=sent.replace('(',' ')
sent=sent.replace(')',' ')
sent=sent.replace('&',' ')



list2=[len(x) for x in sent.split()]

print("The number of words is ", len(list2))

print("The number of characters is ", sum(list1))


print(list2)

