import matplotlib

import pandas as pd

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from matplotlib import style

import numpy as np


read data from file

data=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/dataAnalysis_cloud9/master/olympic-games/athletes.csv')




#fillna function can “fill in” NA values with non-null data.Converted NaN(missing values) values to ‘0’

data['weight'] = data.weight.fillna(0)  

data['height'] = data.height.fillna(0)


#copy all the values greater than 0 and leave 0 and (-) numbers.

data = data[data.weight>0]

data = data[data.height>0]


#separate male and female data

males = data[data.sex == 'male']

females = data[data.sex == 'female']

fig=plt.figure()

legend = []

#select sports you want to analyse(feel free to choose any number of sports )

sports = ['volleyball','basketball','football']

for sport in sports:

    plt.scatter(males.height[males.sport == sport],males.weight[males.sport == sport])

    legend.append(sport)


#(optional)The legend() method adds the legend to the plot.Legend is a label/description

plt.legend(legend, loc = 2,numpoints=3)


#(optional)

plt.title('height and weight  difference in sports?')

plt.xlabel('Height [m]')

plt.ylabel('Weight [kg]')

plt.show()

fig.savefig("hight_weight.png")

