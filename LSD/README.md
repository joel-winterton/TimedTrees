# Least Squares Dating 
## Setup 
You'll need to compile IQTree2 with a specific option to run this, follow the guide at http://www.iqtree.org/doc/Compilation-Guide
Importantly when running the `cmake` step, add the flag `-DUSE_LSD2=ON` to enable the library. 
## Data preparation 
## How to use
Enter the directory path of the SuperSimPy output data in `sim_data_path` in the `data_preparation.ipynb` notebook.
This will write a date file the output data directory, which is needed in this method.
Once you've installed IQTree properly and this date-file is written, navigate into the SuperSimPy output data directory and run: 

``iqtree2 -s sim.fasta --date datefile.txt -te newick_output_tree.nwk -m GTR+F --date-options "-a 0"``