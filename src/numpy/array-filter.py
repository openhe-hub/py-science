# %%
import numpy as np

# %%
a = np.random.randint(low=1, high=100, size=[10, 10])
print(a)
# use function 'where' to filter
odd=a[np.where(a%2==1)]
print(odd)

# %%
