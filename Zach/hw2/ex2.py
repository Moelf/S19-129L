#!/usr/bin/env python3

sent=input("Please input a sentence: ")

list1=[len(x) for x in sent.split()] #Count all characters excluding only spaces; includes punctuation in 'characters'

sent=sent.replace(',',' ') #separates words by commas, etc
sent=sent.replace(';',' ') #Francesco said this was the punctuation that mattered; don't need to account for every possible one
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

