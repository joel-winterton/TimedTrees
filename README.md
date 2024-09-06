# Timed Trees
This repository contains the code necessary to reproduce each of the benchmarked methods for creating timed trees on pandemic-scale phylogenetic trees, as well as visualise results.
Each method is benchmarked using data simulated from the pipeline https://github.com/joely-w/SuperSimPy. All preprocessing steps assume you have all the output data from a SuperSimPy simulation.


The EBI HPC was used to run large sample simulations using SuperSimPy.
Contact me if you want to use these.

## Generating Graphs
  <img src="https://github.com/user-attachments/assets/14a1033d-5cf1-4596-8f5b-b5ab2433a66c" alt="Chronumental violin plot" />
  <img src="https://github.com/user-attachments/assets/9911019f-d7ec-4e8a-bea0-31d23c0da2b2" alt="Chronumental scatter plot"/> 

The visualisation script currently outputs error visualisations for TreeTime and Chronumental (the script will visualise all algorithm estimates passed to it that it accepts).

Chronumental data flag: `--dates_chronumental=<path to dates tsv output by Chronumental`

TreeTime data flag: `--dates_treetime=<path to dates.tsv file from TreeTime output>`

```shell
python3 benchmark.py --output_dir=OUTPUT_DIR --dates_true=TRUE_DATES_TSV --tree_true=TRUE_NEWICK_TREE --dates_chronumental=CHRONUMENTAL_ESTIMATED_DATES_TSV --dates_treetime=TREETIME_ESTIMATED_DATES_TSV
```
## Benchmarked methods
Each method has its own directory, with a README.md on how to run the method from the simulated data. 
Current methods are: 
### Chronumental 
**Method and implementation source:** 
*Sanderson, T., 2021. Chronumental: time tree estimation from very large phylogenies. https://doi.org/10.1101/2021.10.27.465994*

**Folder**: `/Chronumental`

### Least Squares Dating 
**Method source:** 

*Thu-Hien To, Matthieu Jung, Samantha Lycett, Olivier Gascuel, Fast Dating Using Least-Squares Criteria and Algorithms, Systematic Biology, Volume 65, Issue 1, January 2016, Pages 82–97, https://doi.org/10.1093/sysbio/syv068*

**Implementation source:** 

*Bui Quang Minh, Heiko A Schmidt, Olga Chernomor, Dominik Schrempf, Michael D Woodhams, Arndt von Haeseler, Robert Lanfear, IQ-TREE 2: New Models and Efficient Methods for Phylogenetic Inference in the Genomic Era, Molecular Biology and Evolution, Volume 37, Issue 5, May 2020, Pages 1530–1534, https://doi.org/10.1093/molbev/msaa015*

**Folder**: `/LSD`
### TreeTime
**Method and implementation source:** 

*Sagulenko, P., Puller, V., & Neher, R. A. (2018). TreeTime: Maximum-likelihood phylodynamic analysis. Virus Evolution, 4(1). https://doi.org/10.1093/ve/vex042*

**Folder:**: `/TreeTime`
