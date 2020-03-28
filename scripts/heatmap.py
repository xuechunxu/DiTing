"""
heatmap of table
"""

import os
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import pandas as pd
import re
import seaborn as sns

__author__ = "Xue Chunxu"
__contact__ = "xuechunxu@outlook.com"
__version__ = "0.5"

def heatmap(abundance_table):
    print("\n" + 'Heatmap starting...Please wait. This may take a while'.center(70, '*'))
    os.mkdir('heatmap_tmp')
    dict_table = {}
    head = ''
    with open(abundance_table) as table:
        for line in table:
            line = line.strip('\n')
            if line.startswith('#'):
                head = line
            else:
                pathway = line.split('\t')[0]
                abundance = line.split('\t')
                del abundance[0]
                values = '\t'.join(abundance)
                dict_table[pathway] = values

    carbon_cycle = ['Photosystem II (psbABCDEF)',
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
                    'DMS oxidation, DMS -> DMSO (ddhA or tmm)',
                    'DMSO reduction, DMSO -> DMS (DMSOR)',
                    'MddA pathway, MeSH -> DMS (mddA)',
                    'MeSH oxidation, MeSH -> Formaldehyde (MTO)'
                    ]

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
             'Dissimilatory arsenic reduction']

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

    tables = ['carbon_cycle.tab',
              'nitrogen_cycle.tab',
              'sulfur_cycle.tab',
              'other_cycle.tab']

    #for i in tables:
        #file_in = open('heatmap_tmp/'+i, "r")
        #data = pd.read_table(file_in, index_col=0)
        #fig = plt.figure()
        #out_name = i.split('.tab')[0]
        #ggplot(data, aes('sample', 'pathway')) + geom_tile(aes(fill='relative abundance'))\
        #+ scale_fill_gradientn(colors=['blue','white','red']) \
        #+ ggtitle("Heatmap of relative abundance of pathways") \
        #+ ggsave(out_name + '_heatmap.png', dpi = 600)
        #plt.close()
    for i in tables:
        plt.cla()
        file_in = open('heatmap_tmp/'+i, "r")
        data = pd.read_table(file_in, index_col=0)
        #sns.set(font_scale=5)
        #color = ["blue", "white", "red"]
        #cmap = sns.palplot(sns.color_palette(color))
        #ax.set_xlabel('X_axi',fontsize=0.05);
        ax = sns.heatmap(data, cmap='coolwarm', xticklabels=True, yticklabels=True, square=True)
        #ax.xaxis.tick_top()
        #ax.set_yticklabels(ax.get_yticklabels(), rotation=90)
        #plt.xticks(rotation=90)
        #plt.yticks(rotation=0)
        # get figure (usually obtained via "fig,ax=plt.subplots()" with matplotlib)
        fig = ax.get_figure()
        # specify dimensions and save
        fig.set_size_inches(8.27, 11.69)
        out_name = i.split('.tab')[0]
        fig.savefig(out_name + '_heatmap.pdf', bbox_inches = 'tight', dpi = 600)
        plt.close()

    print("\n" + 'Heatmap visualization finished'.center(70, '*'))
