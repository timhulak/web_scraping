# Standard imports
import requests as r
from bs4 import BeautifulSoup as soup
import pandas as pd

def img():
    marsImage = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    marsImageData = r.get(marsImage)
    marsImageDataSoup = soup(marsImageData.text, 'html.parser')
    marsFeatureImageUrl = marsImageDataSoup.find('div', {'class': 'carousel_container'}).find('article')['style'].split('\'')[1]

    baseUrl = 'https://www.jpl.nasa.gov/'
    featured_image_url = baseUrl + marsFeatureImageUrl
    return featured_image_url

def weather():
    marsWeather = 'https://twitter.com/MarsWxReport/status/966145463425650694'
    marsWeatherData = r.get(marsWeather)
    marsWeatherSoup = soup(marsWeatherData.text, 'html.parser')
    mars_weather = marsWeatherSoup.find_all('div', {'class': 'js-tweet-text-container'})[0].find('p').text
    return mars_weather

def facts():
    marsFacts = 'https://space-facts.com/mars/'
    tables = pd.read_html(marsFacts)
    df = tables[0]
    df.columns = ['description', 'value']
    df_table_html = df.to_html().replace('\n', '')
    return df_table_html

def hem():
    marsHemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    marsHemiData = r.get(marsHemi)
    marsHemiDataSoup = soup(marsHemiData.text, 'html.parser')
    all_list = marsHemiDataSoup.find_all('div', {'class': 'description'})
    nameList = [each.text for each in all_list]

    img_1 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'

    img_2 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'

    img_3 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'

    img_4 = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    nameUrl = [img_1, img_2, img_3, img_4]

    hemisphere_image_urls = [{'title': title, 'img_url': img_url} for title, img_url in zip(nameList, nameUrl)]

    return hemisphere_image_urls

def news():
    marsNasaUrl = 'https://mars.nasa.gov/news/'
    marsNasaUrlData = r.get(marsNasaUrl)
    marsNasaUrlSoup = soup(marsNasaUrlData.text, 'html.parser')
    marsHeadline = marsNasaUrlSoup.find('div', {'class': 'image_and_description_container'})
    news_title = marsHeadline.find_all('img')[1]['alt']
    news_p = marsHeadline.find('div', {'class': 'rollover_description_inner'}).text.strip()
    return news_title, news_p




