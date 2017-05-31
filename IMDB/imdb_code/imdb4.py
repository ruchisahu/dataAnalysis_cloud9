
import matplotlib

import pandas as pd

matplotlib.use('Agg')

import matplotlib.pyplot as plt

import numpy as np

#Read File

df=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/ml/master/imdb-5000-movie-dataset/movie_metadata.csv')


#prepare a graph:

fig=plt.figure(figsize=(10,8))


#Actors with the highest Facebook likes


actor=df.groupby(["actor_1_name"])["actor_1_facebook_likes"].sum().sort_values(ascending=False)

# select top ten actors and draw horizontal bar graph(barh)or bar

actor[:10].plot(kind='barh')


#save file

fig.savefig('actor.png')


