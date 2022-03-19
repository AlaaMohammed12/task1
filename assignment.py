#!/usr/bin/env python
# coding: utf-8

# In[48]:


import cobra


# In[49]:


from cobra import Model,Reaction,Metabolite


# In[50]:


model=Model('task')


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

M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000


# In[51]:


glc =Metabolite('glc',compartment='c')
AA =Metabolite('AA',compartment='c')
Biomass =Metabolite('Biomass',compartment='c')


# In[52]:


v0.add_metabolites({glc:1})
v0


# In[53]:


v1.add_metabolites({glc:-1,AA:1})
v1


# In[54]:


v2.add_metabolites({AA:-9.09,Biomass:1})
v2


# In[55]:


M.add_metabolites({Biomass:-1})
M


# In[56]:


model.add_reactions([v0,v1,v2,M])


# In[57]:


model.objective='M'


# In[58]:


model.optimize()


# In[65]:


cobra.io.save_json_model(model,"Test2.json")


# In[66]:


import escher


# In[67]:


from escher import Builder


# In[68]:


cobra.io.load_json_model("Test2.json")


# In[69]:


build= Builder(model_json="Test2.json")


# In[70]:


build


# In[ ]:




