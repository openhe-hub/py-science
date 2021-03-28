#%%
import numpy as np
from numpy.matrixlib.defmatrix import matrix
# %%
a=np.arange(1,13,1)
a=a.reshape(3,4)
b=matrix(a)
print(b)
# %%
print(f'size={b.shape}')
print(f'first row={b[0,:]}')
print(f'first column={b[:,0]}')
print(f'transpose={b.T}')
# %%
c=matrix(np.eye(4,4))
print(c)
print(np.linalg.det(c))
# %%
print(np.dot(b,c))
# %%
d=matrix(np.random.rand(3,4))
print(d)

# %%
print(b+d)
print(b-d)
# %%
a = np.array([[1,2],
                 [3,4]])
b = np.array([[5,6],
                 [7,8]])
print(a*b)
# %%
