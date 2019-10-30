#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
import matplotlib
matplotlib.use('Agg')

parser = argparse.ArgumentParser(
    description="Accepts KEGG KOALA text file as input. \
    Produces function list and heat map figure.")
parser.add_argument(
    'Input', help="Input KOALA file. See documentation for correct format")
parser.add_argument('Output', help="List version of the final heat map figure")
args = parser.parse_args()
arg_dict = vars(args)


def Photosystem_II(dir, sample):
    out_data = {'Photosystem II': 0}
    ko_list = [sample+'_K02703', sample+'_K02704',
               sample+'_K02705', sample+'_K02706',
               sample+'_K02707', sample+'_K02708']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Photosystem II'] = (
        dir[sample+'_K02703'] +
        dir[sample+'_K02704'] +
        dir[sample+'_K02705'] +
        dir[sample+'_K02706'] +
        dir[sample+'_K02707'] +
        dir[sample+'_K02708'])/6
    return out_data


def Photosystem_I(dir, sample):
    out_data = {'Photosystem I': 0}
    ko_list = [sample+'_K02689', sample+'_K02690',
               sample+'_K02691', sample+'_K02692',
               sample+'_K02693', sample+'_K02694']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Photosystem I'] = (
        dir[sample+'_K02689'] +
        dir[sample+'_K02690'] +
        dir[sample+'_K02691'] +
        dir[sample+'_K02692'] +
        dir[sample+'_K02693'] +
        dir[sample+'_K02694'])/6
    return out_data


def Cytochrome_b6_f_complex(dir, sample):
    out_data = {'Cytochrome b6/f complex': 0}
    ko_list = [sample+'_K02635', sample+'_K02637',
               sample+'_K02634', sample+'_K02636',
               sample+'_K02642', sample+'_K02643',
               sample+'_K03689', sample+'_K02640']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Cytochrome b6/f complex'] = (
        dir[sample+'_K02635'] +
        dir[sample+'_K02637'] +
        dir[sample+'_K02634'] +
        dir[sample+'_K02636'] +
        dir[sample+'_K02642'] +
        dir[sample+'_K02643'] +
        dir[sample+'_K03689'] +
        dir[sample+'_K02640'])/8
    return out_data


def anoxygenic_photosystem_II_pufML(dir, sample):
    out_data = {'Anoxygenic photosystem II (pufML)': 0}
    ko_list = [sample+'_K08929', sample+'_K08928']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Anoxygenic photosystem II (pufML)'] = (
        dir[sample+'_K08928'] +
        dir[sample+'_K08929'])/2
    return out_data


def anoxygenic_photosystem_I_pscABCD(dir, sample):
    out_data = {'Anoxygenic photosystem I (pscABCD)': 0}
    ko_list = [sample+'_K08940', sample+'_K08941',
               sample+'_K08942', sample+'_K08943']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Anoxygenic photosystem I (pscABCD)'] = (
        dir[sample+'_K08940'] +
        dir[sample+'_K08941'] +
        dir[sample+'_K08942'] +
        dir[sample+'_K08943'])/4
    return out_data


def RuBisCo(dir, sample):
    out_data = {'RuBisCo': 0}
    ko_list = [sample+'_K01601']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['RuBisCo'] = dir[sample+'_K01602']
    return out_data


def CBB_Cycle(dir, sample):
    out_data = {'CBB Cycle': 0}
    ko_list = [sample+'_K00855', sample+'_K01601', sample+'_K00927',
               sample+'_K05298', sample+'_K00150', sample+'_K00134',
               sample+'_K01623', sample+'_K01624', sample+'_K03841',
               sample+'_K02446', sample+'_K11532', sample+'_K01086',
               sample+'_K04041', sample+'_K00615', sample+'_K01100',
               sample+'_K01807', sample+'_K01808']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['CBB Cycle'] = (
      dir[sample+'_K00855'] +
      dir[sample+'_K01601'] +
      dir[sample+'_K00927'] +
      dir[sample+'_K05298'] +
      dir[sample+'_K00150'] +
      dir[sample+'_K00134'] +
      dir[sample+'_K01623'] +
      dir[sample+'_K01624'] +
      dir[sample+'_K03841'] +
      dir[sample+'_K02446'] +
      dir[sample+'_K11532'] +
      dir[sample+'_K01086'] +
      dir[sample+'_K04041'] +
      dir[sample+'_K00615'] +
      dir[sample+'_K01623'] +
      dir[sample+'_K01624'] +
      dir[sample+'_K01100'] +
      dir[sample+'_K11532'] +
      dir[sample+'_K01086'] +
      dir[sample+'_K00615'] +
      dir[sample+'_K01623'] +
      dir[sample+'_K01624'] +
      dir[sample+'_K01100'] +
      dir[sample+'_K11532'] +
      dir[sample+'_K01086'] +
      dir[sample+'_K00615'] +
      dir[sample+'_K01807'] +
      dir[sample+'_K01808'])/11
    return out_data


def rTCA_Cycle(dir, sample):
    out_data = {'rTCA Cycle': 0}
    ko_list = [sample+'_K15230', sample+'_K15231',
               sample+'_K15232', sample+'_K15233',
               sample+'_K15234']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['rTCA Cycle'] = (
        (dir[sample+'_K15230'] +
         dir[sample+'_K15231'])/2 +
        ((dir[sample+'_K15232'] +
          dir[sample+'_K15233'])/2 +
         dir[sample+'_K15234'])/2)
    return out_data


def Wood_Ljungdahl(dir, sample):
    out_data = {'Wood-Ljungdahl': 0}
    ko_list = [sample+'_K00198', sample+'_K05299', sample+'_K01938',
               sample+'_K01491', sample+'_K00297', sample+'_K15023',
               sample+'_K14138', sample+'_K00197', sample+'_K00194']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Wood-Ljungdahl'] = (
      dir[sample+'_K00198'] +
      dir[sample+'_K05299'] +
      dir[sample+'_K01938'] +
      dir[sample+'_K01491'] +
      dir[sample+'_K00297'] +
      dir[sample+'_K15023'] +
      (dir[sample+'_K14138'] +
       dir[sample+'_K00197'] +
       dir[sample+'_K00194'])/3)/7
    return out_data


def three_Hydroxypropionate_Bicycle(dir, sample):
    out_data = {'3-Hydroxypropionate Bicycle': 0}
    ko_list = [sample+'_K02160', sample+'_K01961', sample+'_K01962',
               sample+'_K01963', sample+'_K14468', sample+'_K14469',
               sample+'_K08691', sample+'_K14449', sample+'_K14470',
               sample+'_K09709', sample+'_K15052', sample+'_K05606',
               sample+'_K01847', sample+'_K01848', sample+'_K01849',
               sample+'_K14471', sample+'_K14472', sample+'_K00239',
               sample+'_K00240', sample+'_K00241', sample+'_K01679']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['3-Hydroxypropionate Bicycle'] = (
      (dir[sample+'_K02160'] +
       dir[sample+'_K01961'] +
       dir[sample+'_K01962'] +
       dir[sample+'_K01963'])/4 +
      dir[sample+'_K14468'] +
      dir[sample+'_K14469'] +
      dir[sample+'_K08691'] +
      dir[sample+'_K14449'] +
      dir[sample+'_K14470'] +
      dir[sample+'_K09709'] +
      dir[sample+'_K08691'] +
      dir[sample+'_K15052'] +
      dir[sample+'_K05606'] +
      dir[sample+'_K01847'] +
      (dir[sample+'_K01848'] +
       dir[sample+'_K01849'])/2 +
      (dir[sample+'_K14471'] +
       dir[sample+'_K14472'])/2 +
      (dir[sample+'_K00239'] +
       dir[sample+'_K00240'] +
       dir[sample+'_K00241'])/3 +
      dir[sample+'_K01679'] +
      (dir[sample+'_K14471'] +
       dir[sample+'_K14472'])/2 +
      dir[sample+'_K08691'])/16
    return out_data


def Dicarboxylate_hydroxybutyrate_cycle(dir, sample):
    out_data = {'Dicarboxylate-hydroxybutyrate cycle': 0}
    ko_list = [sample+'_K00169', sample+'_K00170', sample+'_K00171',
               sample+'_K00172', sample+'_K01007', sample+'_K01595',
               sample+'_K00024', sample+'_K01676', sample+'_K01677',
               sample+'_K01678', sample+'_K00239', sample+'_K00240',
               sample+'_K01902', sample+'_K01903', sample+'_K15038',
               sample+'_K15017', sample+'_K14465', sample+'_K14467',
               sample+'_K18861', sample+'_K14534', sample+'_K15016',
               sample+'_K00626']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Dicarboxylate-hydroxybutyrate cycle'] = (
      (dir[sample+'_K00169'] +
       dir[sample+'_K00170'] +
       dir[sample+'_K00171'] +
       dir[sample+'_K00172'])/4 +
      dir[sample+'_K01007'] +
      dir[sample+'_K01595'] +
      dir[sample+'_K00024'] +
      dir[sample+'_K01676'] +
      (dir[sample+'_K01677'] +
       dir[sample+'_K01678'])/2 +
      (dir[sample+'_K00239'] +
       dir[sample+'_K00240'])/2 +
      (dir[sample+'_K01902'] +
       dir[sample+'_K01903'])/2 +
      dir[sample+'_K15038'] +
      dir[sample+'_K15017'] +
      dir[sample+'_K14465'] +
      dir[sample+'_K14467'] +
      dir[sample+'_K18861'] +
      dir[sample+'_K14534'] +
      dir[sample+'_K15016'] +
      dir[sample+'_K15016'] +
      dir[sample+'_K00626'])/14
    return out_data


def pectinesterase(dir, sample):
    out_data = {'Pectinesterase': 0}
    ko_list = [sample+'_K01051']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Pectinesterase'] = dir[sample+'_K01051']
    return out_data


def diacetylchitobiose_deacetylase(dir, sample):
    out_data = {'Diacetylchitobiose deacetylase': 0}
    ko_list = [sample+'_K18454', sample+'_K03478']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Diacetylchitobiose deacetylase'] = (dir[sample+'_K18454'] +
                                                  dir[sample+'_K03478'])
    return out_data


