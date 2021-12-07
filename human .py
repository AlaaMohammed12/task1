#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pyopenms import *
dig = ProteaseDigestion()
dig.getEnzymeName()
bsa = "".join([l.strip() for l in open("uniprot-yourlist_M2021120792C7BAECDB1C5C413EE0E0348724B682350617Q.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
result = []
dig.digest(bsa, result)
print(result[4].toString())
len(result)


# In[ ]:




