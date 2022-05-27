#!/usr/bin/env python
# coding: utf-8

# In[46]:


import networkx as nx


# In[47]:


G =nx.Graph()


# In[48]:


G.add_nodes_from(['a','b','c','d'])


# In[49]:


G.add_edges_from([('a','b'),('b','c'),('c','d'),('a','c')])


# In[50]:


nx.draw(G,with_labels=True,node_color='yellow',node_size=2000,font_size=20,font_color='blue')


# In[23]:


G.nodes()


# In[51]:


G.edges()


# In[52]:


G.number_of_nodes()


# In[53]:


G.number_of_edges()


# In[54]:


for i in G.neighbors('a'):
    print(i)


# In[55]:


G.has_node('a')


# In[56]:


G.has_edge('a','d')


# In[57]:


list(G.neighbors('a'))


# In[58]:


nx.is_tree(G)


# In[59]:


nx.is_connected(G)


# In[60]:


G.degree('a')


# In[61]:


di=nx.DiGraph()


# In[62]:


di.add_edges_from([('a','c'),('c','d'),('b','d'),('c','e')])


# In[63]:


nx.is_tree(di)


# In[65]:


nx.draw(di,with_labels=True,node_color='yellow',node_size=2000,font_size=20,font_color='blue')


# In[ ]:




