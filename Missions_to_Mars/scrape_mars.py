from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'templates/chromedriver'}
    return Browser('chrome', **executable_path, headless=True)

def scrape_all():
    news_title, news_p = scrape_mars_news()
    mars = {
        'news_title': news_title,
        'news_p': news_p,
        'featured_image_url': scrape_mars_image(),
        'fact_table': scrape_mars_facts(),
        'hemisphere_images_urls': scrape_mars_hemispheres()
    }

    return mars

def scrape_mars_news():

    browser = init_browser()
    news_url = 'https://redplanetscience.com/'
    browser.visit(news_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text

    browser.quit()    

    return news_title, news_p

def scrape_mars_image():

    browser = init_browser()

    images_url = 'https://spaceimages-mars.com/'
    browser.visit(images_url)
    browser.links.find_by_partial_text('FULL IMAGE')
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image = soup.find('img', class_='headerimage')['src']    
    featured_image_url = images_url + featured_image
    
    browser.quit()   
    
    return featured_image_url

def scrape_mars_facts():
    facts_url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(facts_url)
    mars_df = tables[1]

    mars_df.columns = ['Parameter', 'Value']
    mars_df.set_index('Parameter', inplace = True)
    fact_table = mars_df.to_html()
    fact_table.replace('\n', '')
    
    return fact_table

def scrape_mars_hemispheres():

    browser = init_browser()

    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)   

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

    for item in items:
        title = item.find('h3').text
        hemisphere_url = 'https://marshemispheres.com/' + item.find('a', class_='itemLink product-item')['href']
        
        browser.visit(hemisphere_url)
 
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
 
        hemisphere_image_url = 'https://marshemispheres.com/' + soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({'title': title, 'img_url': hemisphere_image_url})
        
    browser.quit()   
        
    return hemisphere_image_urls