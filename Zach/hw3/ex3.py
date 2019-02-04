#!/usr/bin/env python3

import numpy as np
import csv
import matplotlib.pyplot as plt

with open('CensusTownAndCityPopulation.csv', newline='', encoding='utf-8') as census:
	reader=list(csv.reader(census))


num=np.array(list(i[2].replace(',' , '') for i in reader[1::])) #All numbers
first_digit=[int(str(num[i])[:1]) for i in range(len(num))] #First digits

plt.hist(first_digit,bins=[1,2,3,4,5,6,7,8,9,10],edgecolor='black')
plt.xlabel('First Digit in Population Count')
plt.ylabel('Number of Ocurrences')
plt.show()
