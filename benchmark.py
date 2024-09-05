import argparse
from graphs import Graphs

parser = argparse.ArgumentParser(
    prog='TimeTreeBenchmarker',
    description="Command line interface to run benchmarks on time tree estimation algorithm outputs.")
parser.add_argument('-o', '--output_dir', required=True)
parser.add_argument('-d', '--dates_true', required=True, help='Path to dated metadata TSV.')
parser.add_argument('-t', '--tree_true', required=True,
                    help='Path to substitutions per site scaled phylogeny in Newick format.')
parser.add_argument('-d1', '--dates_treetime', required=False, help='Path to dates TSV outputted from TreeTime.')
parser.add_argument('-d2', '--dates_chronumental', required=False,
                    help='Path to dates TSV outputted from Chronumental.')

args = vars(parser.parse_args())
graph_args = dict()
graph_args['output_dir'] = args['output_dir'] if args['output_dir'][-1] == '/' else args['output_dir'] + '/'
graph_args['true_dates_path'] = args['dates_true']
graph_args['source_tree_path'] = args['tree_true']

if 'dates_treetime' in args:
    graph_args['treetime_date_path'] = args['dates_treetime']
if 'dates_chronumental' in args:
    graph_args['chronumental_date_path'] = args['dates_chronumental']
print("Creating graphs!")
grapher = Graphs(*graph_args)
grapher.run_all()