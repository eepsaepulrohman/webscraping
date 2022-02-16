#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request, json, pandas as pd


# In[ ]:


df_shopee_item_append = pd.DataFrame()

shopee_url = 'https://shopee.co.id/api/v4/search/search_items?by=relevancy&limit=60&match_id=1028154&newest=0&order=desc&page_type=collection&scenario=PAGE_COLLECTION_SEARCH&version=2'
print(shopee_url)
with urllib.request.urlopen(shopee_url) as url:
    data_shopee = json.loads(url.read().decode())


# In[ ]:


df_shopee = pd.DataFrame.from_dict(data_shopee,orient='index')
df_shopee = pd.DataFrame(df_shopee.transpose())
df_shopee_item = pd.DataFrame(df_shopee['items'])
df_shopee_item = pd.DataFrame(df_shopee_item['items'].values.tolist())
df_shopee_item = df_shopee_item.transpose()
df_shopee_item = pd.DataFrame(df_shopee_item[0].values.tolist())

df_shopee_item.append = df_shopee_item_append.append(df_shopee_item,ignore_index=True)


# In[ ]:


df_shopee_item.append


# In[ ]:


Data = pd.DataFrame(df_shopee_item.append[['item_basic','itemid','shopid']])
Data


# In[ ]:


Data.to_csv('webscarp_itemid.csv', sep=',')

