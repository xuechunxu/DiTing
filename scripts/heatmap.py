"""
heatmap of table
"""

import os
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

    carbon_cycle = ['Photosystem II',
                    'Photosystem I',
                    'Cytochrome b6/f complex',
                    'Anoxygenic photosystem II (pufML)',
                    'Anoxygenic photosystem I (pscABCD)',
                    'RuBisCo',
                    'CBB cycle',
                    'rTCA cycle',
                    'Wood-Ljungdahl',
                    '3-Hydroxypropionate Bicycle',
                    'Dicarboxylate-hydroxybutyrate cycle',
                    'Pectinesterase',
                    'Diacetylchitobiose deacetylase',
                    'Glucoamylase',
                    'D-galacturonate epimerase',
                    'exo-poly-alpha-galacturonosidase',
                    'Oligogalacturonide lyase',
                    'Cellulase',
                    'exopolygalacturonase',
                    'Chitinase',
                    'Basic endochitinase B',
                    'Bifunctional chitinase/lysozyme',
                    'Beta-N-acetylhexosaminidase',
                    'D-galacturonate isomerase',
                    'Alpha-amylase',
                    'Beta-glucosidase',
                    'Pullulanase',
                    'Glycolysis',
                    'Entner-Doudoroff pathway, glucose-6P -> glyceraldehyde-3P + pyruvate',
                    'Gluconeogenesis, oxaloacetate -> fructose-6P',
                    'TCA cycle',
                    'Methanogenesis, methanol -> methane',
                    'Methanogenesis, methylamine -> methane',
                    'Methanogenesis, dimethylamine -> methane',
                    'Methanogenesis, trimethylamine -> methane',
                    'Methanogenesis, acetate -> methane',
                    'Methanogenesis, CO2 -> methane',
                    'Methane oxidation, methane -> methanol',
                    'Methane oxidation, methanol -> Formaldehyde',
                    'Mixed acid: lactate (pyruvate -> lactate)',
                    'Mixed acid: formate (pyruvate -> formate)',
                    'Mixed acid: Formate -> CO2 & H2',
                    'Mixed acid: acetate (pyruvate -> acetate)',
                    'Mixed acid: acetate (acetyl-CoA -> acetate)',
                    'Mixed acid: acetate (lactate -> acetate)',
                    'Mixed acid: ethanol, acetate to acetylaldehyde',
                    'Mixed acid: ethanol, acetyl-CoA to acetylaldehyde (reversible)',
                    'Mixed acid: ethanol, acetylaldehyde to ethanol',
                    'Mixed acid: succinate (phosphoenolpyruvate to succinate via oxaloacetate, malate & fumarate)',
                    'Anaplerotic genes (pyruvate -> oxaloacetate)']

    nitrogen_cycle = ['Dissimilatory nitrate reduction to nitrite (narGHI or napAB)',
                      'Dissimilatory nitrite reduction to ammonia (DNRA) (nirBD or nrfAH)',
                      'Assimilatory nitrate reduction to nitrite (narB or NR or nasAB)',
                      'Assimilatory nitrite reduction to ammonia (NIT-6 or nirA)',
                      'Denitrification, nitrite -> nitric oxide (nirK or nirS)',
                      'Denitrification, nitric oxide -> nitrous oxide (norBC)',
                      'Denitrification, nitrous oxide -> nitrogen (nosZ)',
                      'Nitrogen fixation, nitrogen -> ammonia (nifKDH)',
                      'Nitrification, ammonia -> hydroxylamine (amoABC)',
                      'Nitrification, hydroxylamine -> nitrite (hao)',
                      'Nitrification, nitrite -> nitrate (nxrAB)',
                      'Anammox, nitric oxide + ammonia -> hydrazine (hzs)',
                      'Anammox, hydrazine -> nitrogen (hdh)']

    sulfur_cycle = ['Assimilatory sulfate reduction to sulfite',
                    'Assimilatory sulfite reduction to sulfide (cysJI or sir)',
                    'Dissimilatory sulfate reduction to sulfite (reversible) (sat and aprAB)',
                    'Dissimilatory sulfite reduction to sulfide (reversible) (dsrAB)',
                    'Thiosulfate oxidation by SOX complex, thiosulfate -> sulfate',
                    'Alternative thiosulfate oxidation (doxAD)',
                    'Alternative thiosulfate oxidation (tsdA)',
                    'Sulfur reduction, sulfur -> sulfide (sreABC)',
                    'Thiosulfate disproportionation, thiosulfate -> sulfide & sulfite (phsABC)',
                    'Sulfhydrogenase, (sulfide)n -> (sulfide)n-1',
                    'Sulfur disproportionation, sulfur -> sulfide & sulfite',
                    'Sulfur dioxygenase',
                    'Sulfite oxidation, sulfite -> sulfate (sorB, SUOX, soeABC)',
                    'Sulfide oxidation, sulfide -> sulfur (fccAB)']

    other = ['F-type ATPase',
             'V/A-type ATPase',
             'NADH-quinone oxidoreductase',
             'NAD(P)H-quinone oxidoreductase',
             'Succinate dehydrogenase (ubiquinone)',
             'Cytochrome c oxidase, cbb3-type',
             'Cytochrome bd ubiquinol oxidase',
             'Cytochrome o ubiquinol oxidase',
             'Cytochrome c oxidase, prokaryotes',
             'Cytochrome aa3-600 menaquinol oxidase',
             'Cytochrome bc1 complex',
             'Phosphate transporter',
             'Phosphonate transporter',
             'Thiamin transporter',
             'Vitamin B12 transporter',
             'Urea transporter',
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
