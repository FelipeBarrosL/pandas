import pandas as pd
import re

df = pd.read_csv(r"pandas/pokemon_database/pokemon_data.csv")

#Learning data structure
print(df.tail(10))
print(df.columns)

#Selecting data 
print(df[['Name', 'Type 1', 'Speed']][1:5])

#Printing all names
for index, row in df.iterrows():
   print(index,row['Name'])

#Selecting and sorting grass type
print(df.loc[df['Type 1'] =='Grass'])
print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))

#Creating new columns for Total Power and the top 5
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.sort_values(['Total']).head(5))
df = df.drop(columns=['Total'])
print(df.head(4))
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(4))

#Changing type of single row
df.loc[df['Name'] == 'Ivysaur', 'Type 1'] = 'Felipe'
print(df.loc[df['Name'] == 'Ivysaur'])
df.loc[df['Name'] == 'Ivysaur', 'Type 1'] = 'Grass'
print(df.loc[df['Name'] == 'Ivysaur'])

#Printing names containg 'pi'
print(df.loc[df['Name'].str.contains('^pi[a-z]', flags = re.I, regex=True)])

#Grouping types 
print(df.groupby(['Type 1']).count()['#'])