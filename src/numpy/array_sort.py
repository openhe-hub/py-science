# %%
import numpy as np

# %%
a=np.array([[3,7],[9,1]])
print(a)
# %%
print(np.sort(a))
# %%
print(np.sort(a,axis=0))
# %%
dt = np.dtype([('name',  'S10'),('age',  int)]) 
a = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)  
print ('array：')
print (a)
print ('\n')
print ('sort by name：')
print (np.sort(a, order =  'name'))
# %%
