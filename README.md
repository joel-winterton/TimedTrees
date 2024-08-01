# Timed Trees
This repository contains the code necessary to reproduce each of the benchmarked methods for creating timed trees on pandemic-scale phylogenetic trees.
Each method is benchmarked using data simulated from the pipeline https://github.com/joely-w/SuperSimPy. All preprocessing steps assume you have all the output data from a SuperSimPy simulation.

The EBI HPC was used to run large sample simulations using SuperSimPy, specifically several 500k, 1 million and 5 million sample trees.
Contact me if you want to use these.

## Benchmarked methods
Each method has its own directory, with a README.md on how to run the method from the simulated data. 
Current methods are: 

### Least Squares Dating 
**Method source:** *Thu-Hien To, Matthieu Jung, Samantha Lycett, Olivier Gascuel, Fast Dating Using Least-Squares Criteria and Algorithms, Systematic Biology, Volume 65, Issue 1, January 2016, Pages 82–97, https://doi.org/10.1093/sysbio/syv068*

**Implementation source:** *Bui Quang Minh, Heiko A Schmidt, Olga Chernomor, Dominik Schrempf, Michael D Woodhams, Arndt von Haeseler, Robert Lanfear, IQ-TREE 2: New Models and Efficient Methods for Phylogenetic Inference in the Genomic Era, Molecular Biology and Evolution, Volume 37, Issue 5, May 2020, Pages 1530–1534, https://doi.org/10.1093/molbev/msaa015*

**Folder**: `/LSD`