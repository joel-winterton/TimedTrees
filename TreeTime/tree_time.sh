#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate conda_vgsim
cd /home/joel/EBI/SimulationsData/0.5mil/V1
treetime --tree sim.substitutions.tree --dates full_metadata.csv --outdir timetree --name-column strain --date-column time --sequence-length=31101 --keeproot
