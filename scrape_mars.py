import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser


def scrape():
    url = "https://mars.nasa.gov/news/"
    browser = Browser('chrome', headless=True)
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')
	
	# create empty dicitonary
	marsData = {}
	
    contentTitle = soup.find('div', class_='content_title').find('a')
    contentTitle

    news_title = contentTitle.text.strip()
    news_title

    articleBody = soup.find('div', class_='article_teaser_body')
    articleBody

    news_p = articleBody.text.strip()
    news_p
	
	# begin populating dictionary
	marsData["news_title"]=news_title
	marsData["news_p"]=news_p
	
	
    browser = Browser('chrome', headless=True)
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    fullImage = soup.find('a', class_="button fancybox")
    fullImage

    imageLink = soup.find('a',{'data-fancybox-href': True}).get('data-fancybox-href')
    imageLink

	baseURL = 'https://www.jpl.nasa.gov'
    featured_image_url = baseURL + imageLink
    featured_image_url

	marsData["featured_image_url"]=featured_image_url
	
    browser = Browser('chrome',headless=True)
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    weather_tweet = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    mars_weather = weather_tweet.text.strip()
    mars_weather

	marsData["mars_weather"]=mars_weather
	
	
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    tables

    df = tables[0]
    df.head()

    table = df.to_html()
	
	marsData["table"]=table
	

    browser = Browser('chrome', headless=True)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    headlines = soup.find_all('h3')
    headlines

    headlinesStripped = [h3.text.strip() for h3 in headlines]
    headlinesStripped

    imageLinks = []
    fi1 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"
    fi2 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"
    fi3 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"
    fi4 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"
    imageLinks = [fi1, fi2, fi3, fi4]

    hemisphereLinks = [{'title': headline, 'img_url':imageLink} for headline, imageLink in zip(headlines,imageLinks)] 
    
	marsData["hemisphereLinks"]=hemisphereLinks
	
	print(marsData["featured_image_url"])
	
	return marsData

if __name__ == "__main__":
    scrape()

