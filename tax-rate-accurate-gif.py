#With help from https://eli.thegreenplace.net/2016/drawing-animated-gifs-with-matplotlib/

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

yearLabels = [1950,1960,1972,1980,2000,2018]

# df = pd.DataFrame(listOfYears)
# df = df.set_index("YEAR")
# print(df.head())
# print(type(list(df.columns)[0] ) ) 

fig, ax = plt.subplots()
fig.set_tight_layout(True)

# Query the figure's on-screen size and DPI. Note that when saving the figure to
# a file, we need to provide a DPI for that separately.
print('fig size: {0} DPI, size in inches {1}'.format(
    fig.get_dpi(), fig.get_size_inches()))

increment = 1 / len(listOfYears)
print(increment)
cSet = ['b','g','r','c','m','k']

ax.grid(True)

def update(i):
  if i == 0:
    ax.clear()
    ax.grid(True)
    ax.set_ylim(0,100)
    ax.set_xlim(0,105)
    ax.set_xlabel("Income percentile (%)")
    ax.set_ylabel("Total tax rate (%)")
  label = 'Year: {0}'.format(yearLabels[i])
  print(label)
  #Update the axes
  x = []
  y = []
  year = listOfYears[i]
  for key, value in year.items():
    x.append(float(key))
    y.append(value)
  xArr = np.array( x )
  yArr = np.array( y )
  color = (1.0, 0.0, 1.0, i*increment)
  ax.scatter(xArr, yArr, c = cSet[i-1])
  ax.set_title(label)
  return ax

if __name__ == '__main__':
  # FuncAnimation will call the 'update' function for each frame; here
  # animating over 10 frames, with an interval of 200ms between frames.
  print("Beginning the animation")
  anim = FuncAnimation(fig, update, frames=np.arange(0, 6), interval=1000)
  if len(sys.argv) > 1 and sys.argv[1] == 'save':
    anim.save('tax-rate.gif', dpi=160, writer='imagemagick')
  else:
    # plt.show() will just loop the animation forever.
    plt.show()










#myplot = df.plot(x=[int(x) for x in list(df.columns)], y=)
