"""
Provides methods for invoking third-party programs
"""
import os


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
        print("\n" + 'Metagenomic Assembly'.center(50, '*'))
        print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething went wrong when assembling metagenomic reads!")


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
        print("\n" + 'ORFs prediction'.center(50, '*'))
        print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething wrong with prodigal annotation!")


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
        print("\nSomething wrong with bwa index!")


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
        print("\n" + 'bwa mem'.center(50, '*'))
        print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething wrong with bwa_mem!")


def pileup(sam, output):
    cmd_para = [
                'pileup.sh',
                'usejni=t',
                'in={}'.format(sam),
                'out={}'.format(output)
                ]
    cmd = ' '.join(cmd_para)
    try:
        print("\n" + 'Calculate coverage depths - pileup'.center(50, '*'))
        print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething wrong with pileup.sh!")


def hmmsearch(paras):
    (threshold_method, threshold, output, hmm_db, faa) = paras
    cmd_para = [
        'hmmsearch',
        threshold_method, threshold,
        '--cpu', '1',
        '--tblout', output,
        hmm_db,
        faa
    ]
    cmd = ' '.join(cmd_para)
    try:
        # print(cmd + '\n')
        os.system(cmd)
    except:
        print("\nSomething wrong with KEGG hmmsearch!")