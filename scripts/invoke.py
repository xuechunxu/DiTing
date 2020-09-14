"""
Provides methods for invoking third-party programs
"""
import os
from scripts.logformatter import *


def megahit(reads1, reads2, threads, output):
    cmd_para = [
                'megahit',
                '-1', reads1,
                '-2', reads2,
                '-o', output,
                '-t', str(threads)
                ]
    cmd = ' '.join(cmd_para)
    try:
        logging.info('Metagenomic assembly by MEGAHIT started')
        logging.info(cmd)
        os.system(cmd)
    except:
        logging.exception("\nSomething went wrong when assembling metagenomic reads!")


def megahit_interleaved(reads, threads, output):
    cmd_para = [
        'megahit',
        '--12', reads,
        '-o', output,
        '-t', str(threads)
    ]
    cmd = ' '.join(cmd_para)
    try:
        logging.info('Metagenomic assembly by MEGAHIT started')
        logging.info(cmd)
        os.system(cmd)
    except:
        logging.exception("Something went wrong when assembling metagenomic reads!")


def metaspades(reads1, reads2, threads, output, mem):
    cmd_para = [
        'metaspades.py',
        '-1', reads1,
        '-2', reads2,
        '-o', output,
        '-t', str(threads),
        '-m', str(mem),
    ]
    cmd = ' '.join(cmd_para)
    try:
        logging.info('Metagenomic assembly by metaSPAdes started')
        logging.info(cmd)
        os.system(cmd)
    except:
        logging.exception("Something went wrong when assembling metagenomic reads!")


def metaspades_interleaved(reads, threads, output, mem):
    cmd_para = [
        'metaspades.py',
        '--12', reads,
        '-o', output,
        '-t', str(threads),
        '-m', str(mem),
    ]
    cmd = ' '.join(cmd_para)
    try:
        logging.info('Metagenomic assembly by metaSPAdes started')
        logging.info(cmd)
        os.system(cmd)
    except:
        logging.exception("Something went wrong when assembling metagenomic reads!")


def prodigal_meta(fasta, basename, outdir):
    cmd_para = [
                'prodigal', '-q',
                '-i', fasta,
                '-p', 'meta',
                '-a', os.path.join(outdir, basename + '.faa'),
                '-d', os.path.join(outdir, basename + '.ffn'),
                '-o', os.path.join(outdir, basename + '.gbk')
                ]
    cmd = ' '.join(cmd_para)
    try:
        logging.info('ORFs prediction by prodigal')
        logging.info(cmd)
        os.system(cmd)
    except:
        logging.exception("Something wrong with prodigal annotation!")


def bwa_index(assembly, output):
    cmd_para = [
                'bwa index',
                '-p', output,
                assembly
                ]
    cmd = ' '.join(cmd_para)
    try:
        logging.info(cmd)
        os.system(cmd)
    except:
        logging.exception("Something wrong with bwa index!")


def bwa_mem(index_file, reads1, reads2, output, threads):
    cmd_para = [
                'bwa mem',
                '-t', str(threads),
                '-v 2',  # only show warnings and errors
                index_file,
                reads1,
                reads2,
                '>', output
                ]
    cmd = ' '.join(cmd_para)
    try:
        logging.info(cmd)
        os.system(cmd)
    except:
        logging.exception("Something wrong with bwa_mem!")


def bwa_mem_interleaved(index_file, reads, output, threads):
    cmd_para = [
                'bwa mem -p',
                '-t', str(threads),
                '-v 2',  # only show warnings and errors
                index_file,
                reads,
                '>', output
                ]
    cmd = ' '.join(cmd_para)
    try:
        logging.info(cmd)
        os.system(cmd)
    except:
        logging.exception("Something wrong with bwa_mem!")


def pileup(sam, output):
    cmd_para = [
                'pileup.sh',
                'usejni=t',
                'in={}'.format(sam),
                'out={}'.format(output)
                ]
    cmd = ' '.join(cmd_para)
    try:
        logging.info(cmd)
        os.system(cmd)
    except:
        logging.exception("Something wrong with pileup.sh!")


def hmmsearch(paras):
    (threshold_method, threshold, outtype, output, hmm_db, faa) = paras
    cmd_para = [
        'hmmsearch',
        threshold_method, threshold,
        '--cpu', '1',
        '-o /dev/null',
        outtype, output,
        hmm_db,
        faa
        ]
    cmd = ' '.join(cmd_para)
    try:
        logging.debug(cmd)
        os.system(cmd)
    except:
        logging.exception("Something wrong with KEGG hmmsearch!")