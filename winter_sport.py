import matplotlib
import pandas as pd
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df1=pd.read_csv('http://winterolympicsmedals.com/medals.csv')
print(df1)


print(df1['City'])
print(df1[['City','Year']])

print(df1['City'].value_counts())

counts=df1['City'].value_counts()
ax=counts.plot(kind='bar')
fig=ax.get_figure()
fig.savefig('image_medals.bar.png')

sport=df1.where(df1['Sport']=='Skating')
sport.head()

df1.head()

pd.tools.plotting.scatter_matrix(df1)


ax=df1.plot()
fig=ax.get_figure()
fig.savefig('image_medals.png')

ax=df1.plot(figsize=(15,10))
fig=ax.get_figure()
fig.savefig('image_medals_big.png')
