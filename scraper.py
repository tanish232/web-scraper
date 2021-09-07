from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv 

START_URL='https://exoplanets.nasa.gov/exoplanet-catalog'
browser = webdriver.Chrome("C:/Users/HP/Desktop/pythonVenv/myEnv/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=['name','light_years_from_earth','planet_mass','stellar_magnitude','discovery_date']
    planet_data=[]
for i in range(0,428):
    soup=BeautifulSoup(browser.page_source,"html.parser")
    for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
        li_tags=ul_tag.find_all('li')
        temp_list=[]
        for index,li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append('')
            hyperlink_li_tag=li_tags[0]
            temp_list.append('https://exoplanets.nasa.gov'+hyperlink_li_tag.find_all('a'),href=True)[0]['href']
            planet_data.append(temp_list)
        browser.find_element_py_xpath('//*[@id="primary_column"]/div[1]/div[3]/div[2]/a').click()

        with open('scraper.csv','w') as f:
            csvwriter=csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(planet_data)

scrape()