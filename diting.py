#! /usr/bin/python3

import os
import sys
import argparse
import fnmatch
import re
from collections import defaultdict

__author__ = "Xue chunxu; Heyu Lin"
__contact__ = "xuechunxu@outlook.com; heyu.lin@student.unimelb.edu.au"

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--reads', metavar='input_reads', dest='r',
                    type=str, required=True,
                    help='A folder containing Reads to be used as input')
args = parser.parse_args()


def reads_assembly(reads1, reads2, output):
    cmd_para = [
                'megahit',
                '-1', reads1,
                '-2', reads2,
                '-o', output,
                '-t', '20'
                ]
    cmd = ' '.join(cmd_para)
    try:
        print("\n" + 'Assembly metagenome'.center(50, '*'))
        print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething wrong with assembly metagenome reads!")


def prokka_meta(fasta, prefix, outdir):
    cmd_para = [
                'prokka', fasta,
                '--prefix', prefix,
                '--outdir', outdir,
                '--metagenome'
                ]
    cmd = ' '.join(cmd_para)
    try:
        print("\n" + 'Prokka assembly contig'.center(50, '*'))
        print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething wrong with prokka annotation for assembly contig!")


def bwa_index(assembly, output):
    cmd_para = [
                'bwa index',
                '-p', output,
                assembly
                ]
    cmd = ' '.join(cmd_para)
    try:
        print("\n" + 'bwa index'.center(50, '*'))
        print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething wrong with bwa_index!")
    

def bwa_mem(index_file, reads1, reads2, output):
    cmd_para = [
                'bwa mem',
                '-t',
                '1', index_file,
                reads1,
                reads2,
                '>', output
                ]
    cmd = ' '.join(cmd_para)
    try:
        print("\n" + 'bwa mem'.center(50, '*'))
        print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething wrong with bwa_mem!")


def pileup(sam, output):
    cmd_para = [
                'pileup.sh ',
                'in=', sam,
                ' out=', output
                ]
    cmd = ''.join(cmd_para)
    try:
        print("\n" + 'pileup'.center(50, '*'))
        print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething wrong with pileup.sh!")


def gene_abundance(pileup_dir):
    print("\n" + 'Gene relative abundance'.center(50, '*'))
    os.mkdir('GENE_RELATIVE_ABUNDANCCE')
    for read in os.listdir(pileup_dir):
        if fnmatch.fnmatch(read, '*.pileup.out'):
            total_ave_fold = float(0)
            read_head = read.split('.pileup.out')[0]
            file_out = 'GENE_RELATIVE_ABUNDANCCE/' + read_head + '.gene_abundance.out'
            pileup_file = pileup_dir + read
            with open(file_out, 'a') as outfile_object:
                outfile_object.write("#ID\tgene_abundance\n")
            with open(pileup_file) as file_object:
                for line in file_object:
                    if line.startswith('#ID'):
                        continue
                    else:
                        ave_fold = line.split('\t')[1]
                        total_ave_fold += float(ave_fold)
            with open(pileup_file) as file_object:
                for line in file_object:
                    if line.startswith('#ID'):
                        continue
                    else:
                        gene_id = line.split('\t')[0]
                        ave_fold = line.split('\t')[1]
                        gene_abundance = float(ave_fold)/float(total_ave_fold)
                        with open(file_out, 'a') as outfile_object:
                            outfile_object.write(gene_id + "\t" + str(gene_abundance) + "\n")


