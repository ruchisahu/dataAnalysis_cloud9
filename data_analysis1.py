import pandas as pd

df1=pd.read_csv('http://winterolympicsmedals.com/medals.csv')
print(df1)

sport=df1.where(df1['Sport']=='Skating')
sport.head()

df1.head()

