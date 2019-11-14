
#%%

import pandas as pd
import numpy as np
from am4894pd.utils import df_dummy_ts

df = df_dummy_ts()

#%%

df = pd.DataFrame(
    [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ],
    columns=['a', 'b', 'c']
)
print(df)

#%%


#%%

#df_dupe_check(df)
df_dupe_check(df, keys=['a'])

