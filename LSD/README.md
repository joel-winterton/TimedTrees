# Least Squares Dating 
## Setup 
You'll need to compile IQTree2 with a specific option to run this, follow the guide at http://www.iqtree.org/doc/Compilation-Guide
Importantly when running the `cmake` step, add the flag `-DUSE_LSD2=ON` to enable the library. 
## How to use
Navigate to the SuperSimPy output folder. SuperSimPy's pipeline has been made to work out of the box with this method, so all required data/formats are already there.
```
treetime --tree sim.substitutions.tree --dates full_metadata.csv --outdir timetree --name-column strain --date-column time --sequence-length 31101
 ```     