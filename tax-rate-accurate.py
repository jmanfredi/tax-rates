import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

listOfYears = []

d1950 = {5: 16, 15: 17, 25: 18, 35: 19, 45: 19, 55: 20, 65: 20, 75: 20, 85: 22, 
  92.5: 23, 97.5: 28, 99.45: 40, 99.945: 51, 99.999: 68, 99.9999: 70}
d1960 = {5: 18, 15: 20, 25: 22, 35: 23, 45: 23, 55: 24, 65: 25, 75: 25, 85: 26, 
  92.5: 26, 97.5: 29, 99.45: 39, 99.945: 51, 99.999: 55, 99.9999: 56}
d1972 = {5: 19, 15: 22, 25: 25, 35: 27, 45: 27, 55: 27, 65: 28, 75: 28, 85: 28, 
  92.5: 28, 97.5: 31, 99.45: 38, 99.945: 48, 99.999: 53, 99.9999: 52}
d1980 = {5: 20, 15: 22, 25: 25, 35: 27, 45: 29, 55: 30, 65: 30, 75: 31, 85: 31, 
  92.5: 30, 97.5: 31, 99.45: 36, 99.945: 42, 99.999: 46, 99.9999: 47}
d2000 = {5: 25, 15: 27, 25: 28, 35: 27, 45: 28, 55: 29, 65: 30, 75: 31, 85: 32, 
  92.5: 31, 97.5: 31, 99.45: 33, 99.945: 38, 99.999: 38, 99.9999: 33}
d2018 = {5: 25, 15: 24, 25: 24, 35: 23, 45: 24, 55: 25, 65: 26, 75: 27, 85: 28, 
  92.5: 27, 97.5: 26, 99.45: 27, 99.945: 30, 99.999: 28, 99.9999: 23}

listOfYears.append(d1950)
listOfYears.append(d1960)
listOfYears.append(d1972)
listOfYears.append(d1980)
listOfYears.append(d2000)
listOfYears.append(d2018)

# df = pd.DataFrame(listOfYears)
# df = df.set_index("YEAR")
# print(df.head())
# print(type(list(df.columns)[0] ) ) 

fig, ax = plt.subplots()
increment = 1 / len(listOfYears)
print(increment)
index = 0
cSet = ['b','g','r','c','m','k']
for item in listOfYears:
  index = index + 1
  x = []
  y = []
  for key, value in item.items():
    x.append(float(key))
    y.append(value)
  xArr = np.array( x )
  yArr = np.array( y )
  color = (1.0, 0.0, 1.0, index*increment)
  ax.scatter(xArr, yArr, c = cSet[index-1])

#ax.legend()
ax.grid(True)

plt.show()

#myplot = df.plot(x=[int(x) for x in list(df.columns)], y=)
