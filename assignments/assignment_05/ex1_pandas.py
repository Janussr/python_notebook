import pandas as pd 

url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&K%C3%98N=1%2C2&ALDER=*&CIVILSTAND=U%2CG&Tid=2020K4'
df = pd.read_csv(url, sep=';')

url1 = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=*&K%C3%98N=1%2C2&ALDER=*&CIVILSTAND=U%2CG&Tid=2008K4'
df1 = pd.read_csv(url1, sep=';')

# 2020 data
test = df[(df['CIVILSTAND']=='Gift/separeret') & (df['ALDER']=='I alt') & (df['OMRÅDE']=='Hele landet')  & (df['KØN']=='Mænd')]
stats = test[['INDHOLD']].apply(pd.to_numeric)
#print(test)
#print(stats)

# 2008 data
test1 = df1[(df1['CIVILSTAND']=='Gift/separeret') & (df1['ALDER']=='I alt') & (df1['OMRÅDE']=='Hele landet')  & (df1['KØN']=='Mænd')]
stats1 = test1[['INDHOLD']].apply(pd.to_numeric)
#print(test1)
#print(stats1)




#print('The difference between divorced danes in 2008 to 2020 in percent ->')
##diff = stats-stats1
#print(str(round((diff/stats1) * 100, 2)) + '%')

#1072984 - 1096210 = -23226
#( -23226 / 1096210 ) · 100 = -2.12% 






if __name__ == "__main__":
  print(())