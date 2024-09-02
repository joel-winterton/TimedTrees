# TreeTime
## Setup
Installation instructions can be found here: https://treetime.readthedocs.io/en/latest/installation.html
There's nothing special about this setup, just make sure you're able to `import TreeTime`.
## How to use
Navigate to the SuperSimPy output folder.
```shell
treetime --tree sim.substitutions.tree --dates full_metadata.csv --outdir timetree --name-column strain --date-column time --sequence-length=31101
```
