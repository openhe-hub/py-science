#%%
import numpy as np

# %%
# generate random numbers in [0,1)
data=np.random.rand(100)
print(data)
# %%
print("min=",np.amin(data,0))# 0 is axis number
print("max=",np.amax(data,0))
print("mean=",np.mean(data))
print("max-min=",np.ptp(data))
print("median=",np.median(data))
print("standard-deviation=",np.std(data))
print("variance=",np.var(data))
# %%
