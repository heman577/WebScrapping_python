
# coding: utf-8

# In[ ]:


# Data scrapping from the wikipedia web page
#Goal is to scarp and list the countires in the wikipedia wb page


# In[5]:



# First thing to do ,is to import the libraray to query a website
import requests
#Specify the urls
wiki_link = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"

link=requests.get(wiki_link).text


# In[6]:


#TO check the links what you have fetcehd is corret or not

print(link)


# In[ ]:


#To parse the data return from the website


# In[7]:


from bs4 import BeautifulSoup
#then define with the varible
soup = BeautifulSoup(link ,'lxml')
print(soup)
# it parse the html fromm the link variable


# In[ ]:


#prettify function will the nested structure of the html page,it will allow to see the structure of the html tags and also help with the different avaialle tags
# and to extact the information


# In[8]:


print(soup.prettify())


# In[9]:


#to play with the html tags
soup.title


# In[10]:


#to get the string without the tags
soup.title.string


# In[11]:


#To check the various links in the particular webpage,'a' tags

soup.a


# In[12]:


# to extract all the links which has the "a" tags in it will be using
soup.find_all("a")


# In[14]:


#want all the href links
all_link =soup.find_all("a")
for link in all_link:
    print(link.get("href"))


# In[ ]:


#Extract information with all table tags


# In[15]:


all_tables=soup.find_all('table')
print(all_tables)


# In[ ]:


# to identify which one is the right table,so using the attribute class of table to use it to filter the right table


# In[16]:


right_table=soup.find('table',class_='wikitable sortable')
right_table


# In[18]:


table_links = right_table.findAll('a')
print(table_links)


# In[19]:


#import them to a data frame

country =[]
for links in table_links:
    country.append(links.get('title'))
print(country)


# In[21]:


#to import in the data  frame we need to have the pandas
import pandas as pd
df=pd.DataFrame()
df['country'] = country
print(df)

