import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Download datasettet fra dette link.   https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies """

df_movies = pd.read_csv("./Highest Holywood Grossing Movies.csv")


#1. Find the top 10 highest grossing Disney movies measured by world sales
def highest_grossing_world():
    certain_columns = df_movies[['Title', 'World Sales (in $)']]                         #Takes only the columns with these names
    df_sort_movies = certain_columns.sort_values('World Sales (in $)',ascending=False)   #Sort by world sales from highest to lowest (IKKE NØDVENDIGT DA NLARGEST SORTERE SÅ SORT_VALUES ER LIGEGYLDIG HER)
    top_ten = df_sort_movies.nlargest(n=10, columns=['World Sales (in $)'])              #Take top ten of the highest world sales
    print(top_ten)



#2. Create a pie chart that shows the distribution of Licenses (PG, R, M and so on)
def pie_chart_distribution():
    distribtuion = df_movies["License"].value_counts().to_dict()          #convert to dictionary to get key value pair, to make the pie chart. (key = license, value = pg, pg-13 etc)      
    return distribtuion



#3. Get the percentage of PG rated movies between 2001 and 2015
def percent_pg_movies():
    df1 = df_movies[['License','Release Date']]                                                             #Creating our dataFrame and selecting the only two collums we need.
    df1[['Release Date', 'Year']] = df1['Release Date'].str.split(',', 1, expand=True)                      #Strip month and date from year on the comma.  (First half creates a new colum "year"(the reason we type releaste date is to tell where to place the colum year). Expand true, tells all data to go to the new colum "year")
    df1_filter = df1[(df1['Year'] >= " 2001") & (df1['Year'] < " 2015")]                                    #Sorts the dataframe to only include data in a specific year range 2001-2015.   -> # normalize = true --> data_norm = (data - data.min())/ (data.max() - data.min())

    df1 = df1_filter['License'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'            #Counts all the different licenses and convert that into percentage.
    print('PG movies between 2001 & 2015 = ' + df1.iloc[1])                                                 #iloc[1] - is to get license PG and not any of the others.



#4. Calculate the average of world sales for each genre and visualize the data with a bar chart. (Hint: use groupBy)
def calculate_avg():
    df1 = df_movies[['License','Release Date', 'Genre', 'World Sales (in $)']]  
    
    #Hvor meget har hvert genre tjent
    #del op på hver genre, og summér dens indtjening

    df2 = df1['Genre'].str.replace(",", "")
    df2 = df1['Genre'].str.get_dummies(sep=",")

    print(df2)



if __name__ == "__main__":
    #print(highest_grossing_world())       #Assignment 1 - uncomment
    #print(pie_chart_distribution())       #Assignment 2 - check pie chart.ipynb
  #  print(percent_pg_movies())            #Assignment 3 - uncomment
    print(calculate_avg())                  #Assignment 4 - not finished