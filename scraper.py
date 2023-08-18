from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

import requests
# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("C:/Users/neeli/Downloads/chromedriver_win32 (1)/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)
# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date","hyperlink"]
planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
#4
  for i in range(0,221):
        # BeautifulSoup Object    
        soup = BeautifulSoup(browser.page_source,"html.parser") 
         # Loop to find element using XPATH
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags = ul_tag.findall("li")
            temp_list = []
            for index,li_tags in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tags.findall("a").contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")

            

       

            

              # Find all elements on the page and click to move to the next page
   

# Calling Method    


        # Find all elements on the page and click to move to the next page
       
        

# Define pandas DataFrame 










