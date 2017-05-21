import matplotlib

import pandas as pd
import datetime as DT

matplotlib.use('Agg')


import matplotlib.pyplot as plt

from matplotlib import style

import numpy as np


#Read File

data=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/dataAnalysis_cloud9/master/olympic-games/athletes.csv')

#convert dob to Age.
now = pd.Timestamp(DT.datetime.now())

data['dob'] = pd.to_datetime(data['dob'])  

data['dob'] = data['dob'].where(data['dob'] < now, data['dob'] -  np.timedelta64(100, 'Y'))  

data['age'] = (now - data['dob']).astype('<m8[Y]')  


#fillna function can “fill in” NA values with non-null data.Converted NaN values to ‘0’


data['height'] = data.height.fillna(0)

data['age'] = data.age.fillna(0)


data = data[data.height>0]

data = data[data.age>0]


female = data[data.sex == 'female']


fig=plt.figure()

legend = []


sports = ['hockey','boxing','cycling']

for sport in sports:

    plt.scatter(female.height[female.sport == sport],female.age[female.sport == sport])

    legend.append(sport)


plt.legend(legend, loc = 2,numpoints=3)


# add some text for labels, title and axes ticks

plt.title('female height and age  relation in sports?')

plt.xlabel('Height')

plt.ylabel('age')


plt.show()

fig.savefig("hight_age.png")

