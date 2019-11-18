
#%%

from am4894pd.utils import df_dummy_ts
import matplotlib.pyplot as plt

df = df_dummy_ts(n_cols=3, smooth_n=10000, smooth_f='median')

#%%

df.plot()
plt.show()


