import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)


"""1. Lav en metode der tjekker om det er fredag ved at webscrape på følgende link (Metoden skal returnere Ja eller Nej)    https://www.erdetfredag.dk/"""

def is_it_friday():
 url = 'https://www.erdetfredag.dk'

 browser.get(url)
 browser.implicitly_wait(2)

 answer = browser.find_element_by_id('answer').text
 print(answer)


       

"""2. Lav en metode der returnerer top 5 mest populære opskrifter fra nemlig.com   https://www.nemlig.com/"""

def top_five_nemlig_recipes():
 browser.get('https://www.nemlig.com/')  #Get the website
 browser.implicitly_wait(2)              #wait two seconds I dont think its necessary



"""3. Lav en metode der kan finde den totale pris af disse fire udvalgte varer på nemlig.com   (Gær, Minimælk, Banan, Tomatpasta)"""

def price_of_four_items():
    browser.get('https://www.nemlig.com')
    browser.implicitly_wait(2)
    browser.maximize_window()

    food = ['gær', 'minimælk', 'banan', 'tomatpasta']
    integer_prices = []
    decimal_prices = []

    #Search for each item in the items list
    searchField = browser.find_element_by_xpath('//*[@id="site-header-search-field-main"]')
    searchField.click()
    for item in food:
        searchField.send_keys(item)
        searchField.submit()
        browser.implicitly_wait(2)
        
    #Get the integer of the price and the decimal of the price and add to seperate lists
        integer_price = float(browser.find_element_by_xpath('//*[@id="searchscrollable"]/div/searchresult/div[1]/div[3]/div[1]/div[1]/div[1]/productlist-item[1]/a/div/div[3]/pricecontainer/div/div[2]/span').text)
        integer_prices.append(integer_price)
    
        decimal_price = float(browser.find_element_by_xpath('//*[@id="searchscrollable"]/div/searchresult/div[1]/div[3]/div[1]/div[1]/div[1]/productlist-item[1]/a/div/div[3]/pricecontainer/div/div[2]/sup').text)/100
        decimal_prices.append(decimal_price)

        searchField.clear()
    
    #Add the two lists together and print total
    item_prices = np.add(integer_prices, decimal_prices)
    total = 0
    for i in range(0, len(item_prices)):    
       total = total + item_prices[i];    
    print(str(total) + ' kr.')
    return total 

"""4. Lav et barchart over alle Womens Fiction bøgerne på følgende hjemmeside. Sorter efter pris.   http://books.toscrape.com/index.html"""

if __name__ == "__main__":
   is_it_friday()
   #top_five_nemlig_recipes()
   #price_of_four_items()
