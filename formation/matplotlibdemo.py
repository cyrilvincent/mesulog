import matplotlib.pyplot as plt
import numpy as np
import csv

with open("mesures.csv") as f:
    reader = csv.DictReader(f)
    vt = []
    for row in reader:
        vt.append(float(row["VT"]))

plt.plot(vt)
plt.show()