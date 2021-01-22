import sys
import csv
import matplotlib.pyplot as plt

with open(sys.argv[1]) as f:
  reader = csv.reader(f)
  l1 = [row for row in reader]

for row in l1:
  plt.plot(float(row[0]), float(row[1]), marker='.', c='blue')

plt.show()

with open(sys.argv[2]) as f:
  reader = csv.reader(f)
  l2 = [row for row in reader]

for row in l2:
  if float(row[2]) == 1: plt.plot(float(row[0]), float(row[1]), marker='.', c='blue')
  else:                  plt.plot(float(row[0]), float(row[1]), marker='.', c='red')

plt.show()