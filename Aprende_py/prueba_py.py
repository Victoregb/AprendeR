#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as skl
# %%
comp1 = 12
comp2 = 45

comp1+comp2
# %%
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'iris_class']
df  = pd.read_csv('iris.data', names=col_names)

# %%
df
# %%
df.sepal_length
# %%