def glucoamylase(dir, sample):
    out_data = {'Glucoamylase': 0}
    ko_list = [sample+'_K01178']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Glucoamylase'] = dir[sample+'_K01178']
    return out_data


def D_galacturonate_epimerase(dir, sample):
    out_data = {'D-galacturonate epimerase': 0}
    ko_list = [sample+'_K08679']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['D-galacturonate epimerase'] = dir[sample+'_K08679']
    return out_data


def exo_poly_alpha_galacturonosidase(dir, sample):
    out_data = {'exo-poly-alpha-galacturonosidase': 0}
    ko_list = [sample+'_K18650']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['exo-poly-alpha-galacturonosidase'] = dir[sample+'_K18650']
    return out_data


def oligogalacturonide_lyase(dir, sample):
    out_data = {'Oligogalacturonide lyase': 0}
    ko_list = [sample+'_K01730']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Oligogalacturonide lyase'] = dir[sample+'_K01730']
    return out_data


def cellulase(dir, sample):
    out_data = {'Cellulase': 0}
    ko_list = [sample+'_K19668', sample+'_K01225']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Cellulase'] = dir[sample+'_K19668']+dir[sample+'_K01225']
    return out_data


def exopolygalacturonase(dir, sample):
    out_data = {'exopolygalacturonase': 0}
    ko_list = [sample+'_K01184']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['exopolygalacturonase'] = dir[sample+'_K01184']
    return out_data


def chitinase(dir, sample):
    out_data = {'Chitinase': 0}
    ko_list = [sample+'_K01183']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Chitinase'] = dir[sample+'_K01183']
    return out_data


def basic_endochitinase_B(dir, sample):
    out_data = {'Basic endochitinase B': 0}
    ko_list = [sample+'_K20547']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Basic endochitinase B'] = dir[sample+'_K20547']
    return out_data


def bifunctional_chitinase_or_lysozyme(dir, sample):
    out_data = {'bifunctional chitinase/lysozyme': 0}
    ko_list = [sample+'_K13381']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['bifunctional chitinase/lysozyme'] = dir[sample+'_K13381']
    return out_data


def beta_N_acetylhexosaminidase(dir, sample):
    out_data = {'beta-N-acetylhexosaminidase': 0}
    ko_list = [sample+'_K01207']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['beta-N-acetylhexosaminidase'] = dir[sample+'_K01207']
    return out_data


def D_galacturonate_isomerase(dir, sample):
    out_data = {'D-galacturonate isomerase': 0}
    ko_list = [sample+'_K01812']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['D-galacturonate isomerase'] = dir[sample+'_K01812']
    return out_data


def alpha_amylase(dir, sample):
    out_data = {'alpha-amylase': 0}
    ko_list = [sample+'_K01176']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['alpha-amylase'] = dir[sample+'_K01176']
    return out_data


def beta_glucosidase(dir, sample):
    out_data = {'beta-glucosidase': 0}
    ko_list = [sample+'_K05349', sample+'_K05350']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['beta-glucosidase'] = dir[sample+'_K05350']+dir[sample+'_K05349']
    return out_data


def pullulanase(dir, sample):
    out_data = {'pullulanase': 0}
    ko_list = [sample+'_K01200']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['pullulanase'] = dir[sample+'_K01200']
    return out_data


def glycolysis(dir, sample):
    out_data = {'glycolysis': 0}
    ko_list = [sample+'_K00844', sample+'_K12407', sample+'_K00845',
               sample+'_K00886', sample+'_K08074', sample+'_K01810',
               sample+'_K06859', sample+'_K13810', sample+'_K12406',
               sample+'_K15916', sample+'_K00850', sample+'_K16370',
               sample+'_K00918', sample+'_K01623', sample+'_K01689',
               sample+'_K11645', sample+'_K16305', sample+'_K16306',
               sample+'_K00873', sample+'_K01624', sample+'_K15635',
               sample+'_K16305', sample+'_K01803', sample+'_K11389',
               sample+'_K00134', sample+'_K15633', sample+'_K00927',
               sample+'_K01834', sample+'_K15634']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['glycolysis'] = (dir[sample+'_K00844'] +
                              dir[sample+'_K12407'] +
                              dir[sample+'_K00845'] +
                              dir[sample+'_K00886'] +
                              dir[sample+'_K08074'] +
                              dir[sample+'_K00918'] +
                              dir[sample+'_K01810'] +
                              dir[sample+'_K06859'] +
                              dir[sample+'_K13810'] +
                              dir[sample+'_K15916'] +
                              dir[sample+'_K00850'] +
                              dir[sample+'_K16370'] +
                              dir[sample+'_K00918'] +
                              (dir[sample+'_K01623'] +
                               dir[sample+'_K01624'] +
                               dir[sample+'_K11645'] +
                               dir[sample+'_K16305'] +
                               dir[sample+'_K16306']) +
                              (dir[sample+'_K01623'] +
                               dir[sample+'_K01624'] +
                               dir[sample+'_K11645'] +
                               dir[sample+'_K16305'] +
                               dir[sample+'_K16306'] +
                               dir[sample+'_K01803'])/2 +
                              dir[sample+'_K11389'] +
                              (dir[sample+'_K00134'] +
                               dir[sample+'_K15633'] +
                               dir[sample+'_K00927'])/2 +
                              dir[sample+'_K01834'] +
                              dir[sample+'_K15633'] +
                              dir[sample+'_K15634'] +
                              dir[sample+'_K15635'] +
                              dir[sample+'_K01689'] +
                              dir[sample+'_K00873'] +
                              dir[sample+'_K12406'])/8
    return out_data


def Entner_Doudoroff_Pathway(dir, sample):
    out_data = {'Entner-Doudoroff pathway, glucose-6P -> glyceraldehyde-3P + pyruvate': 0}
    ko_list = [sample+'_K00036', sample+'_K01057',
               sample+'_K07404', sample+'_K01690',
               sample+'_K01625']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Entner-Doudoroff pathway, glucose-6P -> glyceraldehyde-3P + pyruvate'] = (
        dir[sample+'_K00036'] +
        dir[sample+'_K01057'] +
        dir[sample+'_K07404'] +
        dir[sample+'_K01690'] +
        dir[sample+'_K01625'])/4
    return out_data


def gluconeogenesis(dir, sample):
    out_data = {'gluconeogenesis, oxaloacetate -> fructose-6P': 0}
    ko_list = [sample+'_K01596', sample+'_K01610', sample+'_K01689',
               sample+'_K01834', sample+'_K15633', sample+'_K15634',
               sample+'_K15635', sample+'_K00927', sample+'_K00134',
               sample+'_K00150', sample+'_K01803', sample+'_K11645',
               sample+'_K01623', sample+'_K01624', sample+'_K01622',
               sample+'_K03841', sample+'_K02446', sample+'_K11532',
               sample+'_K01086', sample+'_K04041']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['gluconeogenesis, oxaloacetate -> fructose-6P'] = (dir[sample+'_K01596'] +
                                   dir[sample+'_K01610'] +
                                   dir[sample+'_K01689'] +
                                   dir[sample+'_K01834'] +
                                   dir[sample+'_K15633'] +
                                   dir[sample+'_K15634'] +
                                   dir[sample+'_K15635'] +
                                   dir[sample+'_K00927'] +
                                   dir[sample+'_K00134'] +
                                   dir[sample+'_K00150'] +
                                   (dir[sample+'_K01803'] +
                                    dir[sample+'_K01623'] +
                                    dir[sample+'_K01624'] +
                                    dir[sample+'_K11645'])/2 +
                                   dir[sample+'_K01623'] +
                                   dir[sample+'_K01624'] +
                                   dir[sample+'_K11645'] +
                                   dir[sample+'_K01622'] +
                                   dir[sample+'_K03841'] +
                                   dir[sample+'_K02446'] +
                                   dir[sample+'_K11532'] +
                                   dir[sample+'_K01086'] +
                                   dir[sample+'_K04041'])/7
    return out_data


def tca_cycle(dir, sample):
    out_data = {'TCA Cycle': 0}
    ko_list = [sample+'_K01647', sample+'_K05942', sample+'_K01681',
               sample+'_K01682', sample+'_K00031', sample+'_K00030',
               sample+'_K00174', sample+'_K00175', sample+'_K00164',
               sample+'_K00658', sample+'_K00382', sample+'_K01902',
               sample+'_K01903', sample+'_K01899', sample+'_K01900',
               sample+'_K18118', sample+'_K00234', sample+'_K00235',
               sample+'_K00236', sample+'_K00237', sample+'_K00239',
               sample+'_K00240', sample+'_K00241', sample+'_K00244',
               sample+'_K00245', sample+'_K00246', sample+'_K01676',
               sample+'_K01679', sample+'_K01677', sample+'_K01678',
               sample+'_K00026', sample+'_K00025', sample+'_K00024',
               sample+'_K00116']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['TCA Cycle'] = (
        (dir[sample+'_K01647'] +
         dir[sample+'_K05942']) +
        (dir[sample+'_K01681'] +
         dir[sample+'_K01682']) +
        (dir[sample+'_K00031'] +
         dir[sample+'_K00030']) +
        (dir[sample+'_K00174'] +
         dir[sample+'_K00175'])/2 +
        (dir[sample+'_K00164'] +
         dir[sample+'_K00658'] +
         dir[sample+'_K00382'])/3 +
        (dir[sample+'_K01902'] +
         dir[sample+'_K01903'])/2 +
        (dir[sample+'_K01899'] +
         dir[sample+'_K01900'])/2 +
        dir[sample+'_K18118'] +
        (dir[sample+'_K00234'] +
         dir[sample+'_K00235'] +
         dir[sample+'_K00236'] +
         dir[sample+'_K00237'])/4 +
        (dir[sample+'_K00239'] +
         dir[sample+'_K00240'] +
         dir[sample+'_K00241'])/3 +
        (dir[sample+'_K00244'] +
         dir[sample+'_K00245'] +
         dir[sample+'_K00246'])/3 +
        dir[sample+'_K01676'] +
        dir[sample+'_K01679'] +
        (dir[sample+'_K01677'] +
         dir[sample+'_K01678'])/2 +
        dir[sample+'_K00026'] +
        dir[sample+'_K00025'] +
        dir[sample+'_K00024'] +
        dir[sample+'_K00116'])/8
    return out_data


