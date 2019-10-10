#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
headers = {'Content-type': 'application/json'}
data = '{"item": "latte", "Store": str001, "Quantity": 10, "deliverydate": "01/01/2019"}'
response = requests.post('http://localhost:8080/contentListener', headers=headers, data=data)


# In[ ]:




