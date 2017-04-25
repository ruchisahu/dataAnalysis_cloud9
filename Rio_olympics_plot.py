import matplotlib
import pandas as pd
matplotlib.use('Agg')
import datetime as DT
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

df1=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/dataAnalysis_cloud9/master/olympic-games/athletes.csv')
print(df1)

df1.dtypes

sport=df1.where(df1['sport']=='aquatics')
sport.head()

df1.head()

pd.tools.plotting.scatter_matrix(df1)



#Height and Weight Analysis


fig, axs = plt.subplots(ncols=2)

df1.groupby("sex").weight.hist(alpha=0.4, ax=axs[1], bins=50)
df1.groupby("sex").height.hist(alpha=0.4, ax=axs[0], bins=50)

fig.savefig('rio_medals1.png')

#convert dob inti date


now = pd.Timestamp(DT.datetime.now())
df1['dob'] = pd.to_datetime(df1['dob'])   
df1['dob'] = df1['dob'].where(df1['dob'] < now, df1['dob'] -  np.timedelta64(100, 'Y'))   
df1['age'] = (now - df1['dob']).astype('<m8[Y]')  
fig1, axs = plt.subplots(ncols=1)

df1.dtypes

df1.groupby("sex").age.hist(alpha=0.4, bins=50)

fig1.savefig('rio_medals2.png')



#Nations

df1['nationality'].value_counts()[:30]


