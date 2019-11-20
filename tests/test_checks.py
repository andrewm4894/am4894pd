import pandas as pd
from am4894pd.checks import df_check_dupes, df_check_gaps
from am4894pd.utils import df_dummy_ts


def test_df_check_dupes():
    df = pd.DataFrame(
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ],
        columns=['a', 'b', 'c']
    )
    assert df_check_dupes(df, return_str=True) == "rows=3, keys=3, dupes=0, dupe_pct=0.0%"
    assert df_check_dupes(df, keys=['a'], return_str=True) == "rows=3, keys=1, dupes=2, dupe_pct=0.67%"


def test_df_check_gaps():
    df = df_dummy_ts(start='2019-01-01', end='2019-01-02', freq='1min', n_cols=1, dropna=False)
    assert df_check_gaps(df, thold=61, return_str=True) == "Gaps = 0 (0.0%)"
    assert df_check_gaps(df, thold=1, return_str=True) == "Gaps = 1440 (99.92999999999999%)"