def Methanogenesis_via_methanol(dir, sample):
    out_data = {'Methanogenesis, methanol -> methane': 0}
    ko_list = [sample+'_K04480', sample+'_K14080',
               sample+'_K14081', sample+'_K00399',
               sample+'_K00401', sample+'_K00402']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis, methanol -> methane'] = (
        (dir[sample+'_K04480'] +
         dir[sample+'_K14080'] +
         dir[sample+'_K14081'])/3 +
        (dir[sample+'_K00399'] +
         dir[sample+'_K00401'] +
         dir[sample+'_K00402'])/3)/2
    return out_data


def Methanogenesis_via_methylamine(dir, sample):
    out_data = {'Methanogenesis, methylamine -> methane': 0}
    ko_list = [sample+'_K14082', sample+'_K16177',
               sample+'_K00399', sample+'_K00401',
               sample+'_K00402']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis, methylamine -> methane'] = (
      (dir[sample+'_K14082'] +
       dir[sample+'_K16177'])/2 +
      (dir[sample+'_K00399'] +
       dir[sample+'_K00401'] +
       dir[sample+'_K00402'])/3)/2
    return out_data


def Methanogenesis_via_dimethylamine(dir, sample):
    out_data = {'Methanogenesis, dimethylamine -> methane': 0}
    ko_list = [sample+'_K14082', sample+'_K16179',
               sample+'_K00399', sample+'_K00401',
               sample+'_K00402']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis, dimethylamine -> methane'] = (
      (dir[sample+'_K14082'] +
       dir[sample+'_K16179'])/2 +
      (dir[sample+'_K00399'] +
       dir[sample+'_K00401'] +
       dir[sample+'_K00402'])/3)/2
    return out_data


def Methanogenesis_via_trimethylamine(dir, sample):
    out_data = {'Methanogenesis, trimethylamine -> methane': 0}
    ko_list = [sample+'_K14082', sample+'_K14084',
               sample+'_K00399', sample+'_K00401',
               sample+'_K00402']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis, trimethylamine -> methane'] = (
      (dir[sample+'_K14082'] +
       dir[sample+'_K14084'])/2 +
      (dir[sample+'_K00399'] +
       dir[sample+'_K00401'] +
       dir[sample+'_K00402'])/3)/2
    return out_data


def Methanogenesis_via_acetate(dir, sample):
    out_data = {'Methanogenesis, acetate -> methane': 0}
    ko_list = [sample+'_K00925', sample+'_K00625', sample+'_K13788',
               sample+'_K01895', sample+'_K00193', sample+'_K00194', 
               sample+'_K00197', sample+'_K00577', sample+'_K00578', 
               sample+'_K00579', sample+'_K00580', sample+'_K00581', 
               sample+'_K00584', sample+'_K00399', sample+'_K00401', 
               sample+'_K00402']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis, acetate -> methane'] = (
      (dir[sample+'_K00925'] +
       dir[sample+'_K00625'] +
       dir[sample+'_K13788'])/2 +
      dir[sample+'_K01895'] +
      (dir[sample+'_K00193'] +
       dir[sample+'_K00194'] +
       dir[sample+'_K00197'])/3 +
      (dir[sample+'_K00577'] +
       dir[sample+'_K00578'] +
       dir[sample+'_K00579'] +
       dir[sample+'_K00580'] +
       dir[sample+'_K00581'] +
       dir[sample+'_K00584'])/6 +
      (dir[sample+'_K00399'] +
       dir[sample+'_K00401'] +
       dir[sample+'_K00402'])/3)/4
    return out_data


def Methanogenesis_CO2_methane(dir, sample):
    out_data = {'Methanogenesis, CO2 -> methane': 0}
    ko_list = [sample+'_K00200', sample+'_K00201', sample+'_K00202',
               sample+'_K00203', sample+'_K11261', sample+'_K00205',
               sample+'_K11260', sample+'_K00204', sample+'_K00672',
               sample+'_K01499', sample+'_K00319', sample+'_K13942',
               sample+'_K00320', sample+'_K00577', sample+'_K00578',
               sample+'_K00579', sample+'_K00580', sample+'_K00581',
               sample+'_K00584', sample+'_K00399', sample+'_K00401',
               sample+'_K00402']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis, CO2 -> methane'] = (
      (dir[sample+'_K00200'] +
       dir[sample+'_K00201'] +
       dir[sample+'_K00202'] +
       dir[sample+'_K00203'] +
       dir[sample+'_K11261'] +
       dir[sample+'_K00205'] +
       dir[sample+'_K11260'] +
       dir[sample+'_K00204'])/6 +
      dir[sample+'_K00672'] +
      dir[sample+'_K01499'] +
      dir[sample+'_K00319'] +
      dir[sample+'_K13942'] +
      dir[sample+'_K00320'] +
      (dir[sample+'_K00577'] +
       dir[sample+'_K00578'] +
       dir[sample+'_K00579'] +
       dir[sample+'_K00580'] +
       dir[sample+'_K00581'] +
       dir[sample+'_K00584'])/6 +
      (dir[sample+'_K00399'] +
       dir[sample+'_K00401'] +
       dir[sample+'_K00402'])/3)/7
    return out_data


def Methane_oxidation_methane_methanol(dir, sample):
    out_data = {'Methane oxidation, methanol -> Formaldehyde': 0}
    ko_list = [sample+'_K16157', sample+'_K16158', sample+'_K16159', 
               sample+'_K16160', sample+'_K16161', sample+'_K16162',
               sample+'_K10944', sample+'_K10945', sample+'_K10946']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methane oxidation, methanol -> Formaldehyde'] = (
      (dir[sample+'_K16157'] +
       dir[sample+'_K16158'] +
       dir[sample+'_K16159'] +
       dir[sample+'_K16160'] +
       dir[sample+'_K16161'] +
       dir[sample+'_K16162'])/6 +
      (dir[sample+'_K10944'] +
       dir[sample+'_K10945'] +
       dir[sample+'_K10946'])/3)
    return out_data


def Methane_oxidation_methanol_Formaldehyde(dir, sample):
    out_data = {'Methane oxidation, methanol -> Formaldehyde': 0}
    ko_list = [sample+'_K14028', sample+'_K14029',
               sample+'_K17066']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methane oxidation, methanol -> Formaldehyde'] = (
      (dir[sample+'_K14028'] +
       dir[sample+'_K14029'])/2 +
      dir[sample+'_K17066'])
    return out_data


def Mixed_acid_lactate(dir, sample):
    out_data = {'Mixed acid: lactate (pyruvate -> lactate)': 0}
    ko_list = [sample+'_K00016']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: lactate (pyruvate -> lactate)'] = (
      dir[sample+'_K00016'])
    return out_data


def Mixed_acid_formate(dir, sample):
    out_data = {'Mixed acid: formate (pyruvate -> formate)': 0}
    ko_list = [sample+'_K00656']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: formate (pyruvate -> formate)'] = (
      dir[sample+'_K00656'])
    return out_data


def Mixed_acid_Formate_to_CO2_H2(dir, sample):
    out_data = {'Mixed acid: Formate -> CO2 & H2': 0}
    ko_list = [sample+'_K00122', sample+'_K00123', sample+'_K00124',
               sample+'_K00126', sample+'_K00127', sample+'_K22515',
               sample+'_K22516', sample+'_K00125']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: Formate -> CO2 & H2'] = (
      (dir[sample+'_K00122'] +
       dir[sample+'_K00123'] +
       dir[sample+'_K00124'] +
       dir[sample+'_K00126'] +
       dir[sample+'_K00127'] +
       dir[sample+'_K22515'])/6 +
      (dir[sample+'_K22516'] +
       dir[sample+'_K00125'])/2)
    return out_data


def Mixed_acid_acetate(dir, sample):
    out_data = {'Mixed acid: acetate': 0}
    ko_list = [sample+'_K00156', sample+'_K00158', sample+'_K01512',
               sample+'_K00467', sample+'_K01067', sample+'_K04020',
               sample+'_K13788', sample+'_K00625']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: acetate'] = (
      dir[sample+'_K00156'] +
      (dir[sample+'_K00158'] +
       dir[sample+'_K01512'])/2 +
      dir[sample+'_K00467'] +
      dir[sample+'_K01067'] +
      (dir[sample+'_K04020'] +
       dir[sample+'_K13788'] +
       dir[sample+'_K00625'] +
       dir[sample+'_K01512'])/2)
    return out_data


def Mixed_acid_Ethanol_Acetate_to_Acetylaldehyde(dir, sample):
    out_data = {'Mixed acid: ethanol, acetate to acetylaldehyde': 0}
    ko_list = [sample+'_K00128', sample+'_K14085', sample+'_K00149',
               sample+'_K00129', sample+'_K00138']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: ethanol, acetate to acetylaldehyde'] = (
      dir[sample+'_K00128'] +
      dir[sample+'_K14085'] +
      dir[sample+'_K00149'] +
      dir[sample+'_K00129'] +
      dir[sample+'_K00138'])
    return out_data


def Mixed_acid_Ethanol_Acetyl_CoA_to_Acetylaldehyde(dir, sample):
    out_data = {'Mixed acid: ethanol, acetyl-CoA to acetylaldehyde (reversible)': 0}
    ko_list = [sample+'_K00132', sample+'_K04072', sample+'_K04073',
               sample+'_K18366', sample+'_K04021']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: ethanol, acetyl-CoA to acetylaldehyde (reversible)'] = (
      dir[sample+'_K00132'] +
      dir[sample+'_K04072'] +
      dir[sample+'_K04073'] +
      dir[sample+'_K18366'] +
      dir[sample+'_K04021'])
    return out_data


