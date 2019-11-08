"""
Define variables
"""

import os
import sys
from .args import *

READS_DIR = args.r  # directory for input fastq reads
OUT_DIR = args.o  # directory for output results
THREADS = args.n  # threads will be used
ASSEMBLY_TMP = os.path.join(OUT_DIR, 'megahit_tmp')  # directory for megahit temporary files
PRODIGAL_DIR = os.path.join(OUT_DIR, 'ORFs')  # directory for predicted ORFs
BBMAP_DIR = os.path.join(OUT_DIR, 'BBMap')  # directory for predicted ORFs
GENE_ABUN_DIR = os.path.join(OUT_DIR, 'Abundance')  # directory for gene relative abundance
KEGG_DIR = os.path.join(OUT_DIR, 'kegg_annotation')  # directory for KEGG annotations
ROOT_DIR = sys.path[0]
KODB_DIR = os.path.join(ROOT_DIR, 'kofam_database')  # downloaded kofam_database folder from KEGG website

BASENAMES = []  # input files basename list
READS_SUF = ''  # suffix of input reads
ASSEMBLY_SUF = 'fa'  # suffix of assemblies

if args.a:
    ASSEMBLY_DIR = args.a
else:
    ASSEMBLY_DIR = os.path.join(OUT_DIR, 'Assembly')  # directory for assembled contigs
