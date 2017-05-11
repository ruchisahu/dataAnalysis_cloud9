
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

linear_data = np.array([1,2,3,4])
exponential_data = linear_data**2
fig=plt.figure()
# plot the linear data and the exponential data
plt.plot(linear_data, '-o', exponential_data, '-o')
plt.xlabel('x value')
plt.ylabel('y value')
plt.title(' title')
fig.savefig('line.png')


