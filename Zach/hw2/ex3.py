#!/usr/bin/env python3

sent=input("Please input a sentence: ")
list=sent.split()
print (' '.join(sorted(set(list), key=list.index)))


