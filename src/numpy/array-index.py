# %%
import numpy as np
# %%
a = np.arange(1, 11, 1)
print(a)
# %%
print(a[0:2])
# %%
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[1:3, 1:3])
# %%
# : or ... can get all elements in vector
print(b[:, 1:3])
print(b[..., 1:3])
# %%
# bool index operation
print(b[b > 5])

# %%
c = np.array([1, 2+6j, 5,  3.5+5j])
print(c.dtype)
print(c[np.iscomplex(c)])
# %%
