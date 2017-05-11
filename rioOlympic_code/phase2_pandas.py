
import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/dataAnalysis_cloud9/master/olympic-games/athletes.csv')

print(df['sport'])

print(df[['sport','name']])

athletic=df.where(df['sport']=='athletics')

print(athletic.head())

