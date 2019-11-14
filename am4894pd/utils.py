import pandas as pd
import numpy as np


def df_info(df: pd.DataFrame, return_info=False, shape=True, cols=True, info_prefix=''):
    """ Print a string to describe a df.
    """
    info = info_prefix
    if shape:
        info = f'{info}Shape = {df.shape}'
    if cols:
        info = f'{info} , Cols = {df.columns.tolist()}'
    print(info)
    if return_info:
        return info


def df_dummy_ts(start='2019-01-01', end='2019-01-02', freq='1s', n_cols=5):
    """ Make dummy ts df.
    """
    time_range = pd.DataFrame(pd.date_range(start, end, freq=freq), columns=['time'])
    data = pd.DataFrame(np.random.randn(len(time_range), n_cols), columns=[f'col{n}' for n in range(n_cols)])
    df = pd.concat([time_range, data], axis=1)
    return df


def df_dupe_check(df: pd.DataFrame, keys: list = None, return_str=False):
    """Given a df and list of keys print some info on dupes.
    """
    if keys:
        df_keys = df[keys]
    else:
        df_keys = df.index.to_series()
    num_keys = len(df_keys.drop_duplicates())
    num_rows = len(df)
    num_dupes = num_rows - num_keys
    dupe_pct = round(num_dupes / num_rows, 2)
    ret_str = f'rows={num_rows}, keys={num_keys}, dupes={num_dupes}, dupe_pct={dupe_pct}%'
    print(ret_str)
    if return_str:
        return ret_str

