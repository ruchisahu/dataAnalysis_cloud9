
import matplotlib

import pandas as pd

matplotlib.use('Agg')

import matplotlib.pyplot as plt

from matplotlib import style

import numpy as np


#Read File

data=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/dataAnalysis_cloud9/master/olympic-games/athletes.csv')


#convert dob to Age.you can use the method, used previously

for i,row in enumerate(data.iterrows()):

    try:

        data.loc[i,'Age'] = 116 - float(row[1].dob[len(row[1].dob)-2:len(row[1].dob)])

    except TypeError:

        data.loc[i,'Age'] = 0


#fillna function can “fill in” NA values with non-null data.Converted NaN values to ‘0’

data['weight'] = data.weight.fillna(0)

data['height'] = data.height.fillna(0)

data = data[data.weight>0]

data = data[data.height>0]

data = data[data.Age>0]


female = data[data.sex == 'female']


fig=plt.figure()

legend = []


sports = ['hockey','boxing','cycling']

for sport in sports:

    plt.scatter(female.height[female.sport == sport],female.Age[female.sport == sport])

    legend.append(sport)


plt.legend(legend, loc = 2,numpoints=3)


# add some text for labels, title and axes ticks

plt.title('female height and age  relation in sports?')

plt.xlabel('Height [m]')

plt.ylabel('age [kg]')


plt.show()

fig.savefig("hight_age.png")

