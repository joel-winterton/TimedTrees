"""
ENTRYPOINT.
This script accepts dataset paths and outputs benchmarks.
Currently implemented:
1. TreeTime
"""
import matplotlib.pyplot as plt
from parse_dates import input_dates
from compare_dataframes import compare_dataframes

import matplotlib as mpl

mpl.rcParams['figure.dpi'] = 600


class Benchmark:
    def __init__(self, true_dates_path: str, source_tree_path: str, treetime_date_path=None, ):
        self.truth = input_dates('truth', datepath=true_dates_path)
        if treetime_date_path:
            self.treetime = input_dates('treetime', datepath=treetime_date_path, treepath=source_tree_path)
        treetime_errors = compare_dataframes(self.truth, self.treetime)

        fig, ax = plt.subplots()
        # Separate into internal and external nodes
        external = treetime_errors[treetime_errors['internal'] == False]
        internal = treetime_errors[treetime_errors['internal'] == True]

        # Plot true dates
        ax.scatter(external['id'], external['date_true'], c='green', alpha=0.5, s=3, marker='^',
                   label='True external date')
        ax.scatter(external['id'], external['date_estimated'], c='red', marker='^', s=1,
                   label='Estimated external date')
        ax.scatter(internal['id'], internal['date_estimated'], c='red', s=3,
                   label='Estimated internal date')

        ax.scatter(internal['id'], internal['date_true'], c='green', s=1, label='True internal date')

        ax.legend()
        ax.set_title('Date error per node')
        ax.set_xlabel('Node ID (post-order)')
        ax.set_ylabel('Date')
        plt.show(block=True)
        fig1, ax1 = plt.subplots()
        ax1.scatter(treetime_errors['date_true'], treetime_errors['difference'], c='red', s=0.5)
        ax1.set_ylabel('Error (days)')
        ax1.set_xlabel('Node true date')
        plt.show(block=True)


if __name__ == '__main__':
    benchmarked = Benchmark(true_dates_path='/home/joel/EBI/SuperSimPy/output/dated_country_labelled_metadata.tsv',
                            source_tree_path='/home/joel/EBI/SuperSimPy/output/sim.substitutions.tree',
                            treetime_date_path='/home/joel/EBI/SuperSimPy/timetree/dates.tsv')
