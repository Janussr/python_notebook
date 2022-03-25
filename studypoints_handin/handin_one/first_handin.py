'''"https://www.kaggle.com/georgesaavedra/covid19-dataset

1. Hvilken måned var der flest smittede af corona for hvert land (location)?
2. Hvilket land i europa har test flest personer pr. tusinde indbyggere (total_tests_per_thousand), siden juli 2021 til nu?
3. Vis en graph af de ti lande med flest døde til dags dato.
4. Vælg tre lande og vis udviklingen af døde i forhold til total antal smittede i procent fra d. 1 april 2020 til dags dato."'''

import pandas as pd
import numpy as np

df_covid = pd.read_csv("./owid-covid-data.csv")

#total_cases, location. måske date
#1. Hvilken måned var der flest smittede af corona for hvert land (location)?

def highest_covid_cases():
    certain_columns = df_covid[['total_cases', 'location', 'date']]

    #test = certain_columns[certain_columns["location"].str.contains("High") == False] 
   # test1 = test[test["location"].str.contains("World") == False] 
    #df_sort_totalcases = test1.sort_values('total_cases',ascending=False)


    #Used to remove the last parameter of date. so you only get year and month.
    certain_columns["date"] = certain_columns["date"].map(lambda x: str(x)[:-3])


    certain_columns.set_index("location",inplace=True)
    m = certain_columns[certain_columns.groupby('date')['total_cases'].transform('max') == certain_columns['total_cases']]
   # p = m.groupby('date')['total_cases']

   # each_month = certain_columns[certain_columns.groupby("date")["total_cases"].max()]

    print(m)

   # print(m)



#2. Hvilket land i europa har testet flest personer pr. tusinde indbyggere (total_tests_per_thousand), siden juli 2021 til nu?

#new_tests,total_tests,total_tests_per_thousand,new_tests_per_thousand,new_tests_smoothed,
# new_tests_smoothed_per_thousand,positive_rate,tests_per_case,tests_units

def most_tested_eu():
    certain_columns = df_covid[['total_tests_per_thousand', 'date','location']]
    #siden 2021-07-00 til nu
    df_sort_tests = certain_columns.sort_values('total_tests_per_thousand',ascending=False)


    print(df_sort_tests)


if __name__ == "__main__":
    highest_covid_cases()
    #most_tested_eu()

