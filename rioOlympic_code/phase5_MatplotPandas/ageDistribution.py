import matplotlib
import pandas as pd
matplotlib.use('Agg')
import datetime as DT
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')

df1=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/dataAnalysis_cloud9/master/olympic-games/athletes.csv')
#print(df1)


#convert dob inti date

now = pd.Timestamp(DT.datetime.now())

df1['dob'] = pd.to_datetime(df1['dob'])  

df1['dob'] = df1['dob'].where(df1['dob'] < now, df1['dob'] -  np.timedelta64(100, 'Y'))  

df1['age'] = (now - df1['dob']).astype('<m8[Y]')  


#prepare a graph:

fig, axs = plt.subplots()

df1.groupby("age").age.hist(alpha=0.4, bins=2)

fig.savefig('rio_age.png')

