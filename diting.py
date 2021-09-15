#! /usr/bin/env python3
    
from shutil import copy
from scripts import *
    
__author__ = "Xue Chunxu; Heyu Lin"
__contact__ = "xuechunxu@outlook.com; heyu.lin@student.unimelb.edu.au"
__version__ = "0.7"
    
    
def main():
    if args.vis:
        sketch(ABUNDANCE_TABLE)
        os.system('rm -rf Figure_tmp')
        heatmap(ABUNDANCE_TABLE)
        os.system('rm -rf heatmap_tmp')
    else:
        make_dir(OUT_DIR)

        """
        Setting logging
        """
        # Using FileHandler writing log to file
        logfile = os.path.join(OUT_DIR, 'log.txt')
        fh = logging.FileHandler(logfile)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)

        # Using StreamHandler writing to console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        # Add the two Handlers
        logger.addHandler(ch)
        logger.addHandler(fh)


        logging.info('User input: {}'.format(' '.join(sys.argv)))
        
        
        """
        [1/12] Check if ko hmm database exists and has been unpacked
        """
        logging.info('[1/12] Check database'.center(50, '*'))
        if check_kodb(KODB_DIR) is False:
            logging.info("No KEGG database was detected. Downloading is starting automatically.")
            cmd_rm_ko_database = 'rm -rf ' + KODB_DIR
            logging.info(cmd_rm_ko_database)
            os.system(cmd_rm_ko_database)
            download_db(KODB_DIR)
            DMSP_db_parse(DMSP_DIR, KODB_DIR)
        else:
            logging.info("The KEGG database is set")

        if check_DMSP_db(KODB_DIR) is False:
            logging.info("The DMSP database is not parsed yet")
            DMSP_db_parse(DMSP_DIR, KODB_DIR)
        else:
            logging.info("The DMSP database is set")

        """
        Check assemblies / reads & Get input basename
        """
        # Check reads
        BASENAMES, READS_SUF, READS_INTER = check_reads(READS_DIR)

        # Check assembly
        if args.a:
            # If the corresponding assembly was provided, check if the corresponding reads can be found
            ASSEMBLY_SUF = check_reads_assembly(ASSEMBLY_DIR, BASENAMES)
        else:
            """
            [2/12] Assembly
            """
            logging.info('[2/12] Metagenomic assembly'.center(50, '*'))
            make_dir(ASSEMBLY_DIR)
            for bn in BASENAMES:
                remove_dir(ASSEMBLY_TMP)  # make sure the output folder for Megahit does not exist
                if READS_INTER:
                    """
                    if interleaved reads
                    """
                    reads_interleaved = os.path.join(READS_DIR, bn) + READS_SUF
                    if args.spades:
                        logging.info("metaSPAdes Assembly for {}".format(bn))
                        metaspades_interleaved(reads_interleaved, THREADS, ASSEMBLY_TMP, MEM)
                        assembly_ori = os.path.join(ASSEMBLY_TMP, 'contigs.fasta')
                    else:
                        logging.info("Megahit Assembly for {}".format(bn))
                        megahit_interleaved(reads_interleaved, THREADS, ASSEMBLY_TMP)  # Megahit will create the output folder automatically
                        assembly_ori = os.path.join(ASSEMBLY_TMP, 'final.contigs.fa')
                else:
                    """
                    if paired-end reads are in two separate files
                    """
                    reads1 = os.path.join(READS_DIR, bn) + '_1' + READS_SUF
                    reads2 = os.path.join(READS_DIR, bn) + '_2' + READS_SUF
                    if args.spades:

                        logging.info("metaSPAdes Assembly for {}".format(bn))
                        metaspades(reads1, reads2, THREADS, ASSEMBLY_TMP, MEM)
                        assembly_ori = os.path.join(ASSEMBLY_TMP, 'contigs.fasta')
                    else:
                        logging.info("Megahit Assembly for {}".format(bn))
                        megahit(reads1, reads2, THREADS, ASSEMBLY_TMP)  # Megahit will create the output folder automatically
                        assembly_ori = os.path.join(ASSEMBLY_TMP, 'final.contigs.fa')
                assembly_tar = os.path.join(ASSEMBLY_DIR, bn + '.fa')
                copy(assembly_ori, assembly_tar)
            remove_dir(ASSEMBLY_TMP)  # clean up the temporary folder
    
        """
        [3/12] Prodigal Prediction
        """
        logging.info('[3/12] ORFs prediction'.center(50, '*'))
        make_dir(PRODIGAL_DIR)
        for bn in BASENAMES:
            logging.info("Prediction ORFs for {}".format(bn))
            fasta = os.path.join(ASSEMBLY_DIR, bn + '.fa')
            prodigal_meta(fasta, bn, PRODIGAL_DIR)
    
        """
        [4/12] bwa & BBMap
        """
        logging.info('[4/12] Reads recruitment'.center(50, '*'))
        bwa_index_dir = os.path.join(BBMAP_DIR, 'bwa_index')
        mapping_dir = os.path.join(BBMAP_DIR, 'mapping')
        pileup_dir = os.path.join(BBMAP_DIR, 'coverage')
        make_dir(BBMAP_DIR)
        make_dir(bwa_index_dir)
        make_dir(mapping_dir)
        make_dir(pileup_dir)
    
        for bn in BASENAMES:
            logging.info("Mapping reads to {} by bwa mem".format(bn))
            fasta = os.path.join(PRODIGAL_DIR, bn + '.ffn')
            index_file = os.path.join(bwa_index_dir, bn)

            sam = os.path.join(mapping_dir, bn + '.sam')
            pileup_out = os.path.join(pileup_dir, bn + '.pileup')
    
            bwa_index(fasta, index_file)  # build index for genes
            if READS_INTER:
                reads_interleaved = os.path.join(READS_DIR, bn) + READS_SUF
                bwa_mem_interleaved(index_file, reads_interleaved, sam, THREADS)  # map reads to genes
            else:
                reads1 = os.path.join(READS_DIR, bn + '_1' + READS_SUF)
                reads2 = os.path.join(READS_DIR, bn + '_2' + READS_SUF)
                bwa_mem(index_file, reads1, reads2, sam, THREADS)  # map reads to genes

            logging.info("Calculate gene abundance for {} by BBMap pileup".format(bn))
            pileup(sam, pileup_out)  # calculate coverage depths of every gene
    
            if not args.nc:  # the sam file will be removed as soon as it has been parsed due to it's large volume generally
                os.remove(sam)
        
        """
        [5/12] Gene relative abundance calculation
        """
        logging.info('[5/12] Gene relative abundance calculation'.center(50, '*'))
        make_dir(GENE_ABUN_DIR)
        pileup_dir = os.path.join(BBMAP_DIR, 'coverage')
        for bn in BASENAMES:
            logging.info("Calculate TPM values for {}".format(bn))
            pileup_out = os.path.join(pileup_dir, bn + '.pileup')
            gene_relative_abun(pileup_out, bn, GENE_ABUN_DIR)
    
        """
        Resolve ko_list file into dictionary
        """
        logging.info('[6/12] Resolve ko_list file into dict'.center(50, '*'))
        ko_list = os.path.join(KODB_DIR, 'ko_list')
        ko_dic = ko_list_parser(ko_list)
    
        """
        [6/12] KEGG annotation by hmmsearch
        """
        logging.info("[7/12] KEGG annotation by hmmsearch".center(50, '*'))
        make_dir(KEGG_DIR)
        kegg_pieces_dir = os.path.join(KEGG_DIR, 'hmmout')  # containing KEGG annotations of every knum
        make_dir(kegg_pieces_dir)
        for bn in BASENAMES:
            faa = os.path.join(PRODIGAL_DIR, bn + '.faa')
            kegg_annotation(faa, bn, kegg_pieces_dir, KODB_DIR, ko_dic, THREADS)
    
        """
        [7/12] Merge KEGG annotations
        """
        logging.info("[8/12] Merge KEGG annotations".center(50, '*'))
        ko_merged_tab = os.path.join(KEGG_DIR, 'ko_merged.txt')
        merge_ko(kegg_pieces_dir, ko_merged_tab)
    
        """
        [8/12] Merge KEGG annotations and gene relative abundances
        """
        logging.info("[9/12] Merge KEGG annotations and gene relative abundances".center(50, '*'))
        ko_abun_merged_tab = os.path.join(KEGG_DIR, 'ko_abun.txt')
        merge_abun_ko(GENE_ABUN_DIR, ko_merged_tab, ko_abun_merged_tab)
        ko_abundance_among_samples = os.path.join(KEGG_DIR, 'ko_abundance_among_samples.tab')
        table_of_ko_abundance_among_samples(ko_abun_merged_tab, ko_abundance_among_samples)

        """
        [9/12] Build gene families
        """
        logging.info("[9/12] Build gene families".center(50, '*'))
        make_dir(GENE_FAMILY)
        ORF_dir = PRODIGAL_DIR
        ko_abun_txt = os.path.join(KEGG_DIR, 'ko_abun.txt')
        outout_dir = GENE_FAMILY
        build_gene_family(ORF_dir, ko_abun_txt, outout_dir)

        
        """
        [10/12] Generate hierarchical table abundance among samples
        """
        logging.info("[10/12] Generate hierarchical table".center(50, '*'))
        ko_abundance_among_samples = os.path.join(KEGG_DIR, 'ko_abundance_among_samples.tab')
        KO_affilated_to_biogeochemical_cycle_tab = os.path.join(TABLE, 'KO_affilated_to_biogeochemical_cycle.tab')
        pathways_relative_abundance_gene_level_tab = os.path.join(OUT_DIR, 'pathways_relative_abundance_gene_level.tab')
        hierarchical_ko_abundance_among_samples(ko_abundance_among_samples, KO_affilated_to_biogeochemical_cycle_tab, pathways_relative_abundance_gene_level_tab)
    
        """
        [11/12] Calculate relative abundance of pathways
        """
        logging.info("[11/12] Calculate abundance of pathways".center(50, '*'))
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
        [12/12] Diagrammatic drawing
        """
        logging.info("[12/12] Diagrammatic drawing".center(50, '*'))
        sketch(ABUNDANCE_TABLE)
        os.system('rm -rf Figure_tmp')
        heatmap(ABUNDANCE_TABLE)
        os.system('rm -rf heatmap_tmp')
        cmd_mv = 'mv *.png ' + OUT_DIR
        os.system(cmd_mv)
        cmd_mv = 'mv *.pdf ' + OUT_DIR
        os.system(cmd_mv)
        cmd_mv = 'mv pathways_relative_abundance.tab ' + OUT_DIR
        os.system(cmd_mv)

        logging.info('All Done:)'.center(50, '*'))
        logging.info("Please find the results at directory: {}".format(OUT_DIR))

    
if __name__ == '__main__':
    main()