def Mixed_acid_Ethanol_Acetylaldehyde_to_Ethanol(dir, sample):
    out_data = {'Mixed acid: ethanol, acetylaldehyde to ethanol': 0}
    ko_list = [sample+'_K13951', sample+'_K13980', sample+'_K13952',
               sample+'_K13953', sample+'_K13954', sample+'_K00001',
               sample+'_K00121', sample+'_K04072', sample+'_K18857',
               sample+'_K14028', sample+'_K14029', sample+'_K00114',
               sample+'_K00002', sample+'_K04022']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: ethanol, acetylaldehyde to ethanol'] = (
      dir[sample+'_K13951'] +
      dir[sample+'_K13980'] +
      dir[sample+'_K13952'] +
      dir[sample+'_K13953'] +
      dir[sample+'_K13954'] +
      dir[sample+'_K00001'] +
      dir[sample+'_K00121'] +
      dir[sample+'_K04072'] +
      dir[sample+'_K18857'] +
      (dir[sample+'_K14028'] +
       dir[sample+'_K14029'])/2 +
      dir[sample+'_K00114'] +
      dir[sample+'_K00002'] +
      dir[sample+'_K04022'])
    return out_data


def Mixed_acid_succinate(dir, sample):
    out_data = {'Mixed acid: succinate (phosphoenolpyruvate to succinate via oxaloacetate, malate & fumarate)': 0}
    ko_list = [sample+'_K01595', sample+'_K01596', sample+'_K20370', 
               sample+'_K01610', sample+'_K00024', sample+'_K00025', 
               sample+'_K00026', sample+'_K00051', sample+'_K00116', 
               sample+'_K01676', sample+'_K01679', sample+'_K01677', 
               sample+'_K01678', sample+'_K00244', sample+'_K00245', 
               sample+'_K00246', sample+'_K00247']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: succinate (phosphoenolpyruvate to succinate via oxaloacetate, malate & fumarate)'] = (
      dir[sample+'_K01595'] +
      dir[sample+'_K01596'] +
      dir[sample+'_K20370'] +
      dir[sample+'_K01610'] +
      dir[sample+'_K00024'] +
      dir[sample+'_K00025'] +
      dir[sample+'_K00026'] +
      dir[sample+'_K00051'] +
      dir[sample+'_K00116'] +
      dir[sample+'_K01676'] +
      dir[sample+'_K01679'] +
      (dir[sample+'_K01677'] +
       dir[sample+'_K01678'])/2 +
      (dir[sample+'_K00244'] +
       dir[sample+'_K00245'] +
       dir[sample+'_K00246'] +
       dir[sample+'_K00247'])/4)/4
    return out_data


def Glyoxylate_shunt(dir, sample):
    out_data = {'Mixed acid: ethanol, acetyl-CoA to acetylaldehyde (reversible)': 0}
    ko_list = [sample+'_K01637', sample+'_K01638', sample+'_K19282']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: ethanol, acetyl-CoA to acetylaldehyde (reversible)'] = (
      dir[sample+'_K01637'] +
      dir[sample+'_K01638'] +
      dir[sample+'_K19282'])/2
    return out_data


def Anaplerotic_genes(dir, sample):
    out_data = {'Anaplerotic genes (pyruvate -> oxaloacetate)': 0}
    ko_list = [sample+'_K00027', sample+'_K00028', sample+'_K00029',
               sample+'_K01958', sample+'_K01959', sample+'_K01960',
               sample+'_K01595', sample+'_K01610', sample+'_K01596',
               sample+'_K20370']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Anaplerotic genes (pyruvate -> oxaloacetate)'] = (
      dir[sample+'_K00027'] +
      dir[sample+'_K00028'] +
      dir[sample+'_K00029'] +
      dir[sample+'_K01958'] +
      (dir[sample+'_K01959'] +
       dir[sample+'_K01960'])/2 +
      dir[sample+'_K01595'] +
      dir[sample+'_K01610'] +
      dir[sample+'_K01596'] +
      dir[sample+'_K20370'])
    return out_data


def Dissimilatory_nitrate_reduction_to_nitrite(dir, sample):
    out_data = {'Dissimilatory nitrate reduction to nitrite': 0}
    ko_list = [sample+'_K00370', sample+'_K00371', sample+'_K00374',
               sample+'_K02567', sample+'_K02568']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Dissimilatory nitrate reduction to nitrite'] = (
        (dir[sample+'_K00370'] +
         dir[sample+'_K00371'] +
         dir[sample+'_K00374'])/3 +
        (dir[sample+'_K02567'] +
         dir[sample+'_K02568'])/2)
    return out_data


def Dissimilatory_nitrite_reduction_to_ammonia(dir, sample):
    out_data = {'Dissimilatory nitrite reduction to ammonia': 0}
    ko_list = [sample+'_K00362', sample+'_K00363', sample+'_K03385',
               sample+'_K15876']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Dissimilatory nitrite reduction to ammonia'] = (
      (dir[sample+'_K00362'] +
       dir[sample+'_K00363'])/2 +
      (dir[sample+'_K03385'] +
       dir[sample+'_K15876'])/2)
    return out_data


def DNRA(dir, sample):
    out_data = {'DNRA': 0}
    ko_list = [sample+'_K00370', sample+'_K00371', sample+'_K00374',
               sample+'_K02567', sample+'_K02568', sample+'_K00362',
               sample+'_K00363', sample+'_K03385', sample+'_K15876']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['DNRA'] = (
        (dir[sample+'_K00370'] +
         dir[sample+'_K00371'] +
         dir[sample+'_K00374'])/3 +
        (dir[sample+'_K02567'] +
         dir[sample+'_K02568'])/2 +
        (dir[sample+'_K00362'] +
         dir[sample+'_K00363'])/2 +
        (dir[sample+'_K03385'] +
         dir[sample+'_K15876'])/2)/2
    return out_data


def Assimilatory_nitrate_reduction_to_nitrite(dir, sample):
    out_data = {'Assimilatory nitrate reduction to nitrite': 0}
    ko_list = [sample+'_K00367', sample+'_K10534', sample+'_K00372',
               sample+'_K00360']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Assimilatory nitrate reduction to nitrite'] = (
      dir[sample+'_K00367'] +
      dir[sample+'_K10534'] +
      (dir[sample+'_K00372'] +
       dir[sample+'_K00360'])/2)
    return out_data


def Assimilatory_nitrite_reduction_to_ammonia(dir, sample):
    out_data = {'Assimilatory nitrite reduction to ammonia': 0}
    ko_list = [sample+'_K17877', sample+'_K00366']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Assimilatory nitrite reduction to ammonia'] = (
      dir[sample+'_K17877'] +
      dir[sample+'_K00366'])
    return out_data


def Assimilatory_nitrate_reduction_to_ammonia(dir, sample):
    out_data = {'Assimilatory nitrate reduction to ammonia': 0}
    ko_list = [sample+'_K00367', sample+'_K10534', sample+'_K00372',
               sample+'_K00360', sample+'_K17877', sample+'_K00366']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Assimilatory nitrate reduction to ammonia'] = (
      dir[sample+'_K00367'] +
      dir[sample+'_K10534'] +
      (dir[sample+'_K00372'] +
       dir[sample+'_K00360'])/2 +
      dir[sample+'_K17877'] +
      dir[sample+'_K00366'])/2
    return out_data


def Denitrification_NO2_NO(dir, sample):
    out_data = {'Denitrification, NO2 -> NO': 0}
    ko_list = [sample+'_K00368', sample+'_K15864']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Denitrification, NO2 -> NO'] = (
      dir[sample+'_K00368'] +
      dir[sample+'_K15864'])
    return out_data


def Denitrification_NO_N2O(dir, sample):
    out_data = {'Denitrification, NO -> N2O': 0}
    ko_list = [sample+'_K04561', sample+'_K02305']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Denitrification, NO -> N2O'] = (
      dir[sample+'_K04561'] +
      dir[sample+'_K02305'])
    return out_data


def Denitrification_N2O_N2(dir, sample):
    out_data = {'Denitrification, N2O -> N2': 0}
    ko_list = [sample+'_K00376']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Denitrification, N2O -> N2'] = (
      dir[sample+'_K00376'])
    return out_data


def Nitrogen_fixation(dir, sample):
    out_data = {'Nitrogen fixation': 0}
    ko_list = [sample+'_K02586', sample+'_K02591', sample+'_K02588',
               sample+'_K22896', sample+'_K22897', sample+'_K22898',
               sample+'_K22899']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Nitrogen fixation'] = (
        (dir[sample+'_K02586'] +
         dir[sample+'_K02588'] +
         dir[sample+'_K02591'])/3 +
        (dir[sample+'_K22896'] +
         dir[sample+'_K22897'] +
         dir[sample+'_K22898'] +
         dir[sample+'_K22899'])/4)
    return out_data


def Nitrification_ammonia_to_hydroxylamine(dir, sample):
    out_data = {'Nitrification, ammonia -> hydroxylamine (AmoCAB)': 0}
    ko_list = [sample+'_K10944', sample+'_K10945', sample+'_K10946']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Nitrification, ammonia -> hydroxylamine (AmoCAB)'] = (
      dir[sample+'_K10944'] +
      dir[sample+'_K10945'] +
      dir[sample+'_K10946'])/3
    return out_data


def Nitrification_hydroxylamine_to_nitrite(dir, sample):
    out_data = {'Nitrification, hydroxylamine -> nitrite (hao)': 0}
    ko_list = [sample+'_K10535']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Nitrification, hydroxylamine -> nitrite (hao)'] = (
      dir[sample+'_K10535'])
    return out_data


def Nitrification_nitrite_to_nitrate(dir, sample):
    out_data = {'Nitrification, nitrite -> nitrate (nxrAB)': 0}
    ko_list = [sample+'_K00370', sample+'_K00371']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Nitrification, nitrite -> nitrate (nxrAB)'] = (
      dir[sample+'_K00370'] +
      dir[sample+'_K00371'])/2
    return out_data


def Nitrification(dir, sample):
    out_data = {'Nitrification': 0}
    ko_list = [sample+'_K10944', sample+'_K10945', sample+'_K10946',
               sample+'_K10535', sample+'_K00370', sample+'_K00371']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Nitrification'] = (
      (dir[sample+'_K10944'] +
       dir[sample+'_K10945'] +
       dir[sample+'_K10946'])/3 +
      dir[sample+'_K10535'] +
      (dir[sample+'_K00370'] +
       dir[sample+'_K00371'])/2)/3
    return out_data


def Anammox(dir, sample):
    out_data = {'Anammox (anaerobic ammonium oxidation)': 0}
    ko_list = [sample+'_K15864', sample+'_K20932', sample+'_K20933',
               sample+'_K20934', sample+'_K20935']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Anammox (anaerobic ammonium oxidation)'] = (
      dir[sample+'_K15864'] +
      (dir[sample+'_K20932'] +
       dir[sample+'_K20933'] +
       dir[sample+'_K20934'])/3 +
      dir[sample+'_K20935'])/3
    return out_data


