import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)
ax.hist(np.random.randn(1000))
fig.savefig('display.svg') 