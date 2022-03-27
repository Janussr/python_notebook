import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Download datasettet fra dette link.   https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies """

df_movies = pd.read_csv("./Highest Holywood Grossing Movies.csv")


#1. Find the top 10 highest grossing Disney movies measured by world sales
def highest_grossing_world():
    certain_columns = df_movies[['Title', 'World Sales (in $)']]                         #Takes only the columns with these names
    df_sort_movies = certain_columns.sort_values('World Sales (in $)',ascending=False)   #Sort by world sales from highest to lowest
    top_ten = df_sort_movies.nlargest(n=10, columns=['World Sales (in $)'])              #Take top ten of the highest world sales
    print(top_ten)



#2. Create a pie chart that shows the distribution of Licenses (PG, R, M and so on)
def pie_chart_distribution():
    distribtuion = df_movies["License"].value_counts().to_dict()
    return distribtuion



#3. Get the percentage of PG rated movies between 2001 and 2015
def percent_pg_movies():
    df1 = df_movies[['License','Release Date']]                                                             #Creating our dataFrame and selecting the only two collums we need.
    df1[['Release Date', 'Year']] = df1['Release Date'].str.split(',', 1, expand=True)                      #Strip month and date from year on the comma.
    df1_filter = df1[(df1['Year'] >= " 2001") & (df1['Year'] < " 2015")]                                    #Sorts the dataframe to only include data in a specific year range.
    df1 = df1_filter['License'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'            #Counts all the different licenses and convert that into percentage.
    print('PG movies between 2001 & 2015 = ' + df1.iloc[1])       



#4. Calculate the average of world sales for each genre and visualize the data with a bar chart. (Hint: use groupBy)
def calculate_avg():
    df1 = df_movies[['License','Release Date', 'Genre', 'World Sales (in $)']]  
    
    #Hvor meget har hvert genre tjent
    #del op på hver genre, og summér dens indtjening

    df_sale = df_movies.groupby(by = ["Genre"])['World Sales (in $)'].sum().reset_index()
    df_count = df_movies.groupby(by = ["Genre"])['World Sales (in $)'].count().reset_index()
    df_average = (df_sale["World Sales (in $)"] / df_count["World Sales (in $)"]).reset_index()
    df_average['Genre'] = df_count["Genre"]

    print(df_count)



if __name__ == "__main__":
   # highest_grossing_world()
    #print(pie_chart_distribution())
    print(percent_pg_movies())