import matplotlib
import pandas as pd
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np






weather_seattle = pd.read_csv('https://raw.githubusercontent.com/ruchisahu/dataAnalysis_cloud9/master/seattle-weather.csv')

print(weather_seattle)


weather_detail=weather_seattle['weather']

sun=weather_detail.str.contains('sun')
print(sun[:5])

ax=weather_seattle.plot()
fig=ax.get_figure()
fig.savefig('weather_seattle.png')

print(weather_seattle['weather'].value_counts())

