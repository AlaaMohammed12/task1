#!/usr/bin/env python
# coding: utf-8

# In[14]:


import cobra


# In[15]:


from cobra import Model,Reaction,Metabolite


# In[26]:


model=Model('example')


v0=Reaction('v0')
v0.name='V0'
v0.lower_bound=1
v0.upper_bound=1


v1=Reaction('v1')
v1.name='V1'
v1.lower_bound=0
v1.upper_bound=1000


v2=Reaction('v2')
v2.name='V2'
v2.lower_bound=0
v2.upper_bound=1000


v3=Reaction('v3')
v3.name='v3'
v3.lower_bound=0.9
v3.upper_bound=0.9


ATP_R=Reaction('ATP')
ATP_R.name='ATP'
ATP_R.lower_bound=0
ATP_R.upper_bound=1000


M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[27]:


A=Metabolite('A',compartment='c')
B=Metabolite('B',compartment='c')
C=Metabolite('C',compartment='c')
ATP=Metabolite('ATP',compartment='c')


# In[28]:


v0.add_metabolites({A:1})
v0


# In[29]:


v1.add_metabolites({A:-1,B:1})
v1


# In[30]:


v2.add_metabolites({B:-1,C:1})
v2


# In[31]:


v3.add_metabolites({ATP:-1})
v3


# In[32]:


M.add_metabolites({C:-1})
M


# In[33]:


ATP_R.add_metabolites({A:-1,ATP:1})
ATP_R


# In[34]:


model.add_reactions([v0,v1,v2,v3,M,ATP_R])


# In[35]:


model.objective='M'


# In[36]:


model.optimize()


# In[ ]:




