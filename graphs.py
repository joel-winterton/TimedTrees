"""
ENTRYPOINT.
This script accepts dataset paths and outputs benchmarks.
Currently implemented:
1. TreeTime
"""

from parse_dates import input_dates
from compare_dataframes import compare_dataframes

import datetime
import matplotlib as mpl
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mpl.rcParams['figure.dpi'] = 600
mpl.rcParams.update({'figure.autolayout': True})

sns.set(style="whitegrid", palette="pastel", color_codes=True)


class Graphs:
    def __init__(self, true_dates_path: str, source_tree_path: str, treetime_date_path=None,
                 chronumental_date_path=None, output_dir=None):
        self.output_dir = output_dir
        self.truth = input_dates('truth', datepath=true_dates_path)
        self.number_of_samples = str(int((self.truth.shape[0] - 1) / 2))
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
        self.violin_plot()
        for algo1 in self.algorithms:
            self.graph(self.truth, self.algorithms[algo1], algo1)

    def run(self, algorithm: str):
        if algorithm in self.algorithms:
            return self.graph(self.truth, self.algorithms[algorithm], algorithm)
        else:
            raise ValueError('Algorithm not recognized!')

    def violin_plot(self):
        """
        Violin plot for each month of internal nodes months membership distribution for each algorithm passed.
        :param algorithm:
        :param internal_datasets:
        :return:
        """
        grouped_internal_algos = dict()
        for algo in self.algorithms:
            dataset = compare_dataframes(self.truth,self.algorithms[algo])
            internal = dataset[dataset['internal'] == True]
            grouped_internal_algos[algo] = pd.DataFrame(data={
                'date_true': internal['date_true'].apply(lambda x: datetime.date(x.year, x.month, 1)),
                'difference': internal['difference']})

        grouped_internal = pd.concat(grouped_internal_algos, names=['algorithm'])

        f, ax = plt.subplots(figsize=(8, 4))
        sns.violinplot(x="date_true", y="difference", data=grouped_internal, density_norm='count', hue='algorithm')
        sns.despine(left=True)

        f.suptitle(f'Monthly error distributions with {self.number_of_samples} samples.')
        ax.set_xlabel("True date")
        ax.set_ylabel("Error (days)")
        if self.output_dir:
            plt.savefig(f"{self.output_dir} violin.png")
        else:
            plt.show()

    def scatter_plots(self, algorithm: str, internal, external):
        """
        Plots two scatter plots:
        1. True date vs Estimated date
        2. True date vs Error (days)
        :param algorithm:
        :param internal:
        :param external:
        :return:
        """
        fig, axs = plt.subplots(2, figsize=(6, 8))
        ax1, ax2 = axs
        fig.suptitle(f'{algorithm} benchmark with {str(int(self.number_of_samples))} samples.')
        ax1.scatter(external['date_true'], external['date_estimated'], c='blue', s=0.5,
                    label='External nodes date')
        ax1.scatter(internal['date_true'], internal['date_estimated'], c='orange', s=0.5,
                    label='Internal nodes date')
        ax1.plot(internal['date_true'], internal['date_true'], linestyle='dotted', c='grey', zorder=2)
        ax1.plot(external['date_true'], external['date_true'], linestyle='dotted', c='grey', zorder=2)

        ax1.legend()
        ax1.set_title('Date estimation comparison')
        ax1.set_xlabel('True date of node')
        ax1.set_ylabel('Estimated date of node')
        ax1.set_ylim([datetime.date(2018, 1, 1), datetime.date(2020, 10, 1)])
        ax2.scatter(internal['date_true'], internal['difference'], c='red', s=0.5)
        ax2.scatter(external['date_true'], external['difference'], c='red', s=0.5)
        ax2.set_ylabel('Error (days)')
        ax2.set_xlabel('Node true date')
        ax2.set_ylim([-300, 800])

        if self.output_dir:
            plt.savefig(f"{self.output_dir}{algorithm} scatter.png")
        else:
            plt.show(block=True)

    def graph(self, truth, estimated, algorithm):
        comparison = compare_dataframes(truth, estimated)
        # Separate into internal and external nodes
        external = comparison[comparison['internal'] == False]
        internal = comparison[comparison['internal'] == True]

        self.scatter_plots(algorithm, internal, external)


if __name__ == '__main__':
    benchmarker = Graphs(true_dates_path='/home/joel/EBI/TimedTreesData/1000/dated_country_labelled_metadata.tsv',
                         source_tree_path='/home/joel/EBI/TimedTreesData/1000/sim.substitutions.tree',
                         treetime_date_path='/home/joel/EBI/TimedTreesData/1000/TreeTime/dates.tsv',
                         chronumental_date_path='/home/joel/EBI/TimedTreesData/1000/Chronumental'
                                                '/chronumental_dates.tsv')
    benchmarker.run_all()
