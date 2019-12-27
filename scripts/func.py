"""
Provides in-house functions
"""

import os
import sys
import re
import urllib.request
import shutil
import gzip
import tarfile
from multiprocessing import Pool
from .invoke import hmmsearch
from .pathway import *


def download_db(ko_db):
    print("\n" + 'Download database'.center(50, '*'))
    url_ko_list = 'ftp://ftp.genome.jp/pub/db/kofam/ko_list.gz'
    url_profiles = 'ftp://ftp.genome.jp/pub/db/kofam/profiles.tar.gz'
    path_ko_list_gz = os.path.join(ko_db, 'ko_list.gz')
    path_ko_list = os.path.join(ko_db, 'ko_list')
    path_profiles_tar_gz = os.path.join(ko_db, 'profiles.tar.gz')
    if not os.path.exists(ko_db):
        os.mkdir(ko_db)

    #  download
    print("Downloading started... Please wait. This may take a while.")
    with urllib.request.urlopen(url_ko_list) as response, open(path_ko_list_gz, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    with urllib.request.urlopen(url_profiles) as response, open(path_profiles_tar_gz, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    #  decompress
    with gzip.open(path_ko_list, 'rb') as f_in, open(path_ko_list_gz, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    tar = tarfile.open(path_profiles_tar_gz)
    tar.extractall()
    tar.close()
    print('Database has been downloaded and deployed successfully at {}'. format(ko_db))


def gene_relative_abun(pileup_file, basename, out_dir):
    """
    Calculate relative abundance of genes in a file generated by BBMap pileup

    :param pileup_file: coverage depths of genes generated by BBMap pileup
    :param basename: basename of a sample that will be calculated
    :param out_dir: output directory
    :return: None
    """
    print("\n" + 'Gene relative abundance'.center(50, '*'))
    total_ave_fold = float(0)
    file_out = os.path.join(out_dir, basename + '.abundance')
    with open(file_out, 'a') as fo:
        fo.write("#ID\tgene_abundance\n")
    with open(pileup_file) as fi:
        for line in fi:
            if line.startswith('#ID'):
                continue
            else:
                ave_fold = line.split('\t')[1]
                total_ave_fold += float(ave_fold)
    with open(pileup_file) as fi:
        for line in fi:
            if line.startswith('#ID'):
                continue
            else:
                gene_id = line.split('\t')[0]
                ave_fold = line.split('\t')[1]
                gene_abund = float(ave_fold) / float(total_ave_fold)
                with open(file_out, 'a') as fo:
                    fo.write(gene_id + "\t" + str(gene_abund) + "\n")


def ko_list_parser(ko_list):
    """
    parse ko_list file into a dict object

    :param ko_list: path of the file ko_list
    :return: a dictionary mapping knum to threshold and score_type
    :rtype: dict
    """
    ko_dic = {}  # { knum : [threshold, score_type] }
    with open(ko_list) as fi:
        next(fi)  # skip the first line (header)
        for line in fi:
            knum, threshold, score_type = line.split('\t')[0:3]
            ko_dic[knum] = [threshold, score_type]
    return ko_dic


def kegg_annotation(faa, basename, out_dir, db_dir, ko_dic, threads):
    print("\n" + 'KEGG annotation for {}'.format(basename).center(50, '*'))
    paras = []  # Build a parameter list for multiprocessing

    for knum, info in ko_dic.items():
        output = os.path.join(out_dir, knum + '.' + str(basename) + '.hmmout')
        hmm_db = os.path.join(db_dir, 'profiles', knum + '.hmm')
        if info[1] == 'full':
            threshold_method = '-T'
            outtype = '--tblout'
        elif info[1] == 'domain':
            threshold_method = '--domT'
            outtype = '--domtblout'
        else:
            threshold_method = '-E'
            info[0] = '1e-5'
            outtype = '--tblout'
        paras.append((threshold_method, info[0], outtype, output, hmm_db, faa))

    process = Pool(threads)
    process.map(hmmsearch, paras)


# merge kegg annotations into one file
def merge_ko(hmmout_dir, output):
    print("\n" + 'merge KEGG annotations'.center(50, '*'))
    #ko_merged_dict = {}  # { basename + gene_id : abundance }
    with open(output, 'w') as fo:
        fo.write('#sample\tgene_id\tk_number\n')
    for hmmout_file in os.listdir(hmmout_dir):  # K00039.sample1.hmmout
        if hmmout_file.endswith('.hmmout'):
            kobasename = hmmout_file.rsplit('.', 1)[0]  # K00039.sample1
            basename = kobasename.split('.', 1)[1]  # sample1
            hmmout_file_path = os.path.join(hmmout_dir, hmmout_file)
            with open(hmmout_file_path, 'r') as fi:
                for line in fi:
                    if not line.startswith('#'):
                        gene_id, accession = line.split()[0:2]
                        lines = line.split()
                        for i in lines:
                            if re.match(r'K\d\d\d\d\d', i):
                                k_number = i
                            #key = str(basename) + '+' + str(gene_id)
                            #ko_merged_dict[key] = k_number
                                with open(output, 'a') as fo:
                                    fo.write(basename + '\t' + gene_id + '\t' + k_number + '\n')
    #return ko_merged_dict


# merge gene relative abundance table with gene kegg annotation table
def merge_abun_ko(abun_table_dir, ko_merged_tab, output):
    print("\n" + 'merge abundance table with kegg table'.center(50, '*'))
    with open(output, 'w') as fo:
        fo.write('#sample\tk_number\trelative_abundance\tgene_id\n')
    abun_tab_dict = {}
    for abun in os.listdir(abun_table_dir):
        if abun.endswith('.abundance'):
            basename = abun.rsplit('.', 1)[0]
            abun_path = os.path.join(abun_table_dir, abun)
            with open(abun_path) as fi:
                next(fi)
                for line in fi:
                    line = line.strip('\n')
                    gene_id, abundance = line.split('\t')
                    key = str(basename) + '+' + str(gene_id)
                    abun_tab_dict[key] = abundance
    a = []
    with open(ko_merged_tab, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            else:
                a.append(line.strip())
    for item in sorted(a):
        basename = item.split('\t')[0]
        gene_id = item.split('\t')[1]
        k_number = item.split('\t')[2]
        key = basename + '+' + gene_id
        abundance = abun_tab_dict[key]
        with open(output, 'a') as fo:
            fo.write(basename + '\t' + k_number + '\t' + abundance + '\t' + gene_id + '\n')


def kegg_decoder(input_tab, output):
    print("\n" + 'kegg decoder'.center(50, '*'))
    self_script_pathway = sys.path[0]
    kegg_decoder_meta_py = os.path.join(self_script_pathway, 'accessory-scripts', 'KEGG-decoder_meta.py')
    cmd_para = [
                'python',
                kegg_decoder_meta_py,
                input_tab,
                output
                ]
    cmd = ' '.join(cmd_para)
    os.system(cmd)


def pathway_parser(in_tab, output):
    relative_abundance = {}
    genome_data = []
    for line in open(in_tab, "r"):
        # print(line)
        line = line.rstrip()
        info = line.split()
        if line.startswith('#'):
            continue
        else:
            line_key = info[0]+'_'+info[1]
            if line_key in relative_abundance:
                relative_abundance[line_key] += float(info[2])
            else:
                relative_abundance[line_key] = float(info[2])
            genome_data.append(info[0])
    genome_data2 = {}.fromkeys(genome_data).keys()
    genome_data = genome_data2

    # for key, value in relative_abundance.items():
    #     print("\nKey: " + key)
    #     print("\nValue: " + str(value))

    out_file = open(output, "w")
    out_file.write('#Pathway'+"\t"+str("\t".join(function_order))+"\n")

    for k in genome_data:
        # print(k)
        # print(reverse_tca(relative_abundance, k))
        pathway_abundant = Pathway(relative_abundance, k)
        pathway_data = pathway_abundant.solve_pathway()

        # print k, pathway_data
        out_string = str(k)+"\t"
        out_list = [k]
        for i in function_order:
            out_list.append(pathway_data[i])
            out_string = str(out_list).strip('[]')
        tab_string = ""
        for line2 in out_string:
            if line2 == "\'":
                continue
            if line2 == ",":
                tab_string = tab_string + "\t"
            else:
                tab_string = tab_string + line2
        out_file.write(tab_string+"\n")
    out_file.close()

