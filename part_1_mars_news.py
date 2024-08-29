#!/usr/bin/env python
# coding: utf-8

# # Module 11 Challenge
# ## Deliverable 1: Scrape Titles and Preview Text from Mars News

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup


# In[3]:


browser = Browser('chrome')


# ### Step 1: Visit the Website
# 
# 1. Use automated browsing to visit the [Mars news site](https://static.bc-edx.com/data/web/mars_news/index.html). Inspect the page to identify which elements to scrape.
# 
#       > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools.

# In[6]:


# Visit the Mars news site
url = 'https://static.bc-edx.com/data/web/mars_news/index.html'
browser.visit(url)


# ### Step 2: Scrape the Website
# 
# Create a Beautiful Soup object and use it to extract text elements from the website.

# In[9]:


# Create a Beautiful Soup object
html = browser.html
news_soup = soup(html, 'html.parser')


# In[11]:


# Extract all the text elements
text_elements = news_soup.find_all('div' , class_='list_text')
text_elements


# ### Step 3: Store the Results
# 
# Extract the titles and preview text of the news articles that you scraped. Store the scraping results in Python data structures as follows:
# 
# * Store each title-and-preview pair in a Python dictionary. And, give each dictionary two keys: `title` and `preview`. An example is the following:
# 
#   ```python
#   {'title': "NASA's MAVEN Observes Martian Light Show Caused by Major Solar Storm", 
#    'preview': "For the first time in its eight years orbiting Mars, NASA’s MAVEN mission witnessed two different types of ultraviolet aurorae simultaneously, the result of solar storms that began on Aug. 27."
#   }
#   ```
# 
# * Store all the dictionaries in a Python list.
# 
# * Print the list in your notebook.

# In[20]:


# Create an empty list to store the dictionaries
news_items = []


# In[22]:


# Loop through the text elements
# Extract the title and preview text from the elements
# Store each title and preview pair in a dictionary
# Add the dictionary to the list
for el in text_elements:
    title = el.find('div', class_='content_title').text
    preview = el.find('div', class_='article_teaser_body').text
    new_item = {
        'title' : title,
        'preview' : preview
    }
    news_items.append(new_item)


# In[24]:


# Print the list to confirm success
news_items


# In[26]:


browser.quit()


# In[ ]:




