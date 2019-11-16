import pandas as pd
import numpy as np


def df_check_dupes(df: pd.DataFrame, keys: list = None, return_str: bool = False):
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


def df_check_gaps(df: pd.DataFrame, key: str = None, thold: float = 1, sort: bool = True, return_str: bool = False):
    """Check for gaps in time based key.
    """
    num_rows = len(df)
    if key:
        key_data = df[key]
    else:
        key_data = df.index.to_series()
    if sort:
        key_data = key_data.sort_values()
    gap_secs = (key_data - key_data.shift(1)).dt.total_seconds()
    gaps = gap_secs[gap_secs > thold]
    num_gaps = len(gaps)
    pct_gaps = round(num_gaps / num_rows, 4) * 100
    ret_str = f'Gaps = {num_gaps} ({pct_gaps}%)'
    print(ret_str)
    if return_str:
        return ret_str


