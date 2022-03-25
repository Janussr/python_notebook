"""Download datasettet fra dette link.
https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies 

1. Find the top 10 highest grossing Disney movies measured by world sales

2. Create a pie chart that shows the distribution of Licenses (PG, R, M and so on)

3. Get the percentage of PG rated movies between 2001 and 2015

4. Calculate the average of world sales for each genre and visualize the data with a bar chart. (Hint: use groupBy)
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_movies = pd.read_csv("./Highest Holywood Grossing Movies.csv")



def highest_grossing_world():
    #Takes only the columns with these names
    certain_columns = df_movies[['Title', 'World Sales (in $)']]
    #Sort by world sales from highest to lowest
    df_sort_movies = certain_columns.sort_values('World Sales (in $)',ascending=False)
    #Take top ten of the highest world sales
    top_ten = df_sort_movies.nlargest(n=10, columns=['World Sales (in $)'])
    print(top_ten)




def pie_chart_distribution():
    #certain_columns = df_movies[['Title', 'Distributor', 'License']]
    
    distribtuion = df_movies["License"].value_counts().to_dict()
    return distribtuion



#Get the percentage of PG rated movies between 2001 and 2015
#PANDAS 5-2 can see STRING MANIPULATION

#change release date to only show year (not show month)
# find antallet af pg rated movies for hvert år
#find alle licensed movies for hvert år
#find procent ved at divider pg_rated med alle movies * 100 per



if __name__ == "__main__":
   # highest_grossing_world()
    #print(pie_chart_distribution())
    print(df_movies)
