#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse
import seaborn as sns
import pandas as pd

__author__ = "Xue Chunxu; Heyu Lin"
__contact__ = "xuechunxu@outlook.com; heyu.lin@student.unimelb.edu.au"
__version__ = "0.5"

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--table', metavar='input_abundance_pathways_table', dest='t',
                    type=str, required=True,
                    help='a table containing relative abundance of pathways to be used as input')
args = parser.parse_args()

abundance_table = args.t

file_in = open(abundance_table, "r")
table = pd.read_table(file_in, index_col=False)
flatui = ["blue", "white", "red"]
cmap = sns.palplot(sns.color_palette(flatui))
ax = sns.heatmap(table, cmap=cmap)
fig = ax.get_figure()
fig.savefig("function_heatmap.svg")
