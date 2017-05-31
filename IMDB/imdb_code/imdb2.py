
import pandas as pd

#Reading data from csv file

df=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/ml/master/imdb-5000-movie-dataset/movie_metadata.csv')


#Total countries on IMDB

country = df['country'].value_counts()

#print(country)

#Gross income by directors and sort by values

df_gross = df.groupby('director_name')['gross'].sum()
#print(df_gross.sort_values(ascending=False).head(20))

# Number of movies released  every year

df_movies_year = df.groupby(['title_year'])['movie_title'].count()

#print(df_movies_year)


#Calculate unique language

print(df['language'].unique())

