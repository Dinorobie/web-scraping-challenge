#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from flask import Flask, render_template, redirect
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[26]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # NASA Mars News
# 
# 

# In[27]:


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html=browser.html
soup=bs(html,'html.parser')


# In[28]:


news_title=soup.find_all('div', class_='content_title')[0].text
news_p=soup.find_all('div', class_='rollover_description_inner')[0].text
news_title
news_p


# # PL Mars Space Images - Featured Image

# In[29]:


jpl_url="spaceimages-mars.com"
jpl_image_url="https://spaceimages-mars.com/"
browser.visit(jpl_image_url)


# In[30]:


html=browser.html
soup=bs(html,"html.parser")
image_url=soup.find_all('article')


# In[31]:


print(image_url)


# # Mars Facts

# In[32]:


# Scrape Mars facts from https://space-facts.com/mars/
url='https://galaxyfacts-mars.com/'
db=pd.read_html(url)
db


# In[33]:


mars_db=db[0]
mars_db=mars_db.rename(columns={0:"Profile",1:"Value"},errors="raise")
mars_db.set_index("Profile",inplace=True)
mars_db


# In[34]:


mars_db.to_html()


# # Mars Hemispheres

# In[35]:


url ='https://marshemispheres.com/'
browser.visit(url)
html=browser.html
soup=bs(html,'html.parser')


# In[36]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

#url to scrap
url = 'https://marshemispheres.com/'
browser.visit(url)

hemisphere_image_urls = []

for i in range(0, 4):
    
    links_found = browser.links.find_by_partial_text('Hemisphere Enhanced')
    links_found[i].click()
    html = browser.html
    soup = bs(html, 'html.parser')
    
    title = soup.find('h2', class_= 'title').text
    
    img_url = soup.find('div', class_= 'downloads')
    img_url = img_url.find('a', target= '_blank')['href']
    img_url = 'https://marshemispheres.com/' + img_url
    
    hemisphere_image_urls.append({
        'Title': title,
        'Image URL': img_url
    })
    
    browser.links.find_by_partial_text('Back').click()

#End browser session
browser.quit()


# In[ ]:




