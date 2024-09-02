"""
ENTRYPOINT.
This script accepts dataset paths and outputs benchmarks.
Currently implemented:
1. TreeTime
"""

import pandas as pd
import argparse

parser = argparse.ArgumentParser(
    prog='Time tree estimation benchmarker',
    description="Collates estimation data and outputs benchmarks for each time tree estimation algorithm.")
parser.add_argument('-r', '--real')
parser.add_argument('-t', '--timetree')
parser.add_argument('-o', '--output')

args = vars(parser.parse_args())