def Assimilatory_sulfate_reduction_to_sulfite(dir, sample):
    out_data = {'Assimilatory sulfate reduction to sulfite': 0}
    ko_list = [sample+'_K13811', sample+'_K00958', sample+'_K00860',
               sample+'_K00955', sample+'_K00957', sample+'_K00956', 
               sample+'_K13911']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Assimilatory sulfate reduction to sulfite'] = (
      dir[sample+'_K13811'] +
      (dir[sample+'_K00958'] +
       dir[sample+'_K00860'])/2 +
      (dir[sample+'_K00955'] +
       dir[sample+'_K00957'])/2 +
      (dir[sample+'_K00956'] +
       dir[sample+'_K00957'] +
       dir[sample+'_K00860'])/3 +
      dir[sample+'_K13911'])/2
    return out_data


def Assimilatory_sulfite_reduction_to_sulfide(dir, sample):
    out_data = {'Assimilatory sulfite reduction to sulfide (cysJI, sir)': 0}
    ko_list = [sample+'_K00380', sample+'_K00381', sample+'_K00392']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Assimilatory sulfite reduction to sulfide (cysJI, sir)'] = (
      (dir[sample+'_K00380'] +
       dir[sample+'_K00381'])/2 +
      dir[sample+'_K00392'])
    return out_data


def Dissimilatory_sulfate_reduction_to_sulfite(dir, sample):
    out_data = {'Dissimilatory sulfate reduction to sulfite (reversible)': 0}
    ko_list = [sample+'_K00956', sample+'_K00957', sample+'_K00958',
               sample+'_K00394', sample+'_K00395']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Dissimilatory sulfate reduction to sulfite (reversible)'] = (
      (dir[sample+'_K00956'] +
       dir[sample+'_K00957'])/2 +
      dir[sample+'_K00958'] +
      (dir[sample+'_K00394'] +
       dir[sample+'_K00395'])/2)
    return out_data


def Dissimilatory_sulfite_reduction_to_sulfide(dir, sample):
    out_data = {'Dissimilatory sulfite reduction to sulfide (reversible)': 0}
    ko_list = [sample+'_K11180', sample+'_K11181']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Dissimilatory sulfite reduction to sulfide (reversible)'] = (
      dir[sample+'_K11180'] +
      dir[sample+'_K11181'])/2
    return out_data


def Thiosulfate_oxidation_by_SOX_complex_thiosulfate_sulfate(dir, sample):
    out_data = {'Thiosulfate oxidation by SOX complex, thiosulfate -> sulfate': 0}
    ko_list = [sample+'_K17222', sample+'_K17223', sample+'_K17224',
               sample+'_K17226', sample+'_K17227']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Thiosulfate oxidation by SOX complex, thiosulfate -> sulfate'] = (
      dir[sample+'_K17222'] +
      dir[sample+'_K17223'] +
      dir[sample+'_K17224'] +
      dir[sample+'_K17226'] +
      dir[sample+'_K17227'])/5
    return out_data


def Alternative_thiosulfate_oxidation_doxAD(dir, sample):
    out_data = {'Alternative thiosulfate oxidation (doxAD)': 0}
    ko_list = [sample+'_K16936', sample+'_K16937']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Alternative thiosulfate oxidation (doxAD)'] = (
      dir[sample+'_K16936'] +
      dir[sample+'_K16937'])/2
    return out_data


def Alternative_thiosulfate_oxidation_tsdA(dir, sample):
    out_data = {'Alternative thiosulfate oxidation (tsdA)': 0}
    ko_list = [sample+'_K19713']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Alternative thiosulfate oxidation (tsdA)'] = (
      dir[sample+'_K19713'])
    return out_data


def sulfur_reduction_sulfur_sulfide_sreABC(dir, sample):
    out_data = {'Sulfur reduction, sulfur -> sulfide (sreABC)': 0}
    ko_list = [sample+'_K17219', sample+'_K17220', sample+'_K17221']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Sulfur reduction, sulfur -> sulfide (sreABC)'] = (
      dir[sample+'_K17219'] +
      dir[sample+'_K17220'] +
      dir[sample+'_K17221'])/3
    return out_data


def thiosulfate_disproportionation_thiosulfate_sulfide_sulfite_phsABC(dir, sample):
    out_data = {'Thiosulfate disproportionation, thiosulfate -> sulfide & sulfite (phsABC)': 0}
    ko_list = [sample+'_K08352', sample+'_K08353', sample+'_K08354']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Thiosulfate disproportionation, thiosulfate -> sulfide & sulfite (phsABC)'] = (
      dir[sample+'_K08352'] +
      dir[sample+'_K08353'] +
      dir[sample+'_K08354'])/3
    return out_data


def sulfhydrogenase(dir, sample):
    out_data = {'Sulfhydrogenase, (sulfide)n -> (sulfide)n-1': 0}
    ko_list = [sample+'_K17993', sample+'_K17994', sample+'_K17995',
               sample+'_K17996']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Sulfhydrogenase, (sulfide)n -> (sulfide)n-1'] = (
      dir[sample+'_K17993'] +
      dir[sample+'_K17994'] +
      dir[sample+'_K17995'] +
      dir[sample+'_K17996'])/4
    return out_data


def sulfur_disproportionation_sulfur_sulfide_sulfite(dir, sample):
    out_data = {'Sulfur disproportionation, sulfur -> sulfide & sulfite': 0}
    ko_list = [sample+'_K16952']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Sulfur disproportionation, sulfur -> sulfide & sulfite'] = (
      dir[sample+'_K16952'])
    return out_data


def sulfur_dioxygenase(dir, sample):
    out_data = {'Sulfur dioxygenase': 0}
    ko_list = [sample+'_K17725']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Sulfur dioxygenase'] = (
      dir[sample+'_K17725'])
    return out_data


def sulfite_oxidation_sulfite_sulfate_sor_SUOX_soeABC(dir, sample):
    out_data = {'Sulfite oxidation, sulfite -> sulfate (sorB, SUOX, soeABC)': 0}
    ko_list = [sample+'_K05301', sample+'_K00387', sample+'_K21307',
               sample+'_K21308', sample+'_K21309']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Sulfite oxidation, sulfite -> sulfate (sorB, SUOX, soeABC)'] = (
      dir[sample+'_K05301'] +
      dir[sample+'_K00387'] +
      (dir[sample+'_K21307'] +
       dir[sample+'_K21308'] +
       dir[sample+'_K21309'])/3)
    return out_data


def sulfide_oxidation_sulfide_sulfur_fccAB(dir, sample):
    out_data = {'Sulfide oxidation, sulfide -> sulfur (fccAB)': 0}
    ko_list = [sample+'_K17229', sample+'_K17230']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Sulfide oxidation, sulfide -> sulfur (fccAB)'] = (
      dir[sample+'_K17229'] +
      dir[sample+'_K17230'])/2
    return out_data


def F_type_ATPase(dir, sample):
    out_data = {'F-type ATPase': 0}
    ko_list = [sample+'_K02111', sample+'_K02112',
               sample+'_K02115', sample+'_K02113',
               sample+'_K02114', sample+'_K02108',
               sample+'_K02109', sample+'_K02110']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['F-type ATPase'] = (dir[sample+'_K02111'] +
                                 dir[sample+'_K02112'] +
                                 dir[sample+'_K02115'] +
                                 dir[sample+'_K02113'] +
                                 dir[sample+'_K02114'] +
                                 dir[sample+'_K02108'] +
                                 dir[sample+'_K02109'] +
                                 dir[sample+'_K02110'])/8
    return out_data


def V_type_ATPase(dir, sample):
    out_data = {'V/A-type ATPase': 0}
    ko_list = [sample+'_K02117', sample+'_K02118',
               sample+'_K02119', sample+'_K02120',
               sample+'_K02121', sample+'_K02122',
               sample+'_K02107', sample+'_K02123',
               sample+'_K02124']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['V/A-type ATPase'] = (
        dir[sample+'_K02117'] +
        dir[sample+'_K02118'] +
        dir[sample+'_K02119'] +
        dir[sample+'_K02120'] +
        dir[sample+'_K02121'] +
        dir[sample+'_K02122'] +
        dir[sample+'_K02107'] +
        dir[sample+'_K02123'] +
        dir[sample+'_K02124'])/9
    return out_data


def NADH_quinone_oxidoreductase(dir, sample):
    out_data = {'NADH-quinone oxidoreductase': 0}
    ko_list = [sample+'_K00330', sample+'_K00331', sample+'_K00332',
               sample+'_K00333', sample+'_K00334', sample+'_K00335',
               sample+'_K00336', sample+'_K00337', sample+'_K00338',
               sample+'_K00339', sample+'_K00340', sample+'_K00341',
               sample+'_K00342', sample+'_K00343', sample+'_K13378',
               sample+'_K13380', sample+'_K15863']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['NADH-quinone oxidoreductase'] = (
        dir[sample+'_K00330'] +
        (dir[sample+'_K00331'] +
         dir[sample+'_K00332'] +
         dir[sample+'_K00333'])/3 +
        (dir[sample+'_K00331'] +
         dir[sample+'_K13378'])/2 +
        dir[sample+'_K13380'] +
        dir[sample+'_K00334'] +
        dir[sample+'_K00335'] +
        dir[sample+'_K00336'] +
        dir[sample+'_K00337'] +
        dir[sample+'_K00338'] +
        dir[sample+'_K00339'] +
        dir[sample+'_K00340'] +
        (dir[sample+'_K00341'] +
         dir[sample+'_K00342'])/2 +
        dir[sample+'_K15863'] +
        dir[sample+'_K00343'])/11
    return out_data


