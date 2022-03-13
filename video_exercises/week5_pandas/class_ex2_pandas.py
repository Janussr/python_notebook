"""02 Exercise Pandas Data Series

The CO2 Emission data set above is not updated since 2014

    

    Find the 10 Countries/Regions with the highest emissions in 2014 and show emission numbers (reverse sorted)
    Remove if you can those rows that are not countries (regions and aggregated groups) (hint: ISO 3166, Alpha-3 country codes, a csv file can be found here: /data/country_codes.csv)
        Find the 10 countries with highest emissions in 2014
    Plot the emissions of China and USA over time respectively

"""
import pandas as pd

#Create a Pandas Series with emission data from 2014 for each country or region

data = pd.read_csv('data/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_1345584.csv', skiprows=4)

emission_country = pd.Series(data=data["2014"].values, index = data ["Country Code"])
print(emission_country[:100])

