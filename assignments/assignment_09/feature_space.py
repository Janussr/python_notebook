'''week 9 Exercise Feature space¶
Ex 1

Data = 'https://think.cs.vt.edu/corgis/datasets/csv/cars/cars.csv'
Download the data

    Programatically download the data from the above link.
    Import the data into a Pandas dataframe.
    Show the head of the Pandas dataframe.

Feature engineering

    Reduce the dataset by:
        Make == Honda
        Fueltype == Gasoline
        Remove outliers. Hint: df[column name'] < df['column name'].quantile(0.90)
        Only use 2 features: 'Fuel Information.Highway mpg' and 'Engine Information.Engine Statistics.Horsepower'
        Normalize data (reduce values to be between 0 and 1)

Linear regression

    Perform linear regression where x = horsepower and y = mpg
    What is the coefficient (slope) of your model? What does this number mean?
    According to your model, what is y when x=1.
    Show the regression line on a scatterplot with the other datapoints.
'''

