
#importing libraries

import matplotlib

import pandas as pd

matplotlib.use('Agg')

import matplotlib.pyplot as plt



#read data from file

df=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/ml/master/imdb-5000-movie-dataset/movie_metadata.csv')


#Draw plot

fig=plt.figure()


#select top 5 directors(feel free to use any other columns like genres,actor_1_name,language,country)

sizes = df["director_name"].value_counts()[:5]

print(sizes)

#select list of 5 colors of your choice

colors = ['turquoise','orange','lightgreen','red','purple']


#plt.pie() takes two values data and the colors:

plt.pie( sizes, colors=colors)



#•(Optional) The legend() method adds the legend to the plot. A legend is a label or description of the values shown.


plt.legend(sizes.index, loc =3)


# add some text for labels, title and axes ticks

plt.title('% of directors total movies')

plt.show()

fig.savefig("pie.png")

