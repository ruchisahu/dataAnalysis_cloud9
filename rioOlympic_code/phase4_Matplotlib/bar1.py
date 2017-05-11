
import matplotlib
import pandas as pd
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


linear_data = np.array([1,2,3,4,5,6,7,8,9,10])
fig=plt.figure()
xvals = range(len(linear_data))
plt.bar(xvals, linear_data, width = 0.3)
fig.savefig('bar.png')