
import pandas as pd

#Reading data from csv file

df=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/ml/master/imdb-5000-movie-dataset/movie_metadata.csv')

#print(df)

#print (df.head(5) ) #Prints first 5  observations


#get the columns of the data

#print(df.columns)


#printing the column

#print(df['director_name'])

#print(df[['director_name','num_critic_for_reviews']])

#imdb_score is more than 7.5

rating = df[df['imdb_score'] >7.5]

print(rating)

