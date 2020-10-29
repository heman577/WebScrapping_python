
# coding: utf-8

# In[2]:


import bs4
import requests
from bs4 import BeautifulSoup


# In[3]:


#to get the url
price_link ="https://finance.yahoo.com/quote/FB?p=FB"


# In[5]:


link=requests.get(price_link).text


# In[6]:


print(link)


# In[16]:


#to get the stock_price
soup=BeautifulSoup(link,'lxml')


# In[18]:


soup.find_all('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px)"})


# In[26]:


soup.find_all('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span')


# In[27]:


soup.find_all('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text


# In[ ]:


#fuction and while loop
    #price_link ="https://finance.yahoo.com/quote/FB?p=FB"
def parsePrice():
    link=requests.get(price_link).text
    soup=BeautifulSoup(link,'lxml')
    price=soup.find_all('div',{'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
    return price
while True:
    print('the current price: '+str(parsePrice()))

