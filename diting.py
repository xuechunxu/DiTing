#! /usr/bin/env python3

from shutil import copy
from scripts import *
import sys

__author__ = "Xue Chunxu; Heyu Lin"
__contact__ = "xuechunxu@outlook.com; heyu.lin@student.unimelb.edu.au"
__version__ = "0.5"


def main():

    make_dir(OUT_DIR)

    """
    Check ko hmm database exists and has been unpacked
    """
    if check_kodb(KODB_DIR) is False:
        download_db(KODB_DIR)

    """
    Check assemblies / reads & Get input basename
    """
    if args.a:
        # If the corresponding assembly was provided, check if the corresponding reads can be found
        BASENAMES, READS_SUF, ASSEMBLY_SUF = check_reads_assembly(ASSEMBLY_DIR, READS_DIR)
    else:
        # If the corresponding assembly was NOT provided, check if the reads are in pairs
        BASENAMES, READS_SUF = check_reads(READS_DIR)

        """
        Megahit Assembly
        """
        make_dir(ASSEMBLY_DIR)
        for bn in BASENAMES:
            remove_dir(ASSEMBLY_TMP)  # make sure the output folder for Megahit does not exist
            reads1 = os.path.join(READS_DIR, bn) + '_1' + READS_SUF
            reads2 = os.path.join(READS_DIR, bn) + '_2' + READS_SUF
            megahit(reads1, reads2, THREADS, ASSEMBLY_TMP)  # Megahit will create the output folder automatically
            assembly_ori = os.path.join(ASSEMBLY_TMP, 'final.contigs.fa')
            assembly_tar = os.path.join(ASSEMBLY_DIR, bn + '.fa')
            copy(assembly_ori, assembly_tar)
        remove_dir(ASSEMBLY_TMP)  # clean up the Megahit temporary folder

    """
    Prodigal Prediction
    """
    make_dir(PRODIGAL_DIR)
    for bn in BASENAMES:
        fasta = os.path.join(ASSEMBLY_DIR, bn + '.fa')
        prodigal_meta(fasta, bn, PRODIGAL_DIR)

    """
    BBMap
    """
    bwa_index_dir = os.path.join(BBMAP_DIR, 'bwa_index')
    mapping_dir = os.path.join(BBMAP_DIR, 'mapping')
    pileup_dir = os.path.join(BBMAP_DIR, 'coverage')
    make_dir(BBMAP_DIR)
    make_dir(bwa_index_dir)
    make_dir(mapping_dir)
    make_dir(pileup_dir)

    for bn in BASENAMES:
        fasta = os.path.join(PRODIGAL_DIR, bn + '.ffn')
        index_file = os.path.join(bwa_index_dir, bn)
        reads1 = os.path.join(READS_DIR, bn + '_1' + READS_SUF)
        reads2 = os.path.join(READS_DIR, bn + '_2' + READS_SUF)
        sam = os.path.join(mapping_dir, bn + '.sam')
        pileup_out = os.path.join(pileup_dir, bn + '.pileup')

        bwa_index(fasta, index_file)  # build index for genes
        bwa_mem(index_file, reads1, reads2, sam, THREADS)  # map reads to genes
        pileup(sam, pileup_out)  # calculate coverage depths of every gene

        if not args.nc:  # the sam file will be removed as soon as it has been parsed due to it's large volume generally
            os.remove(sam)
    
    """
    Gene relative abundance
    """
    make_dir(GENE_ABUN_DIR)
    pileup_dir = os.path.join(BBMAP_DIR, 'coverage')
    for bn in BASENAMES:
        pileup_out = os.path.join(pileup_dir, bn + '.pileup')
        gene_relative_abun(pileup_out, bn, GENE_ABUN_DIR)

    """
    Resolve ko_list file into dictionary
    """
    ko_list = os.path.join(KODB_DIR, 'ko_list')
    ko_dic = ko_list_parser(ko_list)

    """
    KEGG annotation by hmmsearch
    """
    make_dir(KEGG_DIR)
    kegg_pieces_dir = os.path.join(KEGG_DIR, 'hmmout')  # containing KEGG annotations of every knum
    make_dir(kegg_pieces_dir)
    for bn in BASENAMES:
        faa = os.path.join(PRODIGAL_DIR, bn + '.faa')
        kegg_annotation(faa, bn, kegg_pieces_dir, KODB_DIR, ko_dic, THREADS)

    """
    Merge KEGG annotations
    """
    ko_merged_tab = os.path.join(KEGG_DIR, 'ko_merged.txt')
    merge_ko(kegg_pieces_dir, ko_merged_tab)

    """
    Merge KEGG annotations and gene relative abundances
    """
    ko_abun_merged_tab = os.path.join(KEGG_DIR, 'ko_abun.txt')
    merge_abun_ko(GENE_ABUN_DIR, ko_merged_tab, ko_abun_merged_tab)

    """
    Relative abundance of pathways
    """
    final_output = os.path.join(OUT_DIR, 'pathways_relative_abundance.tab')
    pathway_parser(ko_abun_merged_tab, final_output)

    """
    transpose pathway_relative abundance.tab
    """
    table = os.path.join(OUT_DIR, 'pathways_relative_abundance.tab')
    transposition(table)
    cmd_rm_path = 'rm ' + table
    os.system(cmd_rm_path)
    cmd_mv_path = 'mv ' + table + '.transposition pathways_relative_abundance.tab'
    os.system(cmd_mv_path)

    """
    Diagrammatic drawing
    """
    self_script_pathway = sys.path[0]
    diagrammatic_drawing = os.path.join(self_script_pathway, 'accessory-scripts/diagrammatic_drawing.py')
    cmd_para = [
                'python',
                diagrammatic_drawing,
                '-t',
                'pathways_relative_abundance.tab'
                ]
    cmd = ' '.join(cmd_para)
    os.system(cmd)
    os.system('rm -rf Figure_tmp')
    cmd_mv = 'mv *.png ' + OUT_DIR
    os.system(cmd_mv)
    cmd_mv = 'mv pathways_relative_abundance.tab ' + OUT_DIR
    os.system(cmd_mv)


if __name__ == '__main__':
    main()
