#!/usr/bin/env python
# coding: utf-8

# # Module 11 Challenge
# ## Deliverable 2: Scrape and Analyze Mars Weather Data

# In[10]:


# Import relevant libraries
from splinter import Browser
from bs4 import BeautifulSoup as soup
import matplotlib.pyplot as plt
import pandas as pd


# In[12]:


browser = Browser('chrome')


# ### Step 1: Visit the Website
# 
# Use automated browsing to visit the [Mars Temperature Data Site](https://static.bc-edx.com/data/web/mars_facts/temperature.html). Inspect the page to identify which elements to scrape.
# 
#    > **Hint** To identify which elements to scrape, you might want to inspect the page by using Chrome DevTools to discover whether the table contains usable classes.
# 

# In[15]:


# Visit the website
# https://static.bc-edx.com/data/web/mars_facts/temperature.html
url = "https://static.bc-edx.com/data/web/mars_facts/temperature.html"
browser.visit(url)


# ### Step 2: Scrape the Table
# 
# Create a Beautiful Soup object and use it to scrape the data in the HTML table.
# 
# Note that this can also be achieved by using the Pandas `read_html` function. However, use Beautiful Soup here to continue sharpening your web scraping skills.

# In[18]:


# Create a Beautiful Soup Object
html = browser.html
html_soup = soup(html, 'html.parser')


# In[19]:


# Extract all rows of data
rows = html_soup.find_all('tr', class_='data-row')


# ### Step 3: Store the Data
# 
# Assemble the scraped data into a Pandas DataFrame. The columns should have the same headings as the table on the website. Here’s an explanation of the column headings:
# 
# * `id`: the identification number of a single transmission from the Curiosity rover
# * `terrestrial_date`: the date on Earth
# * `sol`: the number of elapsed sols (Martian days) since Curiosity landed on Mars
# * `ls`: the solar longitude
# * `month`: the Martian month
# * `min_temp`: the minimum temperature, in Celsius, of a single Martian day (sol)
# * `pressure`: The atmospheric pressure at Curiosity's location

# In[23]:


# Create an empty list
list_of_rows = []

# Loop through the scraped data to create a list of rows
for row in rows:
    td =row.find_all('td')
    row = [col.text for col in td]
    list_of_rows.append(row)


# In[29]:


# Create a Pandas DataFrame by using the list of rows and a list of the column names
df = pd.DataFrame(list_of_rows, columns=['id','terrestrial_date', 'sol',
                                    'ls', 'month', 'min_temp', 'pressure'])


# In[31]:


# Confirm DataFrame was created successfully
df.head()


# ### Step 4: Prepare Data for Analysis
# 
# Examine the data types that are currently associated with each column. If necessary, cast (or convert) the data to the appropriate `datetime`, `int`, or `float` data types.
# 
#   > **Hint** You can use the Pandas `astype` and `to_datetime` methods to accomplish this task.
# 

# In[34]:


# Examine data type of each column
df.dtypes


# In[36]:


# Change data types for data analysis
df.terrestrial_date = pd.to_datetime(df.terrestrial_date)
df.sol = df.sol.astype('int')
df.ls = df.ls.astype('int')
df.month = df.month.astype('int')
df.min_temp = df.min_temp.astype('float')
df.pressure = df.pressure.astype('float')


# In[38]:


# Confirm type changes were successful by examining data types again
df.dtypes


# ### Step 5: Analyze the Data
# 
# Analyze your dataset by using Pandas functions to answer the following questions:
# 
# 1. How many months exist on Mars?
# 2. How many Martian (and not Earth) days worth of data exist in the scraped dataset?
# 3. What are the coldest and the warmest months on Mars (at the location of Curiosity)? To answer this question:
#     * Find the average the minimum daily temperature for all of the months.
#     * Plot the results as a bar chart.
# 4. Which months have the lowest and the highest atmospheric pressure on Mars? To answer this question:
#     * Find the average the daily atmospheric pressure of all the months.
#     * Plot the results as a bar chart.
# 5. About how many terrestrial (Earth) days exist in a Martian year? To answer this question:
#     * Consider how many days elapse on Earth in the time that Mars circles the Sun once.
#     * Visually estimate the result by plotting the daily minimum temperature.
# 

# In[41]:


# 1. How many months are there on Mars?
df['month'].value_counts().sort_index()


# In[13]:


# 2. How many sols (Martian days) worth of data are there?
df['sol'].unique()


# In[43]:


# 3. What is the average minimum temperature by month?
min_temp_month = df.groupby('month')['min_temp'].mean()
min_temp_month


# In[45]:


# Plot the average minimum temperature by month
min_temp_month.plot(kind='bar')
plt.ylabel('temp in C')
plt.show


# In[49]:


# Identify the coldest and hottest months in Curiosity's location by sorting the previous graph
min_temp_month.sort_values().plot(kind='bar')
plt.ylabel('temp in C')
plt.show()


# In[62]:


# 4. What is the average pressure by month?
pressure_month = df.groupby('month')['pressure'].mean()


# In[64]:


# Plot the average pressure by month
pressure_month.sort_values().plot(kind='bar')
plt.ylabel('Atmospheric pressure')
plt.show()


# In[51]:


# Identify the lowest and highest pressure months in Curiosity's location by sorting the previous graph
min_temp_month.sort_values().plot(kind='bar')
plt.ylabel('temp in C')
plt.show()


# In[53]:


# 5. How many terrestrial (Earth) days are there in a Martian year?
# Visually estimate the result by plotting the daily minimum temperature of each observation in the data set.
df.min_temp.plot()
plt.xlabel('Number of terrestrial days')
plt.ylabel('min temp')
plt.show()


# #### Minimum Temperature
# 
# YOUR ANALYSIS HERE

# #### Atmospheric Pressure
# 
# YOUR ANALYSIS HERE

# #### Year Length
# 
# YOUR ANALYSIS HERE

# ### Step 6: Save the Data
# 
# Export the DataFrame to a CSV file.

# In[58]:


# Write the data to a CSV
df.to_csv('mars_data.csv',index=False)


# In[60]:


browser.quit()


# In[ ]:




