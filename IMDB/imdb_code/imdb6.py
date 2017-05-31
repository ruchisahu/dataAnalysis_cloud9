
#import libraries

import matplotlib

import pandas as pd

matplotlib.use('Agg')


import matplotlib.pyplot as plt

#read File

df=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/ml/master/imdb-5000-movie-dataset/movie_metadata.csv')


#fillna function can “fill in” NA values with non-null data.Converted NaN values to ‘0’

df['imdb_score'] = df.imdb_score.fillna(0)

df['title_year'] = df.title_year.fillna(0)

df = df[df.imdb_score>0]

df = df[df.title_year>0]


fig=plt.figure()

legend = []


director = ['Peter Jackson','Steven Spielberg' ,"Anthony Russo ","Ridley Scott","Lucifer Valentine","Alfred Hitchcock","John Ford"]

for dir in director:

    plt.scatter(df.imdb_score[df.director_name==dir],df.title_year[df.director_name==dir])

       

    legend.append(dir)

    


# add some text for labels, title and axes ticks

plt.legend(legend, loc =3)

plt.title('Can we seperate directors rating')

plt.xlabel('Rating')

plt.ylabel('year')

plt.show()

fig.savefig("director1.png")


