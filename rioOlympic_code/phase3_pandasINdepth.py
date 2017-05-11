
import pandas as pd
import numpy as np

#Reading data from csv file

df=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/dataAnalysis_cloud9/master/olympic-games/athletes.csv')

# Nations value count


print( df['nationality'].value_counts()[:30])


# print total medals

gold = df.groupby('nationality').sum()['gold']

silver = df.groupby('nationality').sum()['silver']

bronze = df.groupby('nationality').sum()['bronze']

total_medals = gold + silver + bronze

print(total_medals)


print(gold['USA'])


import datetime as DT

now = pd.Timestamp(DT.datetime.now())

df['dob'] = pd.to_datetime(df['dob'])  

df['dob'] = df['dob'].where(df['dob'] < now, df['dob'] -  np.timedelta64(100, 'Y'))  

df['age'] = (now - df['dob']).astype('<m8[Y]')  


print(df)
