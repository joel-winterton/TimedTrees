# Chronumental 
## Setup
```shell
pip install chronumental
```
## How to use
Navigate into the root of this repository.
Then prepare the SuperSimPy output directory using: 
```shell
python3 Chronumental/prepare_sim.py --datapath=<absolute path to SuperSimPy output dir>
```
Chronumental can then be run on the simulation: 

```shell
cd <path to SuperSimPy output dir>/Chronumental
chronumental --tree input.tree --dates dates.csv --name_all_nodes --only_use_full_dates
```