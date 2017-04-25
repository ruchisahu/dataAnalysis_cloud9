iimport pandas as pd



df=pd.read_csv('https://raw.githubusercontent.com/ruchisahu/dataAnalysis_cloud9/master/olympic-games/athletes.csv')
# show first few rows

print(df.head())

# Nations

athletes_count = df['nationality'].value_counts()

print( df['nationality'].value_counts()[:30])
# medals

gold = df.groupby('nationality').sum()['gold']
silver = df.groupby('nationality').sum()['silver']
bronze = df.groupby('nationality').sum()['bronze']

total_medals = gold + silver + bronze

print(total_medals)

print(gold['USA'])



