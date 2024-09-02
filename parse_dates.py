"""
Time tree estimation algorithms output estimated in different formats.
This script parses them and returns dictionary with key:value being nodeId:predictedData where predictedDate is in YYYY-MM-DD format.
"""
import pandas as pd


def input_dates(filepath: str, format: str):
    """
    :param filepath:
    :param format:
    :return:
    """
    if format == 'treetime':
        return treetime(filepath)
    pass


def treetime(filepath: str):
    def parse_id(id: str) -> int:
        if id[0] == 'N':
            return int(id[5:])
        else:
            return int(id)

    dates = pd.read_csv(filepath, sep='\t')
    dates['#node'] = dates['#node'].apply(lambda x: parse_id(x))
    dates.rename(columns={'#node': 'id'}, inplace=True)
    dates['date'] = pd.to_datetime(dates['date'], format='%Y-%m-%d')
    dates = dates[['id', 'date']]
    return dates


if __name__ == '__main__':
    treetime_dates = input_dates('/home/joel/EBI/SuperSimPy/timetree/dates.tsv', 'treetime')
    print(treetime_dates.head())
