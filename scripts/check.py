"""
Check data integrity
"""
import os


def check_kodb(ko_db):
    ko_list_path = os.path.join(ko_db, 'ko_list')
    profiles_path = os.path.join(ko_db, 'profiles')
    hmm_path = os.path.join(profiles_path, 'K00001.hmm')
    db_files = [ko_db, ko_list_path, profiles_path, hmm_path]
    for fl in db_files:
        if not os.path.exists(fl):
            return False


def check_reads_assembly(assembly_dir, reads_dir):
    """
    Check if the assembly provided can match corresponding reads pairs

    :param str assembly_dir: directory containing metagenomic assemblies in fasta format
    :param str reads_dir: directory containing metagenomic paired-end reads
    :return: basenames of input files, suffix of the reads, suffix of the assembly
    :rtype: tuple
    :raises FileNotFoundError: if the corresponding reads pairs cannot be found or are not complete

    """
    basenames = []
    reads_suf = ''
    assembly_suf = ''

    for fa in os.listdir(assembly_dir):
        basename, assembly_suf = fa.rsplit('.', 1)
        basenames.append(basename)

        reads_dir_basename = os.path.join(reads_dir, basename)

        if os.path.exists(reads_dir_basename + '_1.fq') and os.path.exists(reads_dir_basename + '_2.fq'):
            reads_suf = '.fq'
        elif os.path.exists(reads_dir_basename + '_1.fastq') and os.path.exists(reads_dir_basename + '_2.fastq'):
            reads_suf = '.fastq'
        elif os.path.exists(reads_dir_basename + '_1.fq.gz') and os.path.exists(reads_dir_basename + '_2.fq.gz'):
            reads_suf = '.fq.gz'
        elif os.path.exists(reads_dir_basename + '_1.fastq.gz') and os.path.exists(reads_dir_basename + '_2.fastq.gz'):
            reads_suf = '.fastq.gz'
        else:
            raise FileNotFoundError('Failed to find the corresponding paired-end reads to {}'.format(fa))

    return basenames, reads_suf, assembly_suf


def check_reads(reads_dir):
    """
    Check if the assembly provided can match corresponding reads pairs

    :param str reads_dir: directory containing metagenomic paired-end reads
    :return: basenames of input files, suffix of the reads
    :rtype: tuple
    :raises FileNotFoundError: if the reads provided in the input directory are not in pairs

    """
    basenames = []
    reads_suf = ''

    for read in os.listdir(reads_dir):
        if read.endswith('_1.fq'):
            basename = read.rsplit('_', 1)[0]
            basenames.append(basename)
            reads_suf = '.fq'
            if not os.path.exists(os.path.join(reads_dir, basename) + '_2.fq'):
                raise FileNotFoundError('Failed to find the corresponding reverse reads to {}'.format(read))
        elif read.endswith('_1.fastq'):
            basename = read.rsplit('_', 1)[0]
            basenames.append(basename)
            reads_suf = '.fastq'
            if not os.path.exists(os.path.join(reads_dir, basename) + '_2.fastq'):
                raise FileNotFoundError('Failed to find the corresponding reverse reads to {}'.format(read))
        elif read.endswith('_1.fastq.gz'):
            basename = read.rsplit('_', 1)[0]
            basenames.append(basename)
            reads_suf = '.fastq.gz'
            if not os.path.exists(os.path.join(reads_dir, basename) + '_2.fastq.gz'):
                raise FileNotFoundError('Failed to find the corresponding reverse reads to {}'.format(read))
        elif read.endswith('_1.fq.gz'):
            basename = read.rsplit('_', 1)[0]
            basenames.append(basename)
            reads_suf = '.fq.gz'
            if not os.path.exists(os.path.join(reads_dir, basename) + '_2.fq.gz'):
                raise FileNotFoundError('Failed to find the corresponding reverse reads to {}'.format(read))

    return basenames, reads_suf


# def check_kodb(KODB_DIR):
