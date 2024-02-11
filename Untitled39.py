#!/usr/bin/env python
# coding: utf-8

# ## WEB SCRAPPING OF TABLES

# In[18]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[19]:


url = "https://finance.yahoo.com/currencies/"
response = requests.get(url)


# In[24]:


soup = BeautifulSoup(response.content, "html.parser")
table = soup.find('table')
rows = table.find_all('tr')
data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)
df = pd.DataFrame(data, columns=['Symbol','Name', 'Last Price', 'Change','% Change', '52 Week Range','Day Chart'])


# In[25]:


print(df)


# In[ ]:




