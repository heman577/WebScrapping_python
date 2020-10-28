# WebScrapping_python
Data Science Web scrapping
# Data scrapping from the wikipedia web page
#Goal is to scarp and list the countires in the wikipedia wb page

# First thing to do ,is to import the libraray to query a website
import requests

wiki_link = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"

link=requests.get(wiki_link).text

#TO check the links what you have fetcehd is corret or not

print(link)

#To parse the data return from the website

from bs4 import BeautifulSoup

#then define with the varible

soup = BeautifulSoup(link ,'lxml')

print(soup)

# it parse the html from the link variable

#prettify function will the nested structure of the html page,it will allow to see the structure of the html tags and also help with the different avaialle tags and to extact the information

print(soup.prettify())

#to play with the html tags

soup.title

#to get the string without the tags

soup.title.string

#To check the various links in the particular webpage,'a' tags

soup.a

#want all the href links

all_link =soup.find_all("a")
for link in all_link:
    print(link.get("href"))
    
#Extract information with all table tags

all_tables=soup.find_all('table')
print(all_tables)


# to identify which one is the right table,so using the attribute class of table to use it to filter the right table

right_table=soup.find('table',class_='wikitable sortable')
right_table

table_links = right_table.findAll('a')
print(table_links)

#import them to a data frame

country =[]
for links in table_links:
    country.append(links.get('title'))
print(country)

#to import in the data  frame we need to have the pandas

import pandas as pd
df=pd.DataFrame()
df['country'] = country
print(df)
