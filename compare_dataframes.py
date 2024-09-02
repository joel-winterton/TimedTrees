"""
This is used once a time tree estimation algorithm output has been converted to the correct dataframe.
This simply compares dataframes by outputting sums and graphs of defined error functions.
Current error functions to implement:
    1. Square error
    2. Absolute error

Both dataframes should have columns with formats: id: int, date: datetime(%Y-%m-%d)
"""


def compare_dataframes(df1, df2):
    """

    :param df1:
    :param df2:
    :return:
    """
    result = df1.merge(df2, on='id', how='outer', left_suffix='_left', right_suffix='_right')
