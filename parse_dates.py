"""
Time tree estimation algorithms output estimated in different formats.
This script parses them and returns dictionary with key:value being nodeId:predictedData where predictedDate is in YYYY-MM-DD format.
"""
import pandas as pd
from Bio import Phylo


def input_dates(estimation_source: str, **kwargs):
    """
    :param estimation_source:
    :return:
    """
    if estimation_source == 'treetime':
        df = TreeTime(**kwargs).dates
    elif estimation_source == 'truth':
        df = Truth(**kwargs).dates
    elif estimation_source == 'chronumental':
        df = Chronumental(**kwargs).dates
    else:
        raise ValueError(f'{estimation_source} is not a valid date format identifier!')
    return df.sort_values('id')


class Truth:
    def __init__(self, datepath: str):
        dates = pd.read_csv(datepath, sep='\t')
        dates.rename(columns={'strain': 'id', 'time': 'date'}, inplace=True)
        dates['date'] = pd.to_datetime(dates['date'], format='%Y-%m-%d')
        self.dates = dates[['id', 'date']]


class Chronumental:
    def __init__(self, treepath: str, datepath: str):
        if treepath is None or datepath is None:
            raise ValueError('Missing parameter for Chronumental parser!')
        print(f'Loading data for Chronumental from dates {datepath} and tree {treepath}.')
        self.tree = Phylo.read(treepath, format='newick', rooted=True)
        self.lookup = self.create_id_lookup()
        self.dates = self.get_dates(datepath)

    def create_id_lookup(self):
        lookup = set()
        for clade in self.tree.get_nonterminals():
            name = int(clade.confidence)
            if name not in lookup:
                lookup.add(name)

        return lookup

    def get_dates(self, datepath):
        dates = pd.read_csv(datepath, sep='\t')
        dates['internal'] = dates['strain'].apply(lambda x: x in self.lookup)
        dates.rename(columns={'strain': 'id', 'predicted_date': 'date'}, inplace=True)
        dates['date'] = pd.to_datetime(dates['date'], format='%Y-%m-%d %H:%M:%S.%f')
        return dates[['id', 'date', 'internal']]


class TreeTime:
    def __init__(self, treepath: str, datepath: str):
        if treepath is None or datepath is None:
            raise ValueError('Missing parameter for TreeTime parser!')
        print(f'Loading data for TreeTime from dates {datepath} and tree {treepath}.')
        self.tree = Phylo.read(treepath, format='newick', rooted=True)

        self.lookup = self.create_id_lookup()

        self.dates = self.get_dates(datepath)

    def create_id_lookup(self):
        lookup = {}
        name_set = {n.name for n in self.tree.find_clades() if n.name}
        internal_node_count = 0
        for clade in self.tree.get_nonterminals(order='preorder'):  # parents first
            if clade.name is None:
                tmp = "NODE_" + format(internal_node_count, '07d')
                while tmp in name_set:
                    internal_node_count += 1
                    tmp = "NODE_" + format(internal_node_count, '07d')
                clade.name = tmp
                name_set.add(clade.name)
                lookup[clade.name] = int(clade.confidence)
            internal_node_count += 1
            for c in clade.clades:
                c.up = clade
        return lookup

    def parse_id(self, node_id: str) -> int:
        if node_id in self.lookup:
            return self.lookup[node_id]
        return int(node_id)

    def get_dates(self, datepath):
        dates = pd.read_csv(datepath, sep='\t')
        dates['internal'] = dates['#node'].apply(lambda x: x in self.lookup)
        dates['#node'] = dates['#node'].apply(lambda x: self.parse_id(x))
        dates.rename(columns={'#node': 'id'}, inplace=True)
        dates['date'] = pd.to_datetime(dates['date'], format='%Y-%m-%d')
        return dates[['id', 'date', 'internal']]


if __name__ == '__main__':
    treetime_dates = input_dates('treetime', datepath='/home/joel/EBI/SuperSimPy/timetree/dates.tsv',
                                 treepath='/home/joel/EBI/SuperSimPy/output/sim.substitutions.tree')
    print(treetime_dates.head())
