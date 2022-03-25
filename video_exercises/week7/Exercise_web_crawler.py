import bs4
import requests


r = requests.get(' https://www.cphbusiness.dk/')
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

#print(soup.prettify()[:1500])

for link in soup.find_all('a'):
  if(str(link.get('href'))).startswith('https') == True:
    print(link.get('href'))

    