#!/usr/bin/env python
# coding: utf-8

# In[59]:


from readit import read_data, write_req_tidy_data
df = read_data('data/2020RES_APR2019PubDataShare.csv')
write_req_tidy_data(df)

