"""
This is used once a time tree estimation algorithm output has been converted to the correct dataframe.
This simply compares dataframes by outputting sums and graphs of defined error functions.
Current error functions to implement:
    1. Square error
    2. Absolute error

Both dataframes should have columns with formats: id: int, date: datetime(%Y-%m-%d)
"""
import pandas as pd


def compare_dataframes(truth, estimation):
    """
    Creates dataframe to compare dates, input dataframes must both have columns id: int, date: datetime(%Y-%m-%d)
    :param truth: Dataframe of true dates
    :param estimation: Dataframe of estimated dates
    :return: Dataframe with columns id: int, date_true: datetime(%Y-%m-%d),  date_estimated: datetime(%Y-%m-%d)
    """
    result = pd.merge(truth, estimation, on='id', how='outer', suffixes=('_true', '_estimated'))
    result['difference'] = (result['date_true'] - result['date_estimated']).dt.days
    return result
