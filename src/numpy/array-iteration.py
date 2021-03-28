#%%
import numpy as np

# %%
a=np.arange(6).reshape(3,2)
print(a)
# %%
for x in np.nditer(a):
    print(f'{x},')
# %%
