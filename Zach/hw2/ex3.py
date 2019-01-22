#!/usr/bin/env python3

sent=input("Please input a sentence: ")
sent=sent.replace(',',' ') #separates words by commas, etc
sent=sent.replace(';',' ')
sent=sent.replace(':',' ')
sent=sent.replace('.',' ')
sent=sent.replace('/',' ')
sent=sent.replace('\\',' ')
sent=sent.replace('-',' ')
sent=sent.replace('(',' ')
sent=sent.replace(')',' ')
sent=sent.replace('&',' ')

list=sent.split()
print (' '.join(sorted(set(list), key=list.index)))


