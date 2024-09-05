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


class Graphs:
    def __init__(self, true_dates_path: str, source_tree_path: str, treetime_date_path=None,
                 chronumental_date_path=None, output_dir=None):
        if output_dir:
            self.output_dir = output_dir
        self.truth = input_dates('truth', datepath=true_dates_path)
        self.algorithms = dict()
        if treetime_date_path:
            self.algorithms['TreeTime'] = input_dates('treetime', datepath=treetime_date_path,
                                                      treepath=source_tree_path)
        if chronumental_date_path:
            self.algorithms['Chronumental'] = input_dates('chronumental', datepath=chronumental_date_path,
                                                          treepath=source_tree_path)

    def run_all(self):
        """
        Run all benchmarks that are available given inputted data.
        :return:
        """
        for algorithm in self.algorithms:
            self.graph(self.truth, self.algorithms[algorithm], algorithm)

    def run(self, algorithm: str):
        if algorithm in self.algorithms:
            return self.graph(self.truth, self.algorithms[algorithm], algorithm)
        else:
            raise ValueError('Algorithm not recognized!')

    def graph(self, truth, estimated, algorithm):
        comparison = compare_dataframes(truth, estimated)
        number_of_samples = (estimated.shape[0] - 1) / 2
        fig, axs = plt.subplots(2, figsize=(6, 8))
        ax1, ax2 = axs
        fig.suptitle(f'{algorithm} benchmark with {str(int(number_of_samples))} samples.')

        # Separate into internal and external nodes
        external = comparison[comparison['internal'] == False]
        internal = comparison[comparison['internal'] == True]

        # Plot true dates
        ax1.scatter(external['id'], external['date_true'], c='green', alpha=0.5, s=3, marker='^',
                    label='True external date')
        ax1.scatter(external['id'], external['date_estimated'], c='red', marker='^', s=1,
                    label='Estimated external date')
        ax1.scatter(internal['id'], internal['date_estimated'], c='red', s=3,
                    label='Estimated internal date')

        ax1.scatter(internal['id'], internal['date_true'], c='green', s=1, label='True internal date')

        ax1.legend()
        ax1.set_title('Date error per node')
        ax1.set_xlabel('Node ID (post-order)')
        ax1.set_ylabel('Date')

        ax2.scatter(comparison['date_true'], comparison['difference'], c='red', s=0.5)
        ax2.set_ylabel('Error (days)')
        ax2.set_xlabel('Node true date')
        ax2.set_ylim([-300, 800])

        if self.output_dir:
            plt.savefig(f"{self.output_dir}{algorithm}.png")
        else:
            plt.show(block=True)


if __name__ == '__main__':
    benchmarker = Graphs(true_dates_path='/home/joel/EBI/TimedTreesData/1000/dated_country_labelled_metadata.tsv',
                         source_tree_path='/home/joel/EBI/TimedTreesData/1000/sim.substitutions.tree',
                         treetime_date_path='/home/joel/EBI/TimedTreesData/1000/TreeTime/dates.tsv',
                         chronumental_date_path='/home/joel/EBI/TimedTreesData/1000/Chronumental'
                                                '/chronumental_dates.tsv')
    benchmarker.run('Chronumental')
    benchmarker.run('TreeTime')