def NADPH_quinone_oxidoreductase(dir, sample):
    out_data = {'NAD(P)H-quinone oxidoreductase': 0}
    ko_list = [sample+'_K05574', sample+'_K05582',
               sample+'_K05581', sample+'_K05579',
               sample+'_K05572', sample+'_K05580',
               sample+'_K05578', sample+'_K05576',
               sample+'_K05577', sample+'_K05575',
               sample+'_K05573']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['NAD(P)H-quinone oxidoreductase'] = (
        dir[sample+'_K05574'] +
        dir[sample+'_K05582'] +
        dir[sample+'_K05581'] +
        dir[sample+'_K05579'] +
        dir[sample+'_K05572'] +
        dir[sample+'_K05580'] +
        dir[sample+'_K05578'] +
        dir[sample+'_K05576'] +
        dir[sample+'_K05577'] +
        dir[sample+'_K05575'] +
        dir[sample+'_K05573'])/11
    return out_data


def succinate_dehydrogenase_ubiquinone(dir, sample):
    out_data = {'Succinate dehydrogenase (ubiquinone)': 0}
    ko_list = [sample+'_K00236', sample+'_K00237',
               sample+'_K00234', sample+'_K00235']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Succinate dehydrogenase (ubiquinone)'] = (
        dir[sample+'_K00234'] +
        dir[sample+'_K00235'] +
        dir[sample+'_K00236'] +
        dir[sample+'_K00237'])/4
    return out_data


def Cytochrome_c_oxidase_cbb3_type(dir, sample):
    out_data = {'Cytochrome c oxidase, cbb3-type': 0}
    ko_list = [sample+'_K00404', sample+'_K00405',
               sample+'_K00406', sample+'_K00407',
               sample+'_K15862']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['"Cytochrome c oxidase, cbb3-type"'] = (
        (dir[sample+'_K00404'] +
         dir[sample+'_K00405'])/2 +
        dir[sample+'_K15862'] +
        dir[sample+'_K00406'] +
        dir[sample+'_K00407'])/3
    return out_data


def Cytochrome_bd_ubiquinol_oxidase(dir, sample):
    out_data = {'Cytochrome bd ubiquinol oxidase': 0}
    ko_list = [sample+'_K00425', sample+'_K00426',
               sample+'_K00424', sample+'_K22501']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Cytochrome bd ubiquinol oxidase'] = (
        dir[sample+'_K00425'] +
        dir[sample+'_K00426'] +
        dir[sample+'_K00424'] +
        dir[sample+'_K22501'])/3
    return out_data


def Cytochrome_o_ubiquinol_oxidase(dir, sample):
    out_data = {'Cytochrome o ubiquinol oxidase': 0}
    ko_list = [sample+'_K02300', sample+'_K02299',
               sample+'_K02298', sample+'_K02297']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Cytochrome o ubiquinol oxidase'] = (
      dir[sample+'_K02300'] +
      dir[sample+'_K02299'] +
      dir[sample+'_K02298'] +
      dir[sample+'_K02297'])/4
    return out_data


def Cytochrome_c_oxidase_prokaryotes(dir, sample):
    out_data = {'Cytochrome c oxidase, prokaryotes': 0}
    ko_list = [sample+'_K02274', sample+'_K02275',
               sample+'_K02276', sample+'_K15408']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Cytochrome c oxidase, prokaryotes'] = (
        dir[sample+'_K02275'] +
        (dir[sample+'_K02274'] +
         dir[sample+'_K02276'])/2 +
        dir[sample+'_K15408'])/2
    return out_data


def Cytochrome_aa3_600_menaquinol_oxidase(dir, sample):
    out_data = {'Cytochrome aa3-600 menaquinol oxidase': 0}
    ko_list = [sample+'_K02829', sample+'_K02828',
               sample+'_K02827', sample+'_K02826']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Cytochrome aa3-600 menaquinol oxidase'] = (
        dir[sample+'_K02829'] +
        dir[sample+'_K02828'] +
        dir[sample+'_K02827'] +
        dir[sample+'_K02826'])/4
    return out_data


def cytochrome_bc1_complex(dir, sample):
    out_data = {'Cytochrome bc1 complex': 0}
    ko_list = [sample+'_K00412', sample+'_K00413', sample+'_K00410',
               sample+'_K00411', sample+'_K00414', sample+'_K00415',
               sample+'_K00416', sample+'_K00417', sample+'_K00418',
               sample+'_K00419', sample+'_K00420']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Cytochrome bc1 complex'] = (
        (dir[sample+'_K00412'] +
         dir[sample+'_K00413'])/2 +
        dir[sample+'_K00410'] +
        dir[sample+'_K00411'] +
        dir[sample+'_K00414'] +
        dir[sample+'_K00415'] +
        dir[sample+'_K00416'] +
        dir[sample+'_K00417'] +
        dir[sample+'_K00418'] +
        dir[sample+'_K00419'] +
        dir[sample+'_K00420'])/9
    return out_data


def Phosphate_transporter(dir, sample):
    out_data = {'Phosphate transporter': 0}
    ko_list = [sample+'_K02037', sample+'_K02038',
               sample+'_K02036', sample+'_K02040']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Phosphate transporter'] = (
        dir[sample+'_K02040'] +
        dir[sample+'_K02036'] +
        dir[sample+'_K02037'] +
        dir[sample+'_K02038'])/3
    return out_data


def Phosphonate_transporter(dir, sample):
    out_data = {'Phosphonate transporter': 0}
    ko_list = [sample+'_K02042', sample+'_K02041', sample+'_K02044']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Phosphonate transporter'] = (
        dir[sample+'_K02041'] +
        dir[sample+'_K02042'] +
        dir[sample+'_K02044'])/3
    return out_data


def Thiamin_transporter(dir, sample):
    out_data = {'Thiamin transporter': 0}
    ko_list = [sample+'_K02062', sample+'_K02063',
               sample+'_K02064']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Thiamin transporter'] = (
        dir[sample+'_K02064'] +
        dir[sample+'_K02063'] +
        dir[sample+'_K02062'])/3
    return out_data


def Vitamin_B12_transporter(dir, sample):
    out_data = {'Vitamin B12 transporter': 0}
    ko_list = [sample+'_K06858', sample+'_K06073',
               sample+'_K06074']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Vitamin B12 transporter'] = (
        dir[sample+'_K06074'] +
        dir[sample+'_K06073'] +
        dir[sample+'_K06858'])/3
    return out_data


def Urea_transporter(dir, sample):
    out_data = {'Urea transporter': 0}
    ko_list = [sample+'_K11959', sample+'_K11960',
               sample+'_K11961', sample+'_K11962',
               sample+'_K11963']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Urea transporter'] = (
        dir[sample+'_K11959'] +
        dir[sample+'_K11960'] +
        dir[sample+'_K11961'] +
        dir[sample+'_K11962'] +
        dir[sample+'_K11963'])/5
    return out_data


def Type_I_Secretion(dir, sample):
    out_data = {'Type I Secretion': 0}
    ko_list = [sample+'_K12340', sample+'_K11003',
               sample+'_K11004']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Type I Secretion'] = (
        dir[sample+'_K12340'] +
        dir[sample+'_K11003'] +
        dir[sample+'_K11004'])/3
    return out_data


def Type_III_Secretion(dir, sample):
    out_data = {'Type III Secretion': 0}
    ko_list = [sample+'_K03221', sample+'_K04056',
               sample+'_K04057', sample+'_K04059',
               sample+'_K03219', sample+'_K04058',
               sample+'_K03222', sample+'_K03223',
               sample+'_K03224', sample+'_K03225',
               sample+'_K03226', sample+'_K03227',
               sample+'_K03228', sample+'_K03229',
               sample+'_K03230']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Type III Secretion'] = (
        dir[sample+'_K03221'] +
        dir[sample+'_K04056'] +
        dir[sample+'_K04057'] +
        dir[sample+'_K04058'] +
        dir[sample+'_K04059'] +
        dir[sample+'_K03219'] +
        dir[sample+'_K03222'] +
        dir[sample+'_K03223'] +
        dir[sample+'_K03224'] +
        dir[sample+'_K03225'] +
        dir[sample+'_K03226'] +
        dir[sample+'_K03227'] +
        dir[sample+'_K03228'] +
        dir[sample+'_K03229'] +
        dir[sample+'_K03230'])/15
    return out_data


def Type_II_Secretion(dir, sample):
    out_data = {'Type II Secretion': 0}
    ko_list = [sample+'_K02452', sample+'_K02453',
               sample+'_K02454', sample+'_K02455',
               sample+'_K02456', sample+'_K02457',
               sample+'_K02458', sample+'_K02459',
               sample+'_K02460', sample+'_K02461',
               sample+'_K02462', sample+'_K02464',
               sample+'_K02465']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Type II Secretion'] = (
        dir[sample+'_K02452'] +
        dir[sample+'_K02453'] +
        dir[sample+'_K02454'] +
        dir[sample+'_K02455'] +
        dir[sample+'_K02456'] +
        dir[sample+'_K02457'] +
        dir[sample+'_K02458'] +
        dir[sample+'_K02459'] +
        dir[sample+'_K02460'] +
        dir[sample+'_K02461'] +
        dir[sample+'_K02462'] +
        dir[sample+'_K02464'] +
        dir[sample+'_K02465'])/13
    return out_data


def Type_IV_Secretion(dir, sample):
    out_data = {'Type IV Secretion': 0}
    ko_list = [sample+'_K03194', sample+'_K03195',
               sample+'_K03196', sample+'_K03197',
               sample+'_K03198', sample+'_K03199',
               sample+'_K03200', sample+'_K03201',
               sample+'_K03202', sample+'_K03203',
               sample+'_K03204', sample+'_K03205']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Type IV Secretion'] = (
        dir[sample+'_K03194'] +
        dir[sample+'_K03197'] +
        dir[sample+'_K03198'] +
        dir[sample+'_K03200'] +
        dir[sample+'_K03202'] +
        dir[sample+'_K03204'] +
        dir[sample+'_K03201'] +
        dir[sample+'_K03203'] +
        dir[sample+'_K03195'] +
        dir[sample+'_K03199'] +
        dir[sample+'_K03196'] +
        dir[sample+'_K03205'])/12
    return out_data


