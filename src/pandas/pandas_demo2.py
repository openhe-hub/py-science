#%%
import pandas as pd
import numpy as np

# %%
df=pd.DataFrame(np.random.randn(10,4))
df
# %%
# 1. concat
pieces=[df[:3],df[3:7],df[7:]]
pieces
# %%
pd.concat(pieces)
# %%
# 2. join with sql style
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
left
# %%
right
# %%
pd.merge(left, right,on='key')

# %%
# 3. append
df=pd.DataFrame(np.random.randn(8,4), columns=list('ABCD'))
df
# %%
piece=df.iloc[3]
df=df.append(piece,ignore_index=True)
df
# %%
