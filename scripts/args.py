"""
Parse arguments
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--reads', metavar='input_reads', dest='r',
                    type=str, required=False,
                    help='folder containing reads to be used as input')
parser.add_argument('-o', '--outdir', metavar='output_dir', dest='o',
                    type=str, required=False,
                    help='output directory')
parser.add_argument('-a', '--assembly', metavar='metagenomic_assembly', dest='a',
                    type=str,
                    help='folder containing metagenomic assemblies corresponding to provided reads, \
                    which should have the same base name as the reads')
parser.add_argument('-n', '--threads', metavar='threads', dest='n',
                    type=int, default=4,
                    help='threads that will be used')
parser.add_argument('--noclean', metavar='no_cleaning', dest='nc',
                    nargs="?", const=True, default=False,
                    help='The sam files would be retained if this flag was used')
parser.add_argument('-vis', '--visualization', metavar='pathways_relative_abundance.tab', dest='vis', \
                    type=str, default=False,
                    help='A table for visualization, note that the name of pathways must be the same \
                    as that in the final table this software pruduced.')

args = parser.parse_args()

