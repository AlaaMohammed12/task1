#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install pyopenms


# In[2]:


import pyopenms as ms
sum_=0
seq=ms.AASequence.fromString("VAKA")
for aa in seq:
    sum_+=aa.getMonoWeight()
sum_


# In[4]:


seq=ms.AASequence.fromString("VAKA")
total=seq.getMonoWeight()
total


# In[5]:


total==sum_

