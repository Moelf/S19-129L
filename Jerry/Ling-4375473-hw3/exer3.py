import math
import numpy as np
import matplotlib.pyplot as plt
import csv
with open('/home/akako/Document/github/S19-129L/Jerry/CensusTownAndCityPopulation.csv', newline='', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    digits = ''.join([x[2].replace(',','') for x in reader[1::]]) # skip header, remove comma and connect all digits
digits = np.array(list(digits)).astype(int)
plt.hist(digits, bins=np.arange(0,10,1),align='left')
plt.xticks(np.arange(0,10,1))

plt.show()