def Type_VI_Secretion(dir, sample):
    out_data = {'Type VI Secretion': 0}
    ko_list = [sample+'_K11903', sample+'_K11904',
               sample+'_K11906', sample+'_K11907',
               sample+'_K11891', sample+'_K11892',
               sample+'_K11912', sample+'_K11913',
               sample+'_K11915']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Type VI Secretion'] = (
        dir[sample+'_K11904'] +
        dir[sample+'_K11903'] +
        dir[sample+'_K11906'] +
        dir[sample+'_K11891'] +
        dir[sample+'_K11892'] +
        dir[sample+'_K11907'] +
        dir[sample+'_K11912'] +
        dir[sample+'_K11913'] +
        dir[sample+'_K11915'])/9
    return out_data


def Sec_SRP(dir, sample):
    out_data = {'Sec-SRP': 0}
    ko_list = [sample+'_K03072', sample+'_K03074', sample+'_K12257',
               sample+'_K03073', sample+'_K03075', sample+'_K03076',
               sample+'_K03210', sample+'_K03217', sample+'_K03070',
               sample+'_K13301', sample+'_K03110', sample+'_K03071',
               sample+'_K03106']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Sec-SRP'] = (
        dir[sample+'_K03072'] +
        dir[sample+'_K03074'] +
        dir[sample+'_K12257'] +
        dir[sample+'_K03073'] +
        dir[sample+'_K03075'] +
        dir[sample+'_K03076'] +
        dir[sample+'_K03210'] +
        dir[sample+'_K03217'] +
        dir[sample+'_K03070'] +
        dir[sample+'_K13301'] +
        dir[sample+'_K03110'] +
        dir[sample+'_K03071'] +
        dir[sample+'_K03106'])/13
    return out_data


def Twin_arginine_targeting(dir, sample):
    out_data = {'Twin arginine targeting': 0}
    ko_list = [sample+'_K03116', sample+'_K03117',
               sample+'_K03118', sample+'_K03425']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Twin arginine targeting'] = (
        dir[sample+'_K03116'] +
        dir[sample+'_K03117'] +
        dir[sample+'_K03118'] +
        dir[sample+'_K03425'])/4
    return out_data


def Type_Vabc_secretion(dir, sample):
    out_data = {'Type Vabc secretion': 0}
    ko_list = [sample+'_K11016', sample+'_K11017',
               sample+'_K11028', sample+'_K12341',
               sample+'_K12342']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Type Vabc secretion'] = (
        dir[sample+'_K11028'] +
        (dir[sample+'_K11017'] +
         dir[sample+'_K11016'])/2 +
        (dir[sample+'_K12341'] +
         dir[sample+'_K12342'])/2)
    return out_data


def Bacterial_chemotaxis(dir, sample):
    out_data = {'Bacterial chemotaxis': 0}
    ko_list = [sample+'_K03406', sample+'_K05874', sample+'_K05875',
               sample+'_K05876', sample+'_K05877', sample+'_K03776',
               sample+'_K10108', sample+'_K10439', sample+'_K10540',
               sample+'_K12368', sample+'_K03407', sample+'_K03408',
               sample+'_K03413', sample+'_K03410', sample+'_K03414',
               sample+'_K03409', sample+'_K03412', sample+'_K13924',
               sample+'_K03415', sample+'_K03411', sample+'_K00575',
               sample+'_K02410', sample+'_K02416', sample+'_K02417',
               sample+'_K02556', sample+'_K02557']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Bacterial chemotaxis'] = (
      dir[sample+'_K03406'] +
      dir[sample+'_K05874'] +
      dir[sample+'_K05875'] +
      dir[sample+'_K05876'] +
      dir[sample+'_K05877'] +
      dir[sample+'_K03776'] +
      dir[sample+'_K10108'] +
      dir[sample+'_K10439'] +
      dir[sample+'_K10540'] +
      dir[sample+'_K12368'] +
      dir[sample+'_K03407'] +
      dir[sample+'_K03408'] +
      dir[sample+'_K03413'] +
      dir[sample+'_K03410'] +
      dir[sample+'_K03414'] +
      dir[sample+'_K03409'] +
      dir[sample+'_K03412'] +
      dir[sample+'_K13924'] +
      dir[sample+'_K03415'] +
      dir[sample+'_K03411'] +
      dir[sample+'_K00575'] +
      dir[sample+'_K02410'] +
      dir[sample+'_K02416'] +
      dir[sample+'_K02417'] +
      dir[sample+'_K02556'] +
      dir[sample+'_K02557'])/26
    return out_data


def Flagellum_assembly(dir, sample):
    out_data = {'Flagellum assembly': 0}
    ko_list = [sample+'_K02402', sample+'_K02403', sample+'_K02398',
               sample+'_K02405', sample+'_K02406', sample+'_K02407',
               sample+'_K02397', sample+'_K02396', sample+'_K02414',
               sample+'_K02389', sample+'_K02390', sample+'_K02391',
               sample+'_K02392', sample+'_K02393', sample+'_K02394',
               sample+'_K02387', sample+'_K02388', sample+'_K02408',
               sample+'_K02409', sample+'_K02410', sample+'_K02416',
               sample+'_K02417', sample+'_K02400', sample+'_K02401',
               sample+'_K02411', sample+'_K02412', sample+'_K02418',
               sample+'_K02419', sample+'_K02420', sample+'_K02421',
               sample+'_K13820', sample+'_K02556', sample+'_K02557',
               sample+'_K21217', sample+'_K21218', sample+'_K02399',
               sample+'_K02413', sample+'_K02422', sample+'_K02423',
               sample+'_K02386']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Flagellum assembly'] = (
      dir[sample+'_K02402'] +
      dir[sample+'_K02403'] +
      dir[sample+'_K02398'] +
      dir[sample+'_K02405'] +
      dir[sample+'_K02406'] +
      dir[sample+'_K02407'] +
      dir[sample+'_K02397'] +
      dir[sample+'_K02396'] +
      dir[sample+'_K02414'] +
      dir[sample+'_K02389'] +
      dir[sample+'_K02390'] +
      dir[sample+'_K02391'] +
      dir[sample+'_K02392'] +
      dir[sample+'_K02393'] +
      dir[sample+'_K02394'] +
      dir[sample+'_K02387'] +
      dir[sample+'_K02388'] +
      dir[sample+'_K02408'] +
      dir[sample+'_K02409'] +
      dir[sample+'_K02410'] +
      dir[sample+'_K02416'] +
      dir[sample+'_K02417'] +
      dir[sample+'_K02400'] +
      dir[sample+'_K02401'] +
      dir[sample+'_K02411'] +
      dir[sample+'_K02412'] +
      dir[sample+'_K02418'] +
      dir[sample+'_K02419'] +
      dir[sample+'_K02420'] +
      dir[sample+'_K02421'] +
      dir[sample+'_K13820'] +
      dir[sample+'_K02556'] +
      dir[sample+'_K02557'] +
      dir[sample+'_K21217'] +
      dir[sample+'_K21218'] +
      dir[sample+'_K02399'] +
      dir[sample+'_K02413'] +
      dir[sample+'_K02422'] +
      dir[sample+'_K02423'] +
      dir[sample+'_K02386'])/40
    return out_data


def Dissimilatory_arsenic_reduction(dir, sample):
    out_data = {'Dissimilatory arsenic reduction': 0}
    ko_list = [sample+'_K00537', sample+'_K03741',
               sample+'_K18701', sample+'_K03325',
               sample+'_K03893', sample+'_K03892',
               sample+'_K01551']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Dissimilatory arsenic reduction'] = (
      dir[sample+'_K00537'] +
      dir[sample+'_K03741'] +
      dir[sample+'_K18701'] +
      dir[sample+'_K03325'] +
      dir[sample+'_K03893'] +
      dir[sample+'_K03892'] +
      dir[sample+'_K01551'])/4
    return out_data


relative_abundance = {}
genome_data = []
for line in open(str(arg_dict['Input']), "r"):
    print(line)
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

for key, value in relative_abundance.items():
    print("\nKey: " + key)
    print("\nValue: " + str(value))

