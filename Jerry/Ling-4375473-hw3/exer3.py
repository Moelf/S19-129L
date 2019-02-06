import math
import numpy as np
import matplotlib.pyplot as plt
import csv
with open('./CensusTownAndCityPopulation.csv', newline='', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    digits = [x[2][0] for x in reader[1::]] # skip header, collect all first digits
digits = np.array(digits).astype(int)
plt.xlabel("First digit")
plt.ylabel("Occurance")
plt.title("US Census Population first digit")
plt.hist(digits, bins=np.arange(1,11,1), align='left', label="First digit occurance")
plt.xticks(np.arange(1,11,1))
plt.legend()
plt.show()
