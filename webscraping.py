
from bs4 import BeautifulSoup
import requests
import pandas as pd

# downloading the web page 
page= requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")

# BeautifulSoup class to parse the page
soup= BeautifulSoup(page.content, 'html.parser')

# examples of web scraping based on special ids & class (the output of each variable is available in outputs.txt)
forecast =soup.find(id='seven-day-forecast')
forecast_items=forecast.find_all(class_='tombstone-container')
first_item = forecast_items[0]
period = first_item.find(class_="period-name").get_text()
short_Desc = first_item.find(class_= "short-desc").get_text()
temp=first_item.find(class_="temp temp-high").get_text()
image = first_item.find('img')
describtion=image['title']


# select all tags with class= 'period-name' in tombstone-container class
period_tags = forecast.select(".tombstone-container .period-name")

# get the text of each period_tags variable
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text() for sd in forecast.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in forecast.select(".tombstone-container .temp")]
descs = [d["title"] for d in forecast.select(".tombstone-container img")]

# Combining extracted data into a Pandas Dataframe (you need to import pandas )
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temperature":temps,
    "desc":descs
})

# create and open a data.txt file to write some data
with open('data.txt', 'w') as file:
     file.write(str(weather))

