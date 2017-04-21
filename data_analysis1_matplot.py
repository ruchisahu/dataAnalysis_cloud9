import matplotlib
import pandas as pd
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df1=pd.read_csv('http://winterolympicsmedals.com/medals.csv')
print(df1)

sport=df1.where(df1['Sport']=='Skating')
sport.head()

df1.head()

pd.tools.plotting.scatter_matrix(df1)


ax=df1.plot()
fig=ax.get_figure()
fig.savefig('image_medals.png')