def kegg_annotation(prokka_faa):
    os.mkdir('Tmp/KEGG')
    self_script_pathway = sys.path[0]
    ko_list = self_script_pathway + '/kofam_database/ko_list'
    knum2threshold = {}
    knum2score_type = {}
    knums = []
    with open(ko_list) as ko_list_object:
        for line in ko_list_object:
            if line.startswith('knum'):
                continue
            else:
                knum = line.split('\t')[0]
                threshold = line.split('\t')[1]
                score_type = line.split('\t')[2]
                knums.append(knum)
                knum2threshold[knum] = threshold
                knum2score_type[knum] = score_type
    for read in os.listdir(prokka_faa):
        if fnmatch.fnmatch(read, '*.faa'):
            read_head = read.split('.faa')[0]
            faa_file = prokka_faa + '/' + read
            for knum1 in knums:
                output = 'Tmp/KEGG/' + knum1 + '.' + read_head + '.hmmsearch_result.txt'
                hmm_db = self_script_pathway + '/kofam_database/profiles/' + knum1 + '.hmm'
                if knum2score_type[knum1] == 'full':
                    cmd_para = [
                                'hmmsearch',
                                '-T', knum2threshold[knum1],
                                '--cpu', '1',
                                '--tblout', output,
                                hmm_db,
                                faa_file
                                ]
                    cmd = ' '.join(cmd_para)
                    try:
                        print("\n" + 'KEGG annotation'.center(50, '*'))
                        print(cmd + '\n')
                        os.system(cmd)
                    except:
                        print("\nSomething wrong with KEGG hmmsearch!")
                elif knum2score_type[knum1] == 'domain':
                    cmd_para = [
                                'hmmsearch',
                                '-domT', knum2threshold[knum1],
                                '--cpu', '1',
                                '--tblout', output,
                                hmm_db,
                                faa_file
                                ]
                    cmd = ' '.join(cmd_para)
                    try:
                        print("\n" + 'KEGG annotation'.center(50, '*'))
                        print(cmd + '\n')
                        os.system(cmd)
                    except:
                        print("\nSomething wrong with KEGG hmmsearch!")


#merge each single kegg annotation into one file
def selected_ko(input_dir):
    print("\n" + 'merge each single kegg annotation into one file'.center(50, '*'))
    os.mkdir('KEGG_ANNO')
    with open('KEGG_ANNO/kegg_anno_result', 'a') as outfile_object:
        outfile_object.write('#sample\tgene_id\tk_number\n')
    for read in os.listdir(input_dir):
        if fnmatch.fnmatch(read, '*.final.contigs.hmmsearch_result.txt'):
            sample_name1 = read.split('.final.contigs.hmmsearch_result.txt')[0]
            sample_name = re.split(r'K\d\d\d\d\d\.', sample_name1)[1]
            input_read = input_dir + read
            with open(input_read) as ko_object:
                for line in ko_object:
                    if line.startswith('#'):
                        continue
                    else:
                        gene_id = line.split(' ')[0]
                        k_numbers = re.findall(r'K\d\d\d\d\d', line)
                        k_number = k_numbers[0]
                        with open('KEGG_ANNO/kegg_anno_result', 'a') as outfile_object:
                            outfile_object.write(sample_name + '\t' + gene_id + '\t' + k_number + '\n')


#merge gene relative abundance table with gene kegg annotation table
def mer_abun_ko(abun_table_dir, kegg_table):
    print("\n" + 'merge abundance table with kegg table'.center(50, '*'))
    with open('KEGG_ANNO/sample_kegg_abundance_result', 'a') as outfile_object:
        outfile_object.write('#sample\tk_number\trelative_abundance\tgene_id\n')
    abun_table = {}
    kegg_table1 = {}
    for read in os.listdir(abun_table_dir):
        if fnmatch.fnmatch(read, '*.gene_abundance.out'):
            sample_name = read.split('.gene_abundance.out')[0]
            input_read = abun_table_dir + read
            with open(input_read) as abun_object:
                for line in abun_object:
                    line = line.strip('\n')
                    if line.startswith('#'):
                        continue
                    else:
                        gene_id = line.split('\t')[0]
                        abundance = line.split('\t')[1]
                        key = sample_name + '+' + gene_id
                        abun_table[key] = abundance

    with open(kegg_table) as kegg_table_object:
        for line in kegg_table_object:
            line = line.strip('\n')
            if line.startswith('#'):
                continue
            else:
                sample_name = line.split('\t')[0]
                gene_id = line.split('\t')[1]
                k_number = line.split('\t')[2]
                key = sample_name + '+' + gene_id
                kegg_table1[key] = k_number

    for key in sorted(kegg_table1.keys()):
        sample = key.split('+')[0]
        k_number = kegg_table1[key]
        abundance = abun_table[key]
        gene_id = key.split('+')[1]
        with open('KEGG_ANNO/sample_kegg_abundance_result', 'a') as outfile_object:
            outfile_object.write(sample + '\t' + k_number + '\t' + abundance + '\t' + gene_id + '\n')


#accessory-scripts/KEGG-decoder_meta.py
def kegg_decoder(input_tab, output):
    print("\n" + 'kegg decoder'.center(50, '*'))
    os.mkdir('Final_result')
    self_script_pathway = sys.path[0]
    kegg_decoder_meta_py = self_script_pathway + '/accessory-scripts/KEGG-decoder_meta.py'
    cmd_para = [
                'python3',
                kegg_decoder_meta_py,
                input_tab,
                output
                ]
    cmd = ' '.join(cmd_para)
    os.system(cmd)


def main():
    path = args.r
    os.mkdir('Tmp')
    
    #ASSEMBLY
    os.mkdir('ASSEMBLY')
    for read in os.listdir(path):
        if fnmatch.fnmatch(read, '*_1.fastq'):
            read_head = read.split('_1.fastq')[0]
            reads1 = path + '/' + read_head + '_1.fastq'
            reads2 = path + '/' + read_head + '_2.fastq'
            output = 'Tmp/' + read_head + '_megahit.out'
            reads_assembly(reads1, reads2, output)
            cmd = 'cp' + ' ' + output + '/final.contigs.fa' + ' ' + 'ASSEMBLY/' + read_head + '.final.contigs.fa'
            os.system(cmd)
    
    #Prokka annotation
    os.mkdir('PROKKA_ffn_faa')
    for read in os.listdir('ASSEMBLY'):
        if fnmatch.fnmatch(read, '*.fa'):
            read_head = read.split('.fa')[0]
            fasta = 'ASSEMBLY/' + read
            prefix = read_head
            outdir = 'Tmp/' + read_head + '.prokka.out'
            prokka_meta(fasta, prefix, outdir)
            cmd = 'cp' + ' ' + outdir + '/*.ffn' + ' ' + 'PROKKA_ffn_faa/'
            os.system(cmd)
            cmd1 = 'cp' + ' ' + outdir + '/*.faa' + ' ' + 'PROKKA_ffn_faa/'
            os.system(cmd1)
    
    #bbmap
    os.mkdir('Tmp/bbmap')
    
    #bwa_index
    os.mkdir('Tmp/bbmap/bwa_index.out')
    for read in os.listdir('PROKKA_ffn_faa'):
        if fnmatch.fnmatch(read, '*.ffn'):
            read_head = read.split('.ffn')[0]
            assembly = 'PROKKA_ffn_faa/' + read
            output = 'Tmp/bbmap/bwa_index.out/' + read_head
            bwa_index(assembly, output)

    #bwa_mem
    os.mkdir('Tmp/bbmap/bwa_mem.out')
    for read in os.listdir(path):
        if fnmatch.fnmatch(read, '*_1.fastq'):
            read_head = read.split('_1.fastq')[0]
            index_file = 'Tmp/bbmap/bwa_index.out/' + read_head + '.final.contigs'
            reads1 = path + '/' + read_head + '_1.fastq'
            reads2 = path + '/' + read_head + '_2.fastq'
            output = 'Tmp/bbmap/bwa_mem.out/' + read_head + '.sam'
            bwa_mem(index_file, reads1, reads2, output)

    #pileup.sh
    os.mkdir('Tmp/bbmap/pileup.out')
    for read in os.listdir('Tmp/bbmap/bwa_mem.out/'):
        if fnmatch.fnmatch(read, '*.sam'):
            sam = 'Tmp/bbmap/bwa_mem.out/' + read
            read_head = read.split('.sam')[0]
            output = 'Tmp/bbmap/pileup.out/' + read_head + '.pileup.out'
            pileup(sam, output)
            os.remove(sam)

    #gene_abundance
    pileup_dir = 'Tmp/bbmap/pileup.out/'
    gene_abundance(pileup_dir)

    #KEGG_annotation
    prokka_faa = 'PROKKA_ffn_faa'
    kegg_annotation(prokka_faa)

    #merge each single kegg annotation into one file
    input_dir = 'Tmp/KEGG/'
    selected_ko(input_dir)

    #merge gene relative abundance table with gene kegg annotation table
    abun_table_dir = 'GENE_RELATIVE_ABUNDANCCE/'
    kegg_table = 'KEGG_ANNO/kegg_anno_result'
    mer_abun_ko(abun_table_dir, kegg_table)

    #accessory-scripts/KEGG-decoder_meta.py
    input_tab = 'KEGG_ANNO/sample_kegg_abundance_result'
    output = 'Final_result/Pathways_relative_abundance_each_sample.tab'
    kegg_decoder(input_tab, output)

if __name__ == '__main__':
    main()
