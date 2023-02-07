#!/usr/bin/env python
# coding: utf-8

# # DEFINING GRAPH

# In[4]:


my_graph = {
    
    'S':['A','B','C'],
    'A':['S','B','D'],
    'B':['S','A','D','H'],
    'C':['S','L'],
    'D':['A','B','F'],
    'F':['D','H'],
    'H':['B','F','G'],
    'G':['H','E'],
    'L':['C','I','J'],
    'I':['L','K'],
    'J':['L','K'],
    'K':['I','J','E'],
    'E':['G','K']
    
    
}


# # DEQUE

# In[5]:


from collections import deque


# # APPLYING ALGORITHM

# In[11]:


def bfs(graph,start,goal):
    visited = []
    queue=deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited :
            visited.append(node)
            print("Have visited: ",node)
            neighbours = graph[node]
            if node == goal :
                return("Goal is reached via path: ",visited)
            for neighbours in neighbours :
                queue.append(neighbours)
    


# # (i) S to E

# In[8]:


bfs(my_graph,'S','E')


# # (ii) S to F

# In[10]:


bfs(my_graph,'S','F')

