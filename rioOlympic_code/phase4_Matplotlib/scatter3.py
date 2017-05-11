import matplotlib
import pandas as pd
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

# create a list of colors for each point to have
# ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'red']
colors = ['green']*(len(x)-1)
colors.append('red')
fig=plt.figure()

# plot the point with size 100 and chosen colors
plt.scatter(x, y, s=100, c=colors)
fig.savefig('scatter.png')
