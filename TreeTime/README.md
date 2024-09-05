# TreeTime
## Setup
Installation instructions can be found here: https://treetime.readthedocs.io/en/latest/installation.html
There's nothing special about this setup, just make sure you're able to `import TreeTime`.
## How to use
Navigate to the SuperSimPy output folder.
```shell
treetime --tree sim.substitutions.tree --dates dated_metadata.csv --outdir TreeTime --name-column strain --date-column time --sequence-length=31101 --keep-root --coalescent=skyline --stochastic-resolve
```
