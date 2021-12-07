#!/usr/bin/env python
# coding: utf-8

# In[5]:


from pyopenms import *
dig = ProteaseDigestion()
dig.getEnzymeName()
bsa = "".join([l.strip() for l in open("uniprot-yourlist_M202111206320BA52A5CE8FCD097CB85A53697A352FF2B4H.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
result = []
dig.digest(bsa, result)
print(result[4].toString())
len(result)


# In[ ]:




