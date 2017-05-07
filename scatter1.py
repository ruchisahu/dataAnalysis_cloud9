import matplotlib
import pandas as pd
matplotlib.use('Agg')
import datetime as DT
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
y = x

fig=plt.figure()
plt.scatter(x, y) 

fig.savefig('test2.png')