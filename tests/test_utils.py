import pandas as pd
from am4894pd.utils import df_info, df_dummy_ts


def test_df_info():
    df = pd.DataFrame([1, 2, 3, 4], columns=['x'])
    res = df_info(df=df, return_info=True)
    assert res == "Shape = (4, 1) , Cols = ['x']"


def test_df_dummy_ts():
    df = df_dummy_ts(start='2019-01-01', end='2019-01-02', freq='1min', n_cols=2, dropna=False)
    assert df.shape == (1441, 2)
    assert df.columns.tolist() == ['col0', 'col1']

