
#%%

import pandas as pd
import numpy as np
from am4894pd.utils import df_dummy_ts
from am4894pd.checks import df_check_dupes, df_check_gaps

df = df_dummy_ts()

#%%

df_check_gaps(df, thold=0.99)

