#similar to 10-Stu_Scrape_Weather/Solved/scrape_surfing.py and exercise 9 and the pandas scrape from day 2.  
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path":'/usr/local/bin/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)
#creating a function that will scrape all of the info we need 
#and put it in a dictionary (set?) that we can use for our dynamic interface

def scrape():
    browser = init_browser()
   
    marsinfo = {}
    
    # Mars News site scrape
    marsurl =  "https://mars.nasa.gov/news"
    browser.visit(marsurl)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    marsinfo["news_title"] = soup.find("div", class_="content_title").get_text()
    marsinfo["news_p"] = soup.find("div", class_="article_teaser_body").get_text()
    
    #image scrape
    jplurl = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jplurl)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    elem = img_soup.find(id="")
    marsinfo["featured_image_url"] = elem.find("img", class_="fancybox-image")["src"]
    
    #facts scrape
    df = pd.read_html('http://space-facts.com/mars/')[0]
    df.columns=['description', 'value']
    df.set_index('description', inplace=True)
    marsinfo["facts"] = df.to_html(classes="table table-striped")
    
    #mars weather scrape 
    weatherurl =  "https://twitter.com/marswxreport?lang=en"
    browser.visit(weatherurl)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    marsinfo["weather_tweet"] = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
    browser.quit()
    return marsinfo