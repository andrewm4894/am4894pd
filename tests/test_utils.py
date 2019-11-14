import pandas as pd
from am4894pd.utils import df_info, df_dummy_ts


def test_df_info():
    df = pd.DataFrame([1, 2, 3, 4], columns=['x'])
    res = df_info(df=df, return_info=True)
    assert res == "Shape = (4, 1) , Cols = ['x']"


def test_df_dummy_ts():
    df = df_dummy_ts()
    assert df.shape == (86401, 6)
    assert df.columns.tolist() == ['time', 'col0', 'col1', 'col2', 'col3', 'col4']
