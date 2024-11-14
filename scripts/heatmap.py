import os
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import logging

__author__ = "Xue Chunxu"
__contact__ = "xuechunxu@outlook.com"
__version__ = "0.6"

def heatmap(abundance_table):
    logging.info('Generate heatmap')
    if not os.path.exists('heatmap_tmp'):
        os.mkdir('heatmap_tmp')
    
    dict_table = {}
    head = ''
    
    # Parse the abundance table
    with open(abundance_table) as table:
        for line in table:
            line = line.strip('\n')
            if line.startswith('#'):
                head = line
            else:
                pathway = line.split('\t')[0]
                abundance = line.split('\t')[1:]
                values = '\t'.join(abundance)
                dict_table[pathway] = values

      
    # Define different cycles
    carbon_cycle =['Photosystem II (psbABCDEF)',
                    'Photosystem I (psaABCDEF)',
                    'Cytochrome b6/f complex (petABCDGLMN)',
                    'Anoxygenic photosystem II (pufML)',
                    'Anoxygenic photosystem I (pscABCD)',
                    'RuBisCo',
                    'CBB cycle (prkB)',
                    'rTCA cycle (aclAB, ccsAB, ccl)',
                    'Wood-Ljungdahl pathway (acsABCDE)',
                    '3-Hydroxypropionate Bicycle',
                    #'Dicarboxylate-hydroxybutyrate cycle',
                    #'Pectinesterase',
                    #'Diacetylchitobiose deacetylase',
                    #'Glucoamylase',
                    #'D-galacturonate epimerase',
                    #'exo-poly-alpha-galacturonosidase',
                    #'Oligogalacturonide lyase',
                    #'Cellulase',
                    #'exopolygalacturonase',
                    #'Chitinase',
                    #'Basic endochitinase B',
                    #'Bifunctional chitinase/lysozyme',
                    #'Beta-N-acetylhexosaminidase',
                    #'D-galacturonate isomerase',
                    #'Alpha-amylase',
                    #'Beta-glucosidase',
                    #'Pullulanase',
                    'Glycolysis (glk, pfk, pyk)',
                    'Entner-Doudoroff pathway, glucose-6P -> glyceraldehyde-3P + pyruvate',
                    'Gluconeogenesis (fbp, pck)',
                    'TCA cycle',
                    'Methanogenesis (mcrABG)',
                    'Methanogenesis, methanol -> methane (mtaABC)',
                    #'Methanogenesis, methylamine -> methane',
                    #'Methanogenesis, dimethylamine -> methane',
                    #'Methanogenesis, trimethylamine -> methane',
                    'Methanogenesis, amines -> methane (mtbA, mtmC, mtbC, mttC)',
                    'Methanogenesis, acetate -> methane (cdhCDE)',
                    'Methanogenesis, CO2 -> methane',
                    'Methane oxidation, methane -> methanol (mmoBCDXYZ, amoABC)',
                    'Methane oxidation, methanol -> formaldehyde (mxaFI, xoxF)',
                    'Fermentation to lactate, pyruvate -> lactate (LDH)',
                    'Fermentation to formate, pyruvate -> formate (pf1D)',
                    'Fermentation to formate -> CO2 & H2 (fdh)',
                    'Fermentation to acetate, pyruvate -> acetate (poxB, poxL, acyP)',
                    'Fermentation to acetate, acetyl-CoA -> acetate (ach1, eutD, pta, acyP)',
                    'Fermentation to acetate, lactate -> acetate (EC:1.13.12.4)',
                    'Fermentation to ethanol, acetate to acetylaldehyde (ald)',
                    'Fermentation to ethanol, acetyl-CoA to acetylaldehyde (reversible)',
                    'Fermentation to ethanol, acetylaldehyde to ethanol (adh, mdh)',
                    'Fermentation to succinate (phosphoenolpyruvate to succinate via oxaloacetate, malate & fumarate)',
                    'Anaplerotic genes (pyruvate -> oxaloacetate)']

    nitrogen_cycle = ['Dissimilatory nitrate reduction, nitrate -> nitrite (narGHI or napAB)',
                      'Dissimilatory nitrate reduction, nitrite -> ammonia (nirBD or nrfAH)',
                      'Assimilatory nitrate reduction, nitrate -> nitrite (narB or NR or nasAB)',
                      'Assimilatory nitrate reduction, nitrite -> ammonia (NIT-6 or nirA)',
                      'Denitrification, nitrite -> nitric oxide (nirK or nirS)',
                      'Denitrification, nitric oxide -> nitrous oxide (norBC)',
                      'Denitrification, nitrous oxide -> nitrogen (nosZ)',
                      'Nitrogen fixation, nitrogen -> ammonia (nifKDH)',
                      'Nitrification, ammonia -> hydroxylamine (amoABC)',
                      'Nitrification, hydroxylamine -> nitrite (hao)',
                      'Nitrification, nitrite -> nitrate (nxrAB)',
                      'Anammox, nitric oxide + ammonia -> hydrazine (hzs)',
                      'Anammox, hydrazine -> nitrogen (hdh)']

    sulfur_cycle = ['Assimilatory sulfate reduction, sulfate -> sulfite',
                    'Assimilatory sulfate reduction, sulfite -> sulfide (cysJI or sir)',
                    'Dissimilatory sulfate reduction, sulfate -> sulfite (reversible) (sat and aprAB)',
                    'Dissimilatory sulfate reduction, sulfite -> sulfide (reversible) (dsrAB)',
                    'Thiosulfate oxidation by SOX complex, thiosulfate -> sulfate',
                    'Alternative thiosulfate oxidation (doxAD)',
                    'Alternative thiosulfate oxidation (tsdA)',
                    'Sulfur reduction, sulfur -> sulfide (sreABC)',
                    'Thiosulfate disproportionation, thiosulfate -> sulfide & sulfite (phsABC)',
                    'Sulfhydrogenase, (sulfide)n -> (sulfide)n-1',
                    'Sulfur disproportionation, sulfur -> sulfide & sulfite',
                    'Sulfur dioxygenase',
                    'Sulfite oxidation, sulfite -> sulfate (sorB, SUOX, soeABC)',
                    'Sulfide oxidation, sulfide -> sulfur (fccAB)',
                    'DMSP biosynthesis, L-Met -> DMSP (DSYB or dsyB or mmtN)',
                    'DMSP demethylation, DMSP -> MMPA (dmdA)',
                    'DMSP demethylation, MMPA -> MeSH (dmdBCD or acuH)',
                    'DMSP cleavage, DMSP -> DMS (ddds or alma1)',
                    'DMS oxidation, DMS -> MeSH (dmoA)',
                    'DMS oxidation, DMS -> DMSO (ddhABC or tmm)',
                    'DMSO reduction, DMSO -> DMS (dms or dorA)',
                    'MddA pathway, MeSH -> DMS (mddA)',
                    'MeSH oxidation, MeSH -> Formaldehyde (MTO)',
                    'Sulfoquinovose degradation (sulfo-EMP pathway) (yihSVTU)',
                    'Sulfoquinovose degradation (sulfo-ED pathway)',
                    'Sulfoquinovose degradation (SFT pathway)']

    other = ['F-type ATPase',
             'V/A-type ATPase',
             'NADH-quinone oxidoreductase',
             'NAD(P)H-quinone oxidoreductase',
             'Succinate dehydrogenase (ubiquinone)',
             'Cytochrome c oxidase, cbb3-type',
             'Cytochrome bd ubiquinol oxidase',
             'Cytochrome o ubiquinol oxidase',
             'Cytochrome c oxidase, prokaryotes, aa3-type',
             'Cytochrome aa3-600 menaquinol oxidase',
             'Cytochrome bc1 complex',
             #'Phosphate transporter',
             #'Phosphonate transporter',
             #'Thiamin transporter',
             #'Vitamin B12 transporter',
             #'Urea transporter',
             'Type I Secretion',
             'Type III Secretion',
             'Type II Secretion',
             'Type IV Secretion',
             'Type VI Secretion',
             'Sec-SRP',
             'Twin arginine targeting',
             'Type Vabc secretion',
             'Bacterial chemotaxis',
             'Flagellum assembly',
             'Dissimilatory arsenic reduction',
             'Isoprene monooxygenase (IsoA)']

    # Write the data for each cycle into separate files
    with open('heatmap_tmp/carbon_cycle.tab', 'w') as carbon_out:
        carbon_out.write(head + '\n')
        for i in carbon_cycle:
            carbon_out.write(i + '\t' + dict_table[i] + '\n')

    with open('heatmap_tmp/nitrogen_cycle.tab', 'w') as nitrogen_out:
        nitrogen_out.write(head + '\n')
        for i in nitrogen_cycle:
            nitrogen_out.write(i + '\t' + dict_table[i] + '\n')

    with open('heatmap_tmp/sulfur_cycle.tab', 'w') as sulfur_out:
        sulfur_out.write(head + '\n')
        for i in sulfur_cycle:
            sulfur_out.write(i + '\t' + dict_table[i] + '\n')

    with open('heatmap_tmp/other_cycle.tab', 'w') as other_out:
        other_out.write(head + '\n')
        for i in other:
            other_out.write(i + '\t' + dict_table[i] + '\n')

    # List of generated table files for plotting heatmaps
    tables = ['carbon_cycle.tab',
              'nitrogen_cycle.tab',
              'sulfur_cycle.tab',
              'other_cycle.tab']

    # Generate heatmaps for each cycle and save them
    for i in tables:

        plt.figure()  # Create a new figure for each heatmap
        plt.clf()  # Clear the current figure to ensure no overlap
        plt.cla()  # Clear current axis to remove any residuals

        file_in = open('heatmap_tmp/' + i, "r")

        data = pd.read_table(file_in, index_col=0)

        fig, ax = plt.subplots(figsize=(8.27, 11.69))  # Set figure size
        sns.heatmap(data, cmap='coolwarm', xticklabels=True, yticklabels=True, square=True, ax=ax)

        # Save the heatmap as a PDF
        out_name = i.split('.tab')[0]
        fig.savefig(out_name + '_heatmap.pdf', bbox_inches='tight', dpi=600)

        plt.close(fig)  # Close the figure to free up memory
        sns.reset_orig()  # Reset Seaborn context to avoid conflicts in the next iteration