function_order = ['Photosystem II',
                  'Photosystem I',
                  'Cytochrome b6/f complex',
                  'Anoxygenic photosystem II (pufML)',
                  'Anoxygenic photosystem I (pscABCD)',
                  'RuBisCo',
                  'CBB Cycle',
                  'rTCA Cycle',
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
                  'bifunctional chitinase/lysozyme',
                  'beta-N-acetylhexosaminidase',
                  'D-galacturonate isomerase',
                  'alpha-amylase',
                  'beta-glucosidase',
                  'pullulanase',
                  'glycolysis',
                  'Entner-Doudoroff pathway, glucose-6P -> glyceraldehyde-3P + pyruvate',
                  'gluconeogenesis, oxaloacetate -> fructose-6P',
                  'TCA Cycle',
                  'Methanogenesis, methanol -> methane',
                  'Methanogenesis, methylamine -> methane',
                  'Methanogenesis, dimethylamine -> methane',
                  'Methanogenesis, trimethylamine -> methane',
                  'Methanogenesis, trimethylamine -> methane',
                  'Methanogenesis, acetate -> methane',
                  'Methanogenesis, CO2 -> methane',
                  'Methane oxidation, methanol -> Formaldehyde',
                  'Methane oxidation, methanol -> Formaldehyde',
                  'Mixed acid: lactate (pyruvate -> lactate)',
                  'Mixed acid: formate (pyruvate -> formate)',
                  'Mixed acid: Formate -> CO2 & H2',
                  'Mixed acid: acetate',
                  'Mixed acid: ethanol, acetate to acetylaldehyde',
                  'Mixed acid: ethanol, acetyl-CoA to acetylaldehyde (reversible)',
                  'Mixed acid: ethanol, acetylaldehyde to ethanol',
                  'Mixed acid: succinate (phosphoenolpyruvate to succinate via oxaloacetate, malate & fumarate)',
                  'Mixed acid: ethanol, acetyl-CoA to acetylaldehyde (reversible)',
                  'Anaplerotic genes (pyruvate -> oxaloacetate)',
                  'Dissimilatory nitrate reduction to nitrite',
                  'Dissimilatory nitrite reduction to ammonia',
                  'DNRA',
                  'Assimilatory nitrate reduction to nitrite',
                  'Assimilatory nitrite reduction to ammonia',
                  'Assimilatory nitrate reduction to ammonia',
                  'Denitrification, NO2 -> NO',
                  'Denitrification, NO -> N2O',
                  'Denitrification, N2O -> N2',
                  'Nitrogen fixation',
                  'Nitrification, ammonia -> hydroxylamine (AmoCAB)',
                  'Nitrification, hydroxylamine -> nitrite (hao)',
                  'Nitrification, nitrite -> nitrate (nxrAB)',
                  'Nitrification',
                  'Anammox (anaerobic ammonium oxidation)',
                  'Assimilatory sulfate reduction to sulfite',
                  'Assimilatory sulfite reduction to sulfide (cysJI, sir)',
                  'Dissimilatory sulfate reduction to sulfite (reversible)',
                  'Dissimilatory sulfite reduction to sulfide (reversible)',
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
                  'F-type ATPase',
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


filehandle = str(arg_dict['Output'])
out_file = open(filehandle, "w")
out_file.write('Function'+"\t"+str("\t".join(function_order))+"\n")


for k in genome_data:
    # print(k)
    # print(reverse_tca(relative_abundance, k))
    pathway_data = {}
    pathway_data.update(Photosystem_II(relative_abundance, k))
    pathway_data.update(Photosystem_I(relative_abundance, k))
    pathway_data.update(Cytochrome_b6_f_complex(relative_abundance, k))
    pathway_data.update(anoxygenic_photosystem_II_pufML(relative_abundance, k))
    pathway_data.update(anoxygenic_photosystem_I_pscABCD(relative_abundance, k))
    pathway_data.update(RuBisCo(relative_abundance, k))
    pathway_data.update(CBB_Cycle(relative_abundance, k))
    pathway_data.update(rTCA_Cycle(relative_abundance, k))
    pathway_data.update(Wood_Ljungdahl(relative_abundance, k))
    pathway_data.update(three_Hydroxypropionate_Bicycle(relative_abundance, k))
    pathway_data.update(Dicarboxylate_hydroxybutyrate_cycle(relative_abundance, k))
    pathway_data.update(pectinesterase(relative_abundance, k))
    pathway_data.update(diacetylchitobiose_deacetylase(relative_abundance, k))
    pathway_data.update(glucoamylase(relative_abundance, k))
    pathway_data.update(D_galacturonate_epimerase(relative_abundance, k))
    pathway_data.update(exo_poly_alpha_galacturonosidase(relative_abundance, k))
    pathway_data.update(oligogalacturonide_lyase(relative_abundance, k))
    pathway_data.update(cellulase(relative_abundance, k))
    pathway_data.update(exopolygalacturonase(relative_abundance, k))
    pathway_data.update(chitinase(relative_abundance, k))
    pathway_data.update(basic_endochitinase_B(relative_abundance, k))
    pathway_data.update(bifunctional_chitinase_or_lysozyme(relative_abundance, k))
    pathway_data.update(beta_N_acetylhexosaminidase(relative_abundance, k))
    pathway_data.update(D_galacturonate_isomerase(relative_abundance, k))
    pathway_data.update(alpha_amylase(relative_abundance, k))
    pathway_data.update(beta_glucosidase(relative_abundance, k))
    pathway_data.update(pullulanase(relative_abundance, k))
    pathway_data.update(glycolysis(relative_abundance, k))
    pathway_data.update(Entner_Doudoroff_Pathway(relative_abundance, k))
    pathway_data.update(gluconeogenesis(relative_abundance, k))
    pathway_data.update(tca_cycle(relative_abundance, k))
    pathway_data.update(Methanogenesis_via_methanol(relative_abundance, k))
    pathway_data.update(Methanogenesis_via_methylamine(relative_abundance, k))
    pathway_data.update(Methanogenesis_via_dimethylamine(relative_abundance, k))
    pathway_data.update(Methanogenesis_via_trimethylamine(relative_abundance, k))
    pathway_data.update(Methanogenesis_via_acetate(relative_abundance, k))
    pathway_data.update(Methanogenesis_CO2_methane(relative_abundance, k))
    pathway_data.update(Methane_oxidation_methane_methanol(relative_abundance, k))
    pathway_data.update(Methane_oxidation_methanol_Formaldehyde(relative_abundance, k))
    pathway_data.update(Mixed_acid_lactate(relative_abundance, k))
    pathway_data.update(Mixed_acid_formate(relative_abundance, k))
    pathway_data.update(Mixed_acid_Formate_to_CO2_H2(relative_abundance, k))
    pathway_data.update(Mixed_acid_acetate(relative_abundance, k))
    pathway_data.update(Mixed_acid_Ethanol_Acetate_to_Acetylaldehyde(relative_abundance, k))
    pathway_data.update(Mixed_acid_Ethanol_Acetyl_CoA_to_Acetylaldehyde(relative_abundance, k))
    pathway_data.update(Mixed_acid_Ethanol_Acetylaldehyde_to_Ethanol(relative_abundance, k))
    pathway_data.update(Mixed_acid_succinate(relative_abundance, k))
    pathway_data.update(Glyoxylate_shunt(relative_abundance, k))
    pathway_data.update(Anaplerotic_genes(relative_abundance, k))
    pathway_data.update(Dissimilatory_nitrate_reduction_to_nitrite(relative_abundance, k))
    pathway_data.update(Dissimilatory_nitrite_reduction_to_ammonia(relative_abundance, k))
    pathway_data.update(DNRA(relative_abundance, k))
    pathway_data.update(Assimilatory_nitrate_reduction_to_nitrite(relative_abundance, k))
    pathway_data.update(Assimilatory_nitrite_reduction_to_ammonia(relative_abundance, k))
    pathway_data.update(Assimilatory_nitrate_reduction_to_ammonia(relative_abundance, k))
    pathway_data.update(Denitrification_NO2_NO(relative_abundance, k))
    pathway_data.update(Denitrification_NO_N2O(relative_abundance, k))
    pathway_data.update(Denitrification_N2O_N2(relative_abundance, k))
    pathway_data.update(Nitrogen_fixation(relative_abundance, k))
    pathway_data.update(Nitrification_ammonia_to_hydroxylamine(relative_abundance, k))
    pathway_data.update(Nitrification_hydroxylamine_to_nitrite(relative_abundance, k))
    pathway_data.update(Nitrification_nitrite_to_nitrate(relative_abundance, k))
    pathway_data.update(Nitrification(relative_abundance, k))
    pathway_data.update(Anammox(relative_abundance, k))
    pathway_data.update(Assimilatory_sulfate_reduction_to_sulfite(relative_abundance, k))
    pathway_data.update(Assimilatory_sulfite_reduction_to_sulfide(relative_abundance, k))
    pathway_data.update(Dissimilatory_sulfate_reduction_to_sulfite(relative_abundance, k))
    pathway_data.update(Dissimilatory_sulfite_reduction_to_sulfide(relative_abundance, k))
    pathway_data.update(Thiosulfate_oxidation_by_SOX_complex_thiosulfate_sulfate(relative_abundance, k))
    pathway_data.update(Alternative_thiosulfate_oxidation_doxAD(relative_abundance, k))
    pathway_data.update(Alternative_thiosulfate_oxidation_tsdA(relative_abundance, k))
    pathway_data.update(sulfur_reduction_sulfur_sulfide_sreABC(relative_abundance, k))
    pathway_data.update(thiosulfate_disproportionation_thiosulfate_sulfide_sulfite_phsABC(relative_abundance, k))
    pathway_data.update(sulfhydrogenase(relative_abundance, k))
    pathway_data.update(sulfur_disproportionation_sulfur_sulfide_sulfite(relative_abundance, k))
    pathway_data.update(sulfur_dioxygenase(relative_abundance, k))
    pathway_data.update(sulfite_oxidation_sulfite_sulfate_sor_SUOX_soeABC(relative_abundance, k))
    pathway_data.update(sulfide_oxidation_sulfide_sulfur_fccAB(relative_abundance, k))
    pathway_data.update(F_type_ATPase(relative_abundance, k))
    pathway_data.update(V_type_ATPase(relative_abundance, k))
    pathway_data.update(NADH_quinone_oxidoreductase(relative_abundance, k))
    pathway_data.update(NADPH_quinone_oxidoreductase(relative_abundance, k))
    pathway_data.update(succinate_dehydrogenase_ubiquinone(relative_abundance, k))
    pathway_data.update(Cytochrome_c_oxidase_cbb3_type(relative_abundance, k))
    pathway_data.update(Cytochrome_bd_ubiquinol_oxidase(relative_abundance, k))
    pathway_data.update(Cytochrome_o_ubiquinol_oxidase(relative_abundance, k))
    pathway_data.update(Cytochrome_c_oxidase_prokaryotes(relative_abundance, k))
    pathway_data.update(Cytochrome_aa3_600_menaquinol_oxidase(relative_abundance, k))
    pathway_data.update(cytochrome_bc1_complex(relative_abundance, k))
    pathway_data.update(Phosphate_transporter(relative_abundance, k))
    pathway_data.update(Phosphonate_transporter(relative_abundance, k))
    pathway_data.update(Thiamin_transporter(relative_abundance, k))
    pathway_data.update(Vitamin_B12_transporter(relative_abundance, k))
    pathway_data.update(Urea_transporter(relative_abundance, k))
    pathway_data.update(Type_I_Secretion(relative_abundance, k))
    pathway_data.update(Type_III_Secretion(relative_abundance, k))
    pathway_data.update(Type_II_Secretion(relative_abundance, k))
    pathway_data.update(Type_IV_Secretion(relative_abundance, k))
    pathway_data.update(Type_VI_Secretion(relative_abundance, k))
    pathway_data.update(Sec_SRP(relative_abundance, k))
    pathway_data.update(Twin_arginine_targeting(relative_abundance, k))
    pathway_data.update(Type_Vabc_secretion(relative_abundance, k))
    pathway_data.update(Bacterial_chemotaxis(relative_abundance, k))
    pathway_data.update(Flagellum_assembly(relative_abundance, k))
    pathway_data.update(Dissimilatory_arsenic_reduction(relative_abundance, k))
    

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

# heatmap
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

file_in = open(filehandle, "r")
table = pd.read_table(file_in, index_col=0)
flatui = ["white", "red", "yellow", "#2F4F4F", "blue", "#4B0082", "#800000"]
cmap = sns.palplot(sns.color_palette(flatui))
ax = sns.heatmap(table, cmap=cmap)
fig = ax.get_figure()
fig.savefig("function_heatmap.svg")
