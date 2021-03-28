#%%
import pandas as pd
import numpy as np
import openpyxl

# %%
df=pd.read_csv("data_in.csv",sep=',')
df
# %%
result=df.describe()
# %%
result
# %%
result.to_csv("data_out.csv")
# %%
df=pd.read_excel("data_in.xlsx")
df
# %%
result=df.describe()
result.to_excel("data_out.xlsx")
# %%
