"""
Creates chronumental friendly files from SuperSimPy output.
"""
import argparse
import pandas as pd
from Bio import Phylo
import os

parser = argparse.ArgumentParser(
    prog='TimeTreeChronumentalPrep',
    description="Prepares SuperSimPy output to be in correct format for Chronumental.")
parser.add_argument('-d', '--datapath')
parser.add_argument('-s', '--sites', default=31101)

args = vars(parser.parse_args())
sim_data_path = args['datapath'] if args['datapath'][-1] == '/' else args['datapath'] + '/'
genome_length = args['sites']

mut_tree = Phylo.read(sim_data_path + 'sim.substitutions.tree', 'newick', rooted=True)


def scale_tree(root):
    stack = [root.clade]
    while stack:
        node = stack.pop()
        node.branch_length *= genome_length
        if not node.is_terminal():
            for clade in node.clades:
                stack.append(clade)

    return root


rescaled_tree = scale_tree(mut_tree)
output_path = sim_data_path + 'Chronumental/'
os.mkdir(output_path)
Phylo.write(rescaled_tree, output_path + 'input.tree', 'newick')

dates = pd.read_csv(sim_data_path + 'dated_metadata.csv')
dates.rename(columns={'time': 'date'}, inplace=True)
dates = dates[['strain', 'date']]
dates.to_csv(output_path + 'dates.csv', index=False)
