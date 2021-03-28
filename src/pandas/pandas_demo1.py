#%%
import numpy as np
from numpy.core.fromnumeric import size
import pandas as pd
# %%
data1=pd.Series([1,3,5,np.nan,6,8])
data1
# %%
dates=pd.date_range("20210312",periods=10,freq='D')
dates #use date as row (index)
# %%
data2=pd.DataFrame(np.random.randint(low=1,high=10,size=[10,4]),index=dates,columns=list('ABCD'))
data2
# %%
data3=pd.DataFrame({
    'Date':pd.Series(dates)[1:5],
    'Type':pd.Categorical(['train','plane','ship','test']),
    'Price':np.abs(np.random.randn(4)),
    'Gender':'Male'
})
data3
# %%
#query info
data3.head()
# %%
data3.head(1)
# %%
data3.tail(1)
# %%
data3.index
data2.index
# %%
data3.columns
# %%
#data analysis
data3.describe()
# %%
data3['Price'].mean()
# %%
data3.sort_values('Price')
# %%
data3.sort_values('Price', ascending=False)
# %%
#data query
#loc query by label
data3.loc[1:3,['Date','Price']]
# %%
data3.loc[1,'Price']
# %%
#iloc query by index
data3.iloc[:,0:]
# %%
data3.iloc[0:2,1:]
# %%
data3.iat[1,1]
# %%
data3[data3['Price']>0.2]

# %%
