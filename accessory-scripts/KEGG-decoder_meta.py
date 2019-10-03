#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import argparse
import matplotlib
matplotlib.use('Agg')

parser = argparse.ArgumentParser(
    description="Accepts KEGG KOALA text file as input and \
    produces function list and heatmap figure.")
parser.add_argument('Input', help="Input KOALA file. See documentation for correct format")
parser.add_argument('Output', help="List version of the final heat map figure")
args = parser.parse_args()
arg_dict = vars(args)


def glycolysis(dir, sample):
    out_data = {'glycolysis': 0}
    ko_list = [sample+'_K01835', sample+'_K01810', sample+'_K01623',
               sample+'_K00927', sample+'_K01689', sample+'_K00850',
               sample+'_K00895', sample+'_K00134', sample+'_K00150',
               sample+'_K01834', sample+'_K15633', sample+'_K00873',
               sample+'_K01006']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['glycolysis'] = (dir[sample+'_K01835']+dir[sample+'_K01810'] +
                              dir[sample+'_K01623']+dir[sample+'_K00927'] +
                              dir[sample+'_K01689']+dir[sample+'_K00850'] +
                              dir[sample+'_K00895']+dir[sample+'_K00134'] +
                              dir[sample+'_K00150']+dir[sample+'_K01834'] +
                              dir[sample+'_K15633']+dir[sample+'_K00873'] +
                              dir[sample+'_K01006'])/9
    return out_data


def gluconeogenesis(dir, sample):
    out_data = {'gluconeogenesis': 0}
    ko_list = [sample+'_K03841', sample+'_K01835', sample+'_K01810',
               sample+'_K01623', sample+'_K00927', sample+'_K01689',
               sample+'_K00134', sample+'_K00150', sample+'_K01834',
               sample+'_K15633', sample+'_K00873', sample+'_K01006']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['gluconeogenesis'] = (dir[sample+'_K03841'] +
                                   dir[sample+'_K01835'] +
                                   dir[sample+'_K01810'] +
                                   dir[sample+'_K01623'] +
                                   dir[sample+'_K00927'] +
                                   dir[sample+'_K01689'] +
                                   dir[sample+'_K00134'] +
                                   dir[sample+'_K00150'] +
                                   dir[sample+'_K01834'] +
                                   dir[sample+'_K15633'] +
                                   dir[sample+'_K00873'] +
                                   dir[sample+'_K01006'])/9
    return out_data


def tca_cycle(dir, sample):
    out_data = {'TCA Cycle': 0}
    ko_list = [sample+'_K01681', sample+'_K01682',
               sample+'_K00031', sample+'_K00030',
               sample+'_K17753', sample+'_K00174',
               sample+'_K00175', sample+'_K01899',
               sample+'_K01900', sample+'_K01902',
               sample+'_K01903', sample+'_K18118',
               sample+'_K00244', sample+'_K00245',
               sample+'_K00246', sample+'_K00247',
               sample+'_K00239', sample+'_K00240',
               sample+'_K00241', sample+'_K00242',
               sample+'_K00234', sample+'_K00235',
               sample+'_K00236', sample+'_K00237',
               sample+'_K01677', sample+'_K01678',
               sample+'_K01679', sample+'_K01676',
               sample+'_K00116', sample+'_K00025',
               sample+'_K00026', sample+'_K00024',
               sample+'_K01647']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['TCA Cycle'] = (
        (dir[sample+'_K01681'] +
         dir[sample+'_K01682']) +
        (dir[sample+'_K00031'] +
         dir[sample+'_K00030'] +
         dir[sample+'_K17753']) +
        (dir[sample+'_K00174'] +
         dir[sample+'_K00175'])/2 +
        ((dir[sample+'_K01899'] +
          dir[sample+'_K01900'])/2 +
         (dir[sample+'_K01902'] +
          dir[sample+'_K01903'])/2 +
         dir[sample+'_K18118']) +
        ((dir[sample+'_K00244'] +
          dir[sample+'_K00245'] +
          dir[sample+'_K00246'] +
          dir[sample+'_K00247'])/4 +
         (dir[sample+'_K00239'] +
          dir[sample+'_K00240'] +
          dir[sample+'_K00241'] +
          dir[sample+'_K00242'])/4 +
         (dir[sample+'_K00234'] +
          dir[sample+'_K00235'] +
          dir[sample+'_K00236'] +
          dir[sample+'_K00237'])/4) +
        ((dir[sample+'_K01677'] +
          dir[sample+'_K01678'] +
          dir[sample+'_K01679'])/3 +
         dir[sample+'_K01676']) +
        (dir[sample+'_K00116'] +
         dir[sample+'_K00025'] +
         dir[sample+'_K00026'] +
         dir[sample+'_K00024']) +
        dir[sample+'_K01647'])/8
    return out_data


def NADPH_quinone_oxidoreductase(dir, sample):
    out_data = {'NAD(P)H-quinone oxidoreductase': 0}
    ko_list = [sample+'_K05574', sample+'_K05582',
               sample+'_K05581', sample+'_K05579',
               sample+'_K05572', sample+'_K05580',
               sample+'_K05578', sample+'_K05576',
               sample+'_K05577', sample+'_K05575',
               sample+'_K05573', sample+'_K05583',
               sample+'_K05584', sample+'_K05585']
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
        dir[sample+'_K05573'] +
        dir[sample+'_K05583'] +
        dir[sample+'_K05584'] +
        dir[sample+'_K05585'])/14
    return out_data


def NADH_quinone_oxidoreductase(dir, sample):
    out_data = {'NADH-quinone oxidoreductase': 0}
    ko_list = [sample+'_K00330', sample+'_K00331', sample+'_K00332',
               sample+'_K00333', sample+'_K00334', sample+'_K00335',
               sample+'_K00336', sample+'_K00337', sample+'_K00338',
               sample+'_K00339', sample+'_K00340', sample+'_K00341',
               sample+'_K00342', sample+'_K00343']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['NADH-quinone oxidoreductase'] = (dir[sample+'_K00330'] +
                                               dir[sample+'_K00331'] +
                                               dir[sample+'_K00332'] +
                                               dir[sample+'_K00333'] +
                                               dir[sample+'_K00334'] +
                                               dir[sample+'_K00335'] +
                                               dir[sample+'_K00336'] +
                                               dir[sample+'_K00337'] +
                                               dir[sample+'_K00338'] +
                                               dir[sample+'_K00339'] +
                                               dir[sample+'_K00340'] +
                                               dir[sample+'_K00341'] +
                                               dir[sample+'_K00342'] +
                                               dir[sample+'_K00343'])/14
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
    out_data = {'V-type ATPase': 0}
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
    out_data['V-type ATPase'] = (dir[sample+'_K02117'] +
                                 dir[sample+'_K02118'] +
                                 dir[sample+'_K02119'] +
                                 dir[sample+'_K02120'] +
                                 dir[sample+'_K02121'] +
                                 dir[sample+'_K02122'] +
                                 dir[sample+'_K02107'] +
                                 dir[sample+'_K02123'] +
                                 dir[sample+'_K02124'])/9
    return out_data


def Cytochrome_c_oxidase(dir, sample):
    out_data = {'Cytochrome c oxidase': 0}
    ko_list = [sample+'_K02274', sample+'_K02275',
               sample+'_K02276', sample+'_K02277']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Cytochrome c oxidase'] = (dir[sample+'_K02274'] +
                                        dir[sample+'_K02275'] +
                                        dir[sample+'_K02276'] +
                                        dir[sample+'_K02277'])/4
    return out_data


def Ubiquinol_cytochrome_c_reductase(dir, sample):
    out_data = {'Ubiquinol-cytochrome c reductase': 0}
    ko_list = [sample+'_K00411', sample+'_K00410']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Ubiquinol-cytochrome c reductase'] = (dir[sample+'_K00411'] +
                                                    dir[sample+'_K00410'])/2
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
    out_data['Cytochrome o ubiquinol oxidase'] = (dir[sample+'_K02300'] +
                                                  dir[sample+'_K02299'] +
                                                  dir[sample+'_K02298'] +
                                                  dir[sample+'_K02297'])/4
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


def Cytochrome_c_oxidase_cbb3_type(dir, sample):
    out_data = {'Cytochrome c oxidase, cbb3-type': 0}
    ko_list = [sample+'_K00404', sample+'_K00405',
               sample+'_K00406', sample+'_K00407']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['"Cytochrome c oxidase, cbb3-type"'] = (
        dir[sample+'_K00404'] +
        dir[sample+'_K00405'] +
        dir[sample+'_K00406'] +
        dir[sample+'_K00407'])/4
    return out_data


def Cytochrome_bd_complex(dir, sample):
    out_data = {'Cytochrome bd complex': 0}
    ko_list = [sample+'_K00425', sample+'_K00426']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Cytochrome bd complex'] = (
        dir[sample+'_K00425'] +
        dir[sample+'_K00426'])/2
    return out_data


def RuBisCo(dir, sample):
    out_data = {'RuBisCo': 0}
    ko_list = [sample+'_K01601', sample+'_K01602']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['RuBisCo'] = (dir[sample+'_K01601'] +
                           dir[sample+'_K01602'])/2
    return out_data


def CBB_Cycle(dir, sample):
    out_data = {'CBB Cycle': 0}
    ko_list = [sample+'_K01601', sample+'_K01602',
               sample+'_K00927', sample+'_K00134',
               sample+'_K05298', sample+'_K00150',
               sample+'_K00855', sample+'_K01783',
               sample+'_K01621', sample+'_K00615',
               sample+'_K01783', sample+'_K00615',
               sample+'_K01807', sample+'_K01623',
               sample+'_K01624', sample+'_K11645',
               sample+'_K00615', sample+'_K11532',
               sample+'_K03841', sample+'_K02446']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['CBB Cycle'] = (
        (dir[sample+'_K01601'] +
         dir[sample+'_K01602'])/2 +
        dir[sample+'_K00927'] +
        (dir[sample+'_K00134'] +
         dir[sample+'_K05298'] +
         dir[sample+'_K00150']) +
        dir[sample+'_K00855'] +
        (dir[sample+'_K01783'] +
         dir[sample+'_K01621']) +
        (dir[sample+'_K00615'] +
         dir[sample+'_K01783']) +
        (dir[sample+'_K00615'] +
         dir[sample+'_K01807']) +
        ((dir[sample+'_K01623'] +
          dir[sample+'_K01624'] +
          dir[sample+'_K11645']) +
         dir[sample+'_K00615'] +
         (dir[sample+'_K11532'] +
             dir[sample+'_K03841'] +
             dir[sample+'_K02446'])))/13
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
        (dir[sample+'_K15232'] +
            dir[sample+'_K15233'] +
            dir[sample+'_K15234'])/3)
    return out_data


def Wood_Ljungdahl(dir, sample):
    out_data = {'Wood-Ljungdahl': 0}
    ko_list = [sample+'_K00192', sample+'_K14138',
               sample+'_K00198', sample+'_K03520',
               sample+'_K05299', sample+'_K15022',
               sample+'_K01938', sample+'_K01491',
               sample+'_K00297']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Wood-Ljungdahl'] = (
        (dir[sample+'_K00192'] +
            dir[sample+'_K14138']) +
        (dir[sample+'_K00198'] +
            dir[sample+'_K03520']) +
        (dir[sample+'_K05299'] +
            dir[sample+'_K15022'])/2 +
        dir[sample+'_K01938'] +
        dir[sample+'_K01491'] +
        dir[sample+'_K00297'])/6
    return out_data


def three_Hydroxypropionate_Bicycle(dir, sample):
    out_data = {'3-Hydroxypropionate Bicycle': 0}
    ko_list = [sample+'_K00169', sample+'_K00170',
               sample+'_K01006', sample+'_K01007',
               sample+'_K01595', sample+'_K00024',
               sample+'_K14471', sample+'_K14472',
               sample+'_K08691', sample+'_K02160',
               sample+'_K01961', sample+'_K01962',
               sample+'_K01963', sample+'_K14468',
               sample+'_K15017', sample+'_K15039',
               sample+'_K14469', sample+'_K15018',
               sample+'_K15019', sample+'_K15020',
               sample+'_K08691', sample+'_K14449',
               sample+'_K14470', sample+'_K09709',
               sample+'_K08691']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['3-Hydroxypropionate Bicycle'] = (
        (dir[sample+'_K00169'] +
            dir[sample+'_K00170'])/2 +
        (dir[sample+'_K01006'] +
            dir[sample+'_K01007']) +
        dir[sample+'_K01595'] +
        dir[sample+'_K00024'] +
        (dir[sample+'_K14471'] +
            dir[sample+'_K14472'])/2 +
        dir[sample+'_K08691'] +
        (dir[sample+'_K02160'] +
            dir[sample+'_K01961'] +
            dir[sample+'_K01962'] +
            dir[sample+'_K01963'])/4 +
        (dir[sample+'_K14468'] +
            dir[sample+'_K15017'])/2 +
        dir[sample+'_K15039'] +
        (dir[sample+'_K14469'] +
            dir[sample+'_K15018'])/2 +
        dir[sample+'_K15019'] +
        dir[sample+'_K15020'] +
        dir[sample+'_K08691'] +
        dir[sample+'_K14449'] +
        dir[sample+'_K14470'] +
        dir[sample+'_K09709'] +
        dir[sample+'_K08691'])/17
    return out_data


def four_Hydroxybutyrate_or_three_hydroxypropionate(dir, sample):
    out_data = {'4-Hydroxybutyrate/3-hydroxypropionate': 0}
    ko_list = [sample+'_K02160', sample+'_K01961',
               sample+'_K01962', sample+'_K01963',
               sample+'_K18602', sample+'_K18594',
               sample+'_K14469', sample+'_K15019',
               sample+'_K05606', sample+'_K01847',
               sample+'_K01848', sample+'_K01849',
               sample+'_K18593', sample+'_K14534',
               sample+'_K15016', sample+'_K00626']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['4-Hydroxybutyrate/3-hydroxypropionate'] = (
        (dir[sample+'_K02160'] +
            dir[sample+'_K01961'] +
            dir[sample+'_K01962'] +
            dir[sample+'_K01963'])/4 +
        dir[sample+'_K18602'] +
        dir[sample+'_K18594'] +
        (dir[sample+'_K14469'] +
            dir[sample+'_K15019'])/2 +
        dir[sample+'_K05606'] +
        (dir[sample+'_K01847'] +
            dir[sample+'_K01848'] +
            dir[sample+'_K01849'])/3 +
        dir[sample+'_K18593'] +
        dir[sample+'_K14534'] +
        dir[sample+'_K15016'] +
        dir[sample+'_K00626'])/10
    return out_data


def pectinesterase(dir, sample):
    out_data = {'pectinesterase': 0}
    ko_list = [sample+'_K01051']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['pectinesterase'] = dir[sample+'_K01051']
    return out_data


def diacetylchitobiose_deacetylase(dir, sample):
    out_data = {'diacetylchitobiose deacetylase': 0}
    ko_list = [sample+'_K18454', sample+'_K03478']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['diacetylchitobiose deacetylase'] = (dir[sample+'_K18454'] +
                                                  dir[sample+'_K03478'])
    return out_data


def glucoamylase(dir, sample):
    out_data = {'glucoamylase': 0}
    ko_list = [sample+'_K01178']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['glucoamylase'] = dir[sample+'_K01178']
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
    out_data = {'oligogalacturonide lyase': 0}
    ko_list = [sample+'_K01730']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['oligogalacturonide lyase'] = dir[sample+'_K01730']
    return out_data


def cellulase(dir, sample):
    out_data = {'cellulase': 0}
    ko_list = [sample+'_K19668', sample+'_K01225']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['cellulase'] = dir[sample+'_K19668']+dir[sample+'_K01225']
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
    out_data = {'chitinase': 0}
    ko_list = [sample+'_K01183']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['chitinase'] = dir[sample+'_K01183']
    return out_data


def basic_endochitinase_B(dir, sample):
    out_data = {'basic endochitinase B': 0}
    ko_list = [sample+'_K20547']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['basic endochitinase B'] = dir[sample+'_K20547']
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


def ammonia_oxidation_amo_pmmo(dir, sample):
    out_data = {'ammonia oxidation (amo/pmmo)': 0}
    ko_list = [sample+'_K10946', sample+'_K10945',
               sample+'_K10944']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['ammonia oxidation (amo/pmmo)'] = (
        dir[sample+'_K10944'] +
        dir[sample+'_K10945'] +
        dir[sample+'_K10946'])/3
    return out_data


def nitrite_oxidation(dir, sample):
    out_data = {'nitrite oxidation': 0}
    ko_list = [sample+'_K00370', sample+'_K00371']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['nitrite oxidation'] = (
        dir[sample+'_K00370']+dir[sample+'_K00371'])/2
    return out_data


def dissim_nitrate_reduction(dir, sample):
    out_data = {'dissim nitrate reduction': 0}
    ko_list = [sample+'_K00370', sample+'_K00371',
               sample+'_K02567', sample+'_K02568']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['dissim nitrate reduction'] = (
        (dir[sample+'_K00370'] +
            dir[sample+'_K00371'])/2 +
        (dir[sample+'_K02567'] +
            dir[sample+'_K02568'])/2)
    return out_data


def DNRA(dir, sample):
    out_data = {'DNRA': 0}
    ko_list = [sample+'_K00362', sample+'_K00363',
               sample+'_K03385', sample+'_K15876']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['DNRA'] = (
        (dir[sample+'_K00362'] +
            dir[sample+'_K00363'])/2 +
        (dir[sample+'_K03385'] +
            dir[sample+'_K15876'])/2)
    return out_data


def nitrite_reduction(dir, sample):
    out_data = {'nitrite reduction': 0}
    ko_list = [sample+'_K00368', sample+'_K15864']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['nitrite reduction'] = (
        dir[sample+'_K00368'] +
        dir[sample+'_K15864'])
    return out_data


def nitric_oxide_reduction(dir, sample):
    out_data = {'nitric oxide reduction': 0}
    ko_list = [sample+'_K04561', sample+'_K02305']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['nitric oxide reduction'] = (dir[sample+'_K04561'] +
                                          dir[sample+'_K02305'])/2
    return out_data


def nitrous_oxide_reduction(dir, sample):
    out_data = {'nitrous-oxide reduction': 0}
    ko_list = [sample+'_K00376']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['nitrous-oxide reduction'] = dir[sample+'_K00376']
    return out_data


def nitrogen_fixation(dir, sample):
    out_data = {'nitrogen fixation': 0}
    ko_list = [sample+'_K02586', sample+'_K02591',
               sample+'_K02588', sample+'_K00531']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['nitrogen fixation'] = (
        dir[sample+'_K00531'] +
        dir[sample+'_K02586'] +
        dir[sample+'_K02588'] +
        dir[sample+'_K02591'])/4
    return out_data


def hydroxylamine_oxidation(dir, sample):
    out_data = {'hydroxylamine oxidation': 0}
    ko_list = [sample+'_K10535']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['hydroxylamine oxidation'] = dir[sample+'_K10535']
    return out_data


def hydrazine_dehydrogenase(dir, sample):
    out_data = {'hydrazine dehydrogenase': 0}
    ko_list = [sample+'_K20935']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['hydrazine dehydrogenase'] = dir[sample+'_K20935']
    return out_data


def hydrazine_synthase(dir, sample):
    out_data = {'hydrazine synthase': 0}
    ko_list = [sample+'_K20932', sample+'_K20933',
               sample+'_K20934']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['hydrazine synthase'] = (
        dir[sample+'_K20932'] +
        dir[sample+'_K20933'] +
        dir[sample+'_K20934'])/3
    return out_data


def dissimilatory_sulfate_to_APS(dir, sample):
    out_data = {'dissimilatory sulfate < > APS': 0}
    ko_list = [sample+'_K00958']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['dissimilatory sulfate < > APS'] = dir[sample+'_K00958']
    return out_data


def dissimilatory_sulfite_to_APS(dir, sample):
    out_data = {'dissimilatory sulfite < > APS': 0}
    ko_list = [sample+'_K00394', sample+'_K00395']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['dissimilatory sulfite < > APS'] = (
        dir[sample+'_K00394'] +
        dir[sample+'_K00395'])/2
    return out_data


def dissimilatory_sulfite_to_sulfide(dir, sample):
    out_data = {'dissimilatory sulfite < > sulfide': 0}
    ko_list = [sample+'_K11181', sample+'_K11180']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['dissimilatory sulfite < > sulfide'] = (
        dir[sample+'_K11181'] +
        dir[sample+'_K11180'])/2
    return out_data


def thiosulfate_oxidation(dir, sample):
    out_data = {'thiosulfate oxidation': 0}
    ko_list = [sample+'_K17222', sample+'_K17223',
               sample+'_K17224', sample+'_K17225',
               sample+'_K17226', sample+'_K17227']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['thiosulfate oxidation'] = (
        dir[sample+'_K17222'] +
        dir[sample+'_K17223'] +
        dir[sample+'_K17224'] +
        dir[sample+'_K17225'] +
        dir[sample+'_K17226'] +
        dir[sample+'_K17227'])/6
    return out_data


def alt_thiosulfate_oxidation_tsdA(dir, sample):
    out_data = {'alt thiosulfate oxidation tsdA': 0}
    ko_list = [sample+'_K19713']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['alt thiosulfate oxidation tsdA'] = dir[sample+'_K19713']
    return out_data


def alt_thiosulfate_oxidation_doxAD(dir, sample):
    out_data = {'alt thiosulfate oxidation doxAD': 0}
    ko_list = [sample+'_K16937', sample+'_K16936']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['alt thiosulfate oxidation doxAD'] = (
        dir[sample+'_K16937'] +
        dir[sample+'_K16936'])/2
    return out_data


def sulfur_reductase_sreABC(dir, sample):
    out_data = {'sulfur reductase sreABC': 0}
    ko_list = [sample+'_K17219', sample+'_K17220',
               sample+'_K17221']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['sulfur reductase sreABC'] = (
        dir[sample+'_K17219'] +
        dir[sample+'_K17220'] +
        dir[sample+'_K17221'])/3
    return out_data


def thiosulfate_or_polysulfide_reductase(dir, sample):
    out_data = {'thiosulfate/polysulfide reductase': 0}
    ko_list = [sample+'_K08352', sample+'_K08353',
               sample+'_K08354']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['thiosulfate/polysulfide reductase'] = (
        dir[sample+'_K08352'] +
        dir[sample+'_K08353'] +
        dir[sample+'_K08354'])/3
    return out_data


def sulfhydrogenase(dir, sample):
    out_data = {'sulfhydrogenase': 0}
    ko_list = [sample+'_K17993', sample+'_K17996',
               sample+'_K17995', sample+'_K17994']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['sulfhydrogenase'] = (
        dir[sample+'_K17993'] +
        dir[sample+'_K17994'] +
        dir[sample+'_K17995'] +
        dir[sample+'_K17996'])/4
    return out_data


def sulfur_disproportionation(dir, sample):
    out_data = {'sulfur disproportionation': 0}
    ko_list = [sample+'_K16952']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['sulfur disproportionation'] = dir[sample+'_K16952']
    return out_data


def sulfur_dioxygenase(dir, sample):
    out_data = {'sulfur dioxygenase': 0}
    ko_list = [sample+'_K17725']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['sulfur dioxygenase'] = dir[sample+'_K17725']
    return out_data


def sulfite_dehydrogenase(dir, sample):
    out_data = {'sulfite dehydrogenase': 0}
    ko_list = [sample+'_K05301']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['sulfite dehydrogenase'] = dir[sample+'_K05301']
    return out_data


def sulfite_dehydrogenase_quinone(dir, sample):
    out_data = {'sulfite dehydrogenase (quinone)': 0}
    ko_list = [sample+'_K21307', sample+'_K21308',
               sample+'_K21309']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['sulfite dehydrogenase (quinone)'] = (
        dir[sample+'_K21307'] +
        dir[sample+'_K21308'] +
        dir[sample+'_K21309'])/3
    return out_data


def sulfide_oxidation(dir, sample):
    out_data = {'sulfide oxidation': 0}
    ko_list = [sample+'_K17218', sample+'_K17229']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['sulfide oxidation'] = (
        dir[sample+'_K17218'] +
        dir[sample+'_K17229'])
    return out_data


def sulfur_assimilation(dir, sample):
    out_data = {'sulfur assimilation': 0}
    ko_list = [sample+'_K00380', sample+'_K00381', sample+'_K00392']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['sulfur assimilation'] = (
        (dir[sample+'_K00380'] +
            dir[sample+'_K00381'])/2 +
        dir[sample+'_K00392'])
    return out_data


def DMSP_demethylation(dir, sample):
    out_data = {'DMSP demethylation': 0}
    ko_list = [sample+'_K17486']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['DMSP demethylation'] = dir[sample+'_K17486']
    return out_data


def DMS_dehydrogenase(dir, sample):
    out_data = {'DMS dehydrogenase': 0}
    ko_list = [sample+'_K16964', sample+'_K16965', sample+'_K16966']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['DMS dehydrogenase'] = (
        dir[sample+'_K16964'] +
        dir[sample+'_K16965'] +
        dir[sample+'_K16966'])/3
    return out_data


def DMSO_reductase(dir, sample):
    out_data = {'DMSO reductase': 0}
    ko_list = [sample+'_K07306', sample+'_K07307',
               sample+'_K07308']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['DMSO reductase'] = (
        dir[sample+'_K07306'] +
        dir[sample+'_K07307'] +
        dir[sample+'_K07308'])/3
    return out_data


def NiFe_hydrogenase(dir, sample):
    out_data = {'NiFe hydrogenase': 0}
    ko_list = [sample+'_K00437', sample+'_K18008']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['NiFe hydrogenase'] = (
        dir[sample+'_K00437'] +
        dir[sample+'_K18008'])/2
    return out_data


def ferredoxin_hydrogenase(dir, sample):
    out_data = {'ferredoxin hydrogenase': 0}
    ko_list = [sample+'_K00534', sample+'_K00533']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['ferredoxin hydrogenase'] = (
        dir[sample+'_K00534'] +
        dir[sample+'_K00533'])/2
    return out_data


def membrane_bound_hydrogenase(dir, sample):
    out_data = {'membrane-bound hydrogenase': 0}
    ko_list = [sample+'_K18016', sample+'_K18017', sample+'_K18023']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['membrane-bound hydrogenase'] = (
        dir[sample+'_K18017'] +
        dir[sample+'_K18016'] +
        dir[sample+'_K18023'])/3
    return out_data


def hydrogen_quinone_oxidoreductase(dir, sample):
    out_data = {'hydrogen:quinone oxidoreductase': 0}
    ko_list = [sample+'_K05922', sample+'_K05927']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['hydrogen:quinone oxidoreductase'] = (
        dir[sample+'_K05927'] +
        dir[sample+'_K05922'])/2
    return out_data


def NAD_reducing_hydrogenase(dir, sample):
    out_data = {'NAD-reducing hydrogenase': 0}
    ko_list = [sample+'_K00436', sample+'_K18005',
               sample+'_K18006', sample+'_K18007']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['NAD-reducing hydrogenase'] = (
        dir[sample+'_K00436'] +
        dir[sample+'_K18007'] +
        dir[sample+'_K18006'] +
        dir[sample+'_K18005'])/4
    return out_data


def NADP_reducing_hydrogenase(dir, sample):
    out_data = {'NADP-reducing hydrogenase': 0}
    ko_list = [sample+'_K17992', sample+'_K18330',
               sample+'_K18331', sample+'_K18332']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['NADP-reducing hydrogenase'] = (
        dir[sample+'_K18332'] +
        dir[sample+'_K18331'] +
        dir[sample+'_K18330'] +
        dir[sample+'_K17992'])/4
    return out_data


def NiFe_hydrogenase_Hyd_one(dir, sample):
    out_data = {'NiFe hydrogenase Hyd-1': 0}
    ko_list = [sample+'_K06282', sample+'_K06281', sample+'_K03620']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['NiFe hydrogenase Hyd-1'] = (
        dir[sample+'_K03620'] +
        dir[sample+'_K06282'] +
        dir[sample+'_K06281'])/3
    return out_data


def thiamin_biosynthesis(dir, sample):
    out_data = {'thiamin biosynthesis': 0}
    ko_list = [sample+'_K03148', sample+'_K04487',
               sample+'_K03150', sample+'_K03153',
               sample+'_K03151', sample+'_K01662',
               sample+'_K03149', sample+'_K10810',
               sample+'_K03146', sample+'_K18278',
               sample+'_K03147', sample+'_K00877',
               sample+'_K00941', sample+'_K00788',
               sample+'_K14153', sample+'_K14154',
               sample+'_K00946']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['thiamin biosynthesis'] = (
        (dir[sample+'_K03148'] +
            dir[sample+'_K04487'] +
            (dir[sample+'_K03150'] +
                dir[sample+'_K03153']) +
            dir[sample+'_K03151'] +
            dir[sample+'_K01662'] +
            dir[sample+'_K03149'] +
            (dir[sample+'_K10810'] +
                dir[sample+'_K03146']) +
            (dir[sample+'_K18278'] +
                dir[sample+'_K03147'] +
                dir[sample+'_K00877'] +
                dir[sample+'_K00941']) +
            (dir[sample+'_K00877'] +
                dir[sample+'_K00941']) +
            (dir[sample+'_K00788'] +
                dir[sample+'_K14153'] +
                dir[sample+'_K14154']) +
            dir[sample+'_K00946']))/11
    return out_data


def riboflavin_biosynthesis(dir, sample):
    out_data = {'riboflavin biosynthesis': 0}
    ko_list = [sample+'_K02858', sample+'_K14652',
               sample+'_K00082', sample+'_K11752',
               sample+'_K00794', sample+'_K00793']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['riboflavin biosynthesis'] = (
        (dir[sample+'_K02858'] +
            dir[sample+'_K14652']) +
        (dir[sample+'_K00082'] +
            dir[sample+'_K11752']) +
        dir[sample+'_K00794'] +
        dir[sample+'_K00793'])/4
    return out_data


def cobalamin_biosynthesis(dir, sample):
    out_data = {'cobalamin biosynthesis': 0}
    ko_list = [sample+'_K00798', sample+'_K19221',
               sample+'_K02232', sample+'_K02225',
               sample+'_K02227', sample+'_K02231',
               sample+'_K19712', sample+'_K02233',
               sample+'_K02226', sample+'_K00768']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['cobalamin biosynthesis'] = (
        (dir[sample+'_K00798'] +
            dir[sample+'_K19221']) +
        dir[sample+'_K02232'] +
        dir[sample+'_K02225'] +
        dir[sample+'_K02227'] +
        dir[sample+'_K02231'] +
        dir[sample+'_K19712'] +
        dir[sample+'_K02233'] +
        dir[sample+'_K02226'] +
        dir[sample+'_K00768'])/8
    return out_data


def transporter_vitamin_B12(dir, sample):
    out_data = {'transporter: vitamin B12': 0}
    ko_list = [sample+'_K06858', sample+'_K06073',
               sample+'_K06074']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['transporter: vitamin B12'] = (
        dir[sample+'_K06074'] +
        dir[sample+'_K06073'] +
        dir[sample+'_K06858'])/3
    return out_data


def transporter_thiamin(dir, sample):
    out_data = {'transporter: thiamin': 0}
    ko_list = [sample+'_K02062', sample+'_K02063',
               sample+'_K02064']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['transporter: thiamin'] = (
        dir[sample+'_K02064'] +
        dir[sample+'_K02063'] +
        dir[sample+'_K02062'])/3
    return out_data


def transporter_urea(dir, sample):
    out_data = {'transporter: urea': 0}
    ko_list = [sample+'_K11959', sample+'_K11960',
               sample+'_K11961', sample+'_K11962',
               sample+'_K11963']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['transporter: urea'] = (
        dir[sample+'_K11959'] +
        dir[sample+'_K11960'] +
        dir[sample+'_K11961'] +
        dir[sample+'_K11962'] +
        dir[sample+'_K11963'])/5
    return out_data


def transporter_phosphonate(dir, sample):
    out_data = {'transporter: phosphonate': 0}
    ko_list = [sample+'_K02042', sample+'_K02041', sample+'_K02044']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['transporter: phosphonate'] = (
        dir[sample+'_K02041'] +
        dir[sample+'_K02042'] +
        dir[sample+'_K02044'])/3
    return out_data


def transporter_phosphate(dir, sample):
    out_data = {'transporter: phosphate': 0}
    ko_list = [sample+'_K02037', sample+'_K02038',
               sample+'_K02036', sample+'_K02040']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['transporter: phosphate'] = (
        dir[sample+'_K02040'] +
        dir[sample+'_K02036'] +
        dir[sample+'_K02037'] +
        dir[sample+'_K02038'])/4
    return out_data


def Flagellum(dir, sample):
    out_data = {'Flagellum': 0}
    ko_list = [sample+'_K02409', sample+'_K02401',
               sample+'_K02394', sample+'_K02397',
               sample+'_K02396', sample+'_K02391',
               sample+'_K02390', sample+'_K02393',
               sample+'_K02392', sample+'_K02386',
               sample+'_K02557', sample+'_K02556',
               sample+'_K02400', sample+'_K02418',
               sample+'_K02389', sample+'_K02412',
               sample+'_K02387', sample+'_K02410',
               sample+'_K02411', sample+'_K02416',
               sample+'_K02417', sample+'_K02407',
               sample+'_K02406']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Flagellum'] = (
        dir[sample+'_K02409'] +
        dir[sample+'_K02401'] +
        dir[sample+'_K02394'] +
        dir[sample+'_K02397'] +
        dir[sample+'_K02396'] +
        dir[sample+'_K02391'] +
        dir[sample+'_K02390'] +
        dir[sample+'_K02393'] +
        dir[sample+'_K02392'] +
        dir[sample+'_K02386'] +
        dir[sample+'_K02557'] +
        dir[sample+'_K02556'] +
        dir[sample+'_K02400'] +
        dir[sample+'_K02418'] +
        dir[sample+'_K02389'] +
        dir[sample+'_K02412'] +
        dir[sample+'_K02387'] +
        dir[sample+'_K02410'] +
        dir[sample+'_K02411'] +
        dir[sample+'_K02416'] +
        dir[sample+'_K02417'] +
        dir[sample+'_K02407'] +
        dir[sample+'_K02406'])/23
    return out_data


def Chemotaxis(dir, sample):
    out_data = {'Chemotaxis': 0}
    ko_list = [sample+'_K13924', sample+'_K00575',
               sample+'_K03413', sample+'_K03412',
               sample+'_K03406', sample+'_K03407',
               sample+'_K03415', sample+'_K03408']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Chemotaxis'] = (
        dir[sample+'_K13924'] +
        dir[sample+'_K00575'] +
        dir[sample+'_K03413'] +
        dir[sample+'_K03412'] +
        dir[sample+'_K03406'] +
        dir[sample+'_K03407'] +
        dir[sample+'_K03415'] +
        dir[sample+'_K03408'])/8
    return out_data


def Methanogenesis_via_methanol(dir, sample):
    out_data = {'Methanogenesis via methanol': 0}
    ko_list = [sample+'_K04480', sample+'_K14080',
               sample+'_K14081']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis via methanol'] = (
        dir[sample+'_K04480'] +
        dir[sample+'_K14080'] +
        dir[sample+'_K14081'])/3
    return out_data


def Methanogenesis_via_acetate(dir, sample):
    out_data = {'Methanogenesis via acetate': 0}
    ko_list = [sample+'_K00193', sample+'_K00194',
               sample+'_K00197']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis via acetate'] = (
        dir[sample+'_K00193'] +
        dir[sample+'_K00194'] +
        dir[sample+'_K00197'])/3
    return out_data


def Methanogenesis_via_dimethylsulfide_methanethiol_methylpropano(dir, sample):
    out_data = {
        'Methanogenesis via dimethylsulfide, methanethiol, methylpropanoate': 0}
    ko_list = [sample+'_K16954', sample+'_K16955']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis via dimethylsulfide, methanethiol, methylpropanoate'] = (dir[sample+'_K16954']+dir[sample+'_K16955'])/2
    return out_data


def Methanogenesis_via_methylamine(dir, sample):
    out_data = {'Methanogenesis via methylamine': 0}
    ko_list = [sample+'_K16178']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis via methylamine'] = dir[sample+'_K16178']
    return out_data


def Methanogenesis_via_trimethylamine(dir, sample):
    out_data = {'Methanogenesis via trimethylamine': 0}
    ko_list = [sample+'_K14083']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis via trimethylamine'] = dir[sample+'_K14083']
    return out_data


def Methanogenesis_via_dimethylamine(dir, sample):
    out_data = {'Methanogenesis via dimethylamine': 0}
    ko_list = [sample+'_K16178', sample+'_K14082']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis via dimethylamine'] = (
        dir[sample+'_K16178']+dir[sample+'_K14082'])/2
    return out_data


def Methanogenesis_via_CO2(dir, sample):
    out_data = {'Methanogenesis via CO2': 0}
    ko_list = [sample+'_K00200', sample+'_K00201',
               sample+'_K00202', sample+'_K00203',
               sample+'_K00205', sample+'_K11261',
               sample+'_K00672', sample+'_K01499',
               sample+'_K13942', sample+'_K00320',
               sample+'_K00577', sample+'_K00578',
               sample+'_K00579', sample+'_K00580',
               sample+'_K00581', sample+'_K00582',
               sample+'_K00583', sample+'_K00584']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Methanogenesis via CO2'] = (
        dir[sample+'_K00200'] +
        dir[sample+'_K00201'] +
        dir[sample+'_K00202'] +
        dir[sample+'_K00203'] +
        dir[sample+'_K00205'] +
        dir[sample+'_K11261'] +
        dir[sample+'_K00672'] +
        dir[sample+'_K01499'] +
        dir[sample+'_K13942'] +
        dir[sample+'_K00320'] +
        dir[sample+'_K00577'] +
        dir[sample+'_K00578'] +
        dir[sample+'_K00579'] +
        dir[sample+'_K00580'] +
        dir[sample+'_K00581'] +
        dir[sample+'_K00582'] +
        dir[sample+'_K00583'] +
        dir[sample+'_K00584'])/18
    return out_data


def Coenzyme_B_Coenzyme_M_regeneration(dir, sample):
    out_data = {'Coenzyme B/Coenzyme M regeneration': 0}
    ko_list = [sample+'_K03388', sample+'_K03389',
               sample+'_K03390', sample+'_K08264',
               sample+'_K08265']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Coenzyme B/Coenzyme M regeneration'] = (
        dir[sample+'_K03388'] +
        dir[sample+'_K03389'] +
        dir[sample+'_K03390'] +
        dir[sample+'_K08264'] +
        dir[sample+'_K08265'])/5
    return out_data


def Coenzyme_M_reduction_to_methane(dir, sample):
    out_data = {'Coenzyme M reduction to methane': 0}
    ko_list = [sample+'_K00399', sample+'_K00401',
               sample+'_K00402']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Coenzyme M reduction to methane'] = (
        dir[sample+'_K00399'] +
        dir[sample+'_K00401'] +
        dir[sample+'_K00402'])/3
    return out_data


def dimethylamine_or_trimethylamine_dehydrogenase(dir, sample):
    out_data = {'dimethylamine/trimethylamine dehydrogenase': 0}
    ko_list = [sample + '_K00317']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['dimethylamine/trimethylamine dehydro\
    genase'] = dir[sample+'_K00317']
    return out_data


def Soluble_methane_monooxygenase(dir, sample):
    out_data = {'Soluble methane monooxygenase': 0}
    ko_list = [sample+'_K16157', sample+'_K16158',
               sample+'_K16159', sample+'_K16161']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Soluble methane monooxygenase'] = (
        dir[sample+'_K16157'] +
        dir[sample+'_K16158'] +
        dir[sample+'_K16159'] +
        dir[sample+'_K16161'])/4
    return out_data


def methanol_dehydrogenase(dir, sample):
    out_data = {'methanol dehydrogenase': 0}
    ko_list = [sample+'_K14028', sample+'_K14029']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['methanol dehydrogenase'] = (
        dir[sample+'_K14028'] +
        dir[sample+'_K14029'])/2
    return out_data


def alcohol_oxidase(dir, sample):
    out_data = {'alcohol oxidase': 0}
    ko_list = [sample + '_K17066']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['alcohol oxidase'] = dir[sample+'_K17066']
    return out_data


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
               sample+'_K02693', sample+'_K02694',
               sample+'_K02696', sample+'_K02697',
               sample+'_K02698', sample+'_K02699',
               sample+'_K02700', sample+'_K08905',
               sample+'_K02695', sample+'_K02701',
               sample+'_K14332', sample+'_K02702']
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
        dir[sample+'_K02694'] +
        dir[sample+'_K02696'] +
        dir[sample+'_K02697'] +
        dir[sample+'_K02698'] +
        dir[sample+'_K02699'] +
        dir[sample+'_K02700'] +
        dir[sample+'_K08905'] +
        dir[sample+'_K02695'] +
        dir[sample+'_K02701'] +
        dir[sample+'_K14332'] +
        dir[sample+'_K02702'])/16
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


def anoxygenic_type_II_reaction_center(dir, sample):
    out_data = {'anoxygenic type-II reaction center': 0}
    ko_list = [sample+'_K08929', sample+'_K08928']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['anoxygenic type-II reaction center'] = (
        dir[sample+'_K08928'] +
        dir[sample+'_K08929'])/2
    return out_data


def anoxygenic_type_I_reaction_center(dir, sample):
    out_data = {'anoxygenic type-I reaction center': 0}
    ko_list = [sample+'_K08940', sample+'_K08941',
               sample+'_K08942', sample+'_K08943']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['anoxygenic type-I reaction center'] = (
        dir[sample+'_K08940'] +
        dir[sample+'_K08941'] +
        dir[sample+'_K08942'] +
        dir[sample+'_K08943'])/4
    return out_data


def Retinal_biosynthesis(dir, sample):
    out_data = {'Retinal biosynthesis': 0}
    ko_list = [sample+'_K02291', sample+'_K06443',
               sample+'_K10027', sample+'_K13789']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Retinal biosynthesis'] = (
        dir[sample+'_K06443'] +
        dir[sample+'_K02291'] +
        dir[sample+'_K10027'] +
        dir[sample+'_K13789'])/4
    return out_data


def Entner_Doudoroff_Pathway(dir, sample):
    out_data = {'Entner-Doudoroff Pathway': 0}
    ko_list = [sample+'_K13937', sample+'_K01690',
               sample+'_K01625', sample+'_K17463',
               sample+'_K11395', sample+'_K00036',
               sample+'_K01057', sample+'_K07404',
               sample+'_K01690', sample+'_K01625',
               sample+'_K17463', sample+'_K11395']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Entner-Doudoroff Pathway'] = (
        (dir[sample+'_K13937'] +
            dir[sample+'_K01690'] +
            (dir[sample+'_K01625'] +
                dir[sample+'_K17463'] +
                dir[sample+'_K11395']))/3 +
        (dir[sample+'_K00036'] +
            (dir[sample+'_K01057'] +
                dir[sample+'_K07404']) +
            dir[sample+'_K01690'] +
            (dir[sample+'_K01625'] +
                dir[sample+'_K17463'] +
                dir[sample+'_K11395']))/4)
    return out_data


def Mixed_acid_Lactate(dir, sample):
    out_data = {'Mixed acid: Lactate': 0}
    ko_list = [sample+'_K00016']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: Lactate'] = dir[sample+'_K00016']
    return out_data


def Mixed_acid_Formate(dir, sample):
    out_data = {'Mixed acid: Formate': 0}
    ko_list = [sample+'_K00656']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: Formate'] = dir[sample+'_K00656']
    return out_data


def Mixed_acid_Formate_to_CO2_and_H2(dir, sample):
    out_data = {'Mixed acid: Formate to CO2 & H2': 0}
    ko_list = [sample+'_K00122', sample+'_K00123',
               sample+'_K00124', sample+'_K00125',
               sample+'_K00126', sample+'_K00127']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: Formate to CO2 & H2'] = (
        dir[sample+'_K00122'] +
        dir[sample+'_K00125'] +
        dir[sample+'_K00126'] +
        dir[sample+'_K00123'] +
        dir[sample+'_K00124'] +
        dir[sample+'_K00127'])/6
    return out_data


def Mixed_acid_Acetate(dir, sample):
    out_data = {'Mixed acid: Acetate': 0}
    ko_list = [sample+'_K01512', sample+'_K00156',
               sample+'_K00158', sample+'_K01067',
               sample+'_K13788', sample+'_K04020',
               sample+'_K00467']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: Acetate'] = (
        (dir[sample+'_K00158'] +
            dir[sample+'_K01512'] +
            dir[sample+'_K13788'] +
            dir[sample+'_K04020'])/2 +
        dir[sample+'_K00156'] +
        dir[sample+'_K01067'] +
        dir[sample+'_K00467'])
    return out_data


def Mixed_acid_Ethanol_Acetate_to_Acetylaldehyde(dir, sample):
    out_data = {'Mixed acid: Ethanol, Acetate to Acetylaldehyde': 0}
    ko_list = [sample+'_K00128', sample+'_K14085',
               sample+'_K00149', sample+'_K00129',
               sample+'_K00138']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: Ethanol, Acetate to Acetylaldehyde'] = (
        dir[sample+'_K00128'] +
        dir[sample+'_K14085'] +
        dir[sample+'_K00149'] +
        dir[sample+'_K00129'] +
        dir[sample+'_K00138'])
    return out_data


def Mixed_acid_Ethanol_Acetyl_CoA_to_Acetylaldehyde_revers(dir, sample):
    out_data = {'Mixed acid: Ethanol, Acetyl-CoA to Acetylaldehyde (reversible)': 0}
    ko_list = [sample+'_K00132', sample+'_K04072',
               sample+'_K04073', sample+'_K18366',
               sample+'_K04021']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: Ethanol, Acetyl-CoA to Acetylaldehyde (reversible)'] = (
        dir[sample+'_K00132'] +
        dir[sample+'_K04072'] +
        dir[sample+'_K04073'] +
        dir[sample+'_K18366'] +
        dir[sample+'_K04021'])
    return out_data


def Mixed_acid_Ethanol_Acetylaldehyde_to_Ethanol(dir, sample):
    out_data = {'Mixed acid: Ethanol, Acetylaldehyde to Ethanol': 0}
    ko_list = [sample+'_K13951', sample+'_K13980',
               sample+'_K13952', sample+'_K13953',
               sample+'_K13954', sample+'_K00001',
               sample+'_K00121', sample+'_K04072',
               sample+'_K18857', sample+'_K00114',
               sample+'_K00002', sample+'_K04022',
               sample+'_K14028', sample+'_K14029']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: Ethanol, Acetylaldehyde to Ethanol'] = (
        (dir[sample+'_K13951'] +
            dir[sample+'_K13980'] +
            dir[sample+'_K13952'] +
            dir[sample+'_K13953'] +
            dir[sample+'_K13954'] +
            dir[sample+'_K00001'] +
            dir[sample+'_K00121'] +
            dir[sample+'_K04072'] +
            dir[sample+'_K18857'] +
            dir[sample+'_K00114'] +
            dir[sample+'_K00002'] +
            dir[sample+'_K04022']) +
        (dir[sample+'_K14028'] +
            dir[sample+'_K14029'])/2)
    return out_data


def Mixed_acid_PEP_to_Succ_via_OAA_malate_fuma(dir, sample):
    out_data = {'Mixed acid: PEP to Succinate via OAA, malate & fumarate': 0}
    ko_list = [sample+'_K01596', sample+'_K20370',
               sample+'_K01610', sample+'_K00024',
               sample+'_K00025', sample+'_K00026',
               sample+'_K00051', sample+'_K00116',
               sample+'_K01676', sample+'_K01677',
               sample+'_K01678', sample+'_K01679',
               sample+'_K00244', sample+'_K00245',
               sample+'_K00246', sample+'_K00247']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Mixed acid: PEP to Succinate via OAA, malate & fuma\
    rate'] = (
        ((dir[sample+'_K01596'] +
            dir[sample+'_K20370'] +
            dir[sample+'_K01610']) +
            ((dir[sample+'_K00051'] +
                dir[sample+'_K00116']) +
                (dir[sample+'_K00025'] +
                    dir[sample+'_K00026'] +
                    dir[sample+'_K00024'])/3) +
            (dir[sample+'_K01676'] +
                dir[sample+'_K01677'] +
                dir[sample+'_K01678'] +
                dir[sample+'_K01679'])/4 +
            (dir[sample+'_K00244'] +
                dir[sample+'_K00245'] +
                dir[sample+'_K00246'] +
                dir[sample+'_K00247'])/4)/4)
    return out_data


def Naphthalene_degradation_to_salicylate(dir, sample):
    out_data = {'Naphthalene degradation to salicylate': 0}
    ko_list = [sample+'_K14578', sample+'_K14579',
               sample+'_K14580', sample+'_K14581',
               sample+'_K14582', sample+'_K14583',
               sample+'_K14584', sample+'_K14585',
               sample+'_K00152']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Naphthalene degradation to salicylate'] = (
        (dir[sample+'_K14579'] +
            dir[sample+'_K14580'] +
            dir[sample+'_K14578'] +
            dir[sample+'_K14581'])/4 +
        dir[sample+'_K14582'] +
        dir[sample+'_K14583'] +
        dir[sample+'_K14584'] +
        dir[sample+'_K14585'] +
        dir[sample+'_K00152'])/6
    return out_data


def Biofilm_PGA_Synthesis_protein(dir, sample):
    out_data = {'Biofilm PGA Synthesis protein': 0}
    ko_list = [sample+'_K11935', sample+'_K11936',
               sample+'_K11937', sample+'_K11931']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Biofilm PGA Synthesis protein'] = (
        dir[sample+'_K11935'] +
        dir[sample+'_K11931'] +
        dir[sample+'_K11936'] +
        dir[sample+'_K11937'])/4
    return out_data


def Colanic_acid_and_Biofilm_transcriptional_regulator(dir, sample):
    out_data = {'Colanic acid and Biofilm transcriptional regulator': 0}
    ko_list = [sample+'_K13654']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Colanic acid and Biofilm transcriptional regul\
    ator'] = dir[sample+'_K13654']
    return out_data


def Biofilm_regulator_BssS(dir, sample):
    out_data = {'Biofilm regulator BssS': 0}
    ko_list = [sample+'_K12148']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Biofilm regulator BssS'] = dir[sample+'_K12148']
    return out_data


def Colanic_acid_and_Biofilm_protein_A(dir, sample):
    out_data = {'Colanic acid and Biofilm protein A': 0}
    ko_list = [sample+'_K13650']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Colanic acid and Biofilm protein A'] = dir[sample+'_K13650']
    return out_data


def Curli_fimbriae_biosynthesis(dir, sample):
    out_data = {'Curli fimbriae biosynthesis': 0}
    ko_list = [sample+'_K04334', sample+'_K04335',
               sample+'_K04336']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Curli fimbriae biosynthesis'] = (
        dir[sample+'_K04335'] +
        dir[sample+'_K04334'] +
        dir[sample+'_K04336'])/3
    return out_data


def Adhesion(dir, sample):
    out_data = {'Adhesion': 0}
    ko_list = [sample+'_K12687']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Adhesion'] = dir[sample+'_K12687']
    return out_data


def Competence_related_core_components(dir, sample):
    out_data = {'Competence-related core components': 0}
    ko_list = [sample+'_K02237', sample+'_K02238',
               sample+'_K02239', sample+'_K02240',
               sample+'_K02241', sample+'_K02242',
               sample+'_K02243', sample+'_K02244',
               sample+'_K02245', sample+'_K02246',
               sample+'_K02247', sample+'_K02248',
               sample+'_K02249', sample+'_K01493']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Competence-related core components'] = (
        dir[sample+'_K02237'] +
        dir[sample+'_K01493'] +
        dir[sample+'_K02238'] +
        dir[sample+'_K02239'] +
        dir[sample+'_K02240'] +
        dir[sample+'_K02241'] +
        dir[sample+'_K02242'] +
        dir[sample+'_K02243'] +
        dir[sample+'_K02244'] +
        dir[sample+'_K02245'] +
        dir[sample+'_K02246'] +
        dir[sample+'_K02247'] +
        dir[sample+'_K02248'] +
        dir[sample+'_K02249'])/14
    return out_data


def Competence_related_related_components(dir, sample):
    out_data = {'Competence-related related components': 0}
    ko_list = [sample+'_K02250', sample+'_K02251',
               sample+'_K02252', sample+'_K02253',
               sample+'_K02254']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Competence-related related components'] = (
        dir[sample+'_K02250'] +
        dir[sample+'_K02251'] +
        dir[sample+'_K02252'] +
        dir[sample+'_K02253'] +
        dir[sample+'_K02254'])/5
    return out_data


def Competence_factors(dir, sample):
    out_data = {'Competence factors': 0}
    ko_list = [sample+'_K12292', sample+'_K12293',
               sample+'_K12294', sample+'_K12295',
               sample+'_K12296', sample+'_K07680',
               sample+'_K12415']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Competence factors'] = (
        dir[sample+'_K12292'] +
        dir[sample+'_K07680'] +
        dir[sample+'_K12293'] +
        dir[sample+'_K12415'] +
        dir[sample+'_K12294'] +
        dir[sample+'_K12295'] +
        dir[sample+'_K12296'])/7
    return out_data


def Glyoxylate_shunt(dir, sample):
    out_data = {'Glyoxylate shunt': 0}
    ko_list = [sample+'_K01637', sample+'_K01638']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Glyoxylate shunt'] = (
        dir[sample+'_K01637']+dir[sample+'_K01638'])/2
    return out_data


def Anaplerotic_genes(dir, sample):
    out_data = {'Anaplerotic genes': 0}
    ko_list = [sample+'_K00029', sample+'_K01595',
               sample+'_K01610', sample+'_K01596',
               sample+'_K20370', sample+'_K01958',
               sample+'_K01959', sample+'_K01960']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Anaplerotic genes'] = (
        dir[sample+'_K00029'] +
        dir[sample+'_K01595'] +
        (dir[sample+'_K01610'] +
            dir[sample+'_K01596'] +
            dir[sample+'_K20370']) +
        (dir[sample+'_K01958'] +
            (dir[sample+'_K01959'] +
                dir[sample+'_K01960']))/2)/4
    return out_data


def Sulfolipid_biosynthesis(dir, sample):
    out_data = {'Sulfolipid biosynthesis': 0}
    ko_list = [sample+'_K06118', sample + '_K06119']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Sulfolipid biosynthesis'] = (
        dir[sample+'_K06118']+dir[sample+'_K06119'])/2
    return out_data


def C_P_lyase_cleavage_PhnJ(dir, sample):
    out_data = {'C-P lyase cleavage PhnJ': 0}
    ko_list = [sample+'_K06163']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['C-P lyase cleavage PhnJ'] = dir[sample+'_K06163']
    return out_data


def CP_lyase_complex(dir, sample):
    out_data = {'CP-lyase complex': 0}
    ko_list = [sample+'_K06163', sample+'_K06164',
               sample+'_K06165', sample+'_K06166']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['CP-lyase complex'] = (
        dir[sample+'_K06163'] +
        dir[sample+'_K06164'] +
        dir[sample+'_K06165'] +
        dir[sample+'_K06166'])/4
    return out_data


def CP_lyase_operon(dir, sample):
    out_data = {'CP-lyase operon': 0}
    ko_list = [sample+'_K06162', sample+'_K06163',
               sample+'_K06164', sample+'_K06165',
               sample+'_K06166', sample+'_K06167',
               sample+'_K05780', sample+'_K05781',
               sample+'_K09994', sample+'_K05774',
               sample+'_K02043']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['CP-lyase operon'] = (
        dir[sample+'_K06163'] +
        dir[sample+'_K06164'] +
        dir[sample+'_K06165'] +
        dir[sample+'_K06166'] +
        dir[sample+'_K05780'] +
        dir[sample+'_K06162'] +
        dir[sample+'_K06167'] +
        dir[sample+'_K09994'] +
        dir[sample+'_K05774'] +
        dir[sample+'_K05781'] +
        dir[sample+'_K02043'])/11
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
    ko_list = [sample+'_K03070', sample+'_K03071',
               sample+'_K03072', sample+'_K03073',
               sample+'_K03074', sample+'_K03075',
               sample+'_K03076', sample+'_K03210',
               sample+'_K03217', sample+'_K13301',
               sample+'_K03110', sample+'_K03106']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Sec-SRP'] = (
        (dir[sample+'_K03072'] +
            dir[sample+'_K03074']) +
        dir[sample+'_K03073'] +
        dir[sample+'_K03075'] +
        dir[sample+'_K03076'] +
        dir[sample+'_K03210'] +
        dir[sample+'_K03217'] +
        dir[sample+'_K03070'] +
        dir[sample+'_K13301'] +
        dir[sample+'_K03110'] +
        dir[sample+'_K03071'] +
        dir[sample+'_K03106'])/11
    return out_data


def Twin_Arginine_Targeting(dir, sample):
    out_data = {'Twin Arginine Targeting': 0}
    ko_list = [sample+'_K03116', sample+'_K03117',
               sample+'_K03118', sample+'_K03425']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Twin Arginine Targeting'] = (
        dir[sample+'_K03116'] +
        dir[sample+'_K03117'] +
        dir[sample+'_K03118'] +
        dir[sample+'_K03425'])/4
    return out_data


def Type_Vabc_Secretion(dir, sample):
    out_data = {'Type Vabc Secretion': 0}
    ko_list = [sample+'_K11016', sample+'_K11017',
               sample+'_K11028', sample+'_K12341',
               sample+'_K12342']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Type Vabc Secretion'] = (
        dir[sample+'_K11028'] +
        dir[sample+'_K11017'] +
        dir[sample+'_K11016'] +
        dir[sample+'_K12341'] +
        dir[sample+'_K12342'])/5
    return out_data


def Serine_pathway_or_formaldehyde_assimilation(dir, sample):
    out_data = {'Serine pathway/formaldehyde assimilation': 0}
    ko_list = [sample+'_K00600', sample+'_K00830',
               sample+'_K00018', sample+'_K11529',
               sample+'_K01689', sample+'_K01595',
               sample+'_K00024', sample+'_K08692',
               sample+'_K14067']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Serine pathway/formaldehyde assimilation'] = (
        (dir[sample+'_K00600'] +
            dir[sample+'_K00830'] +
            dir[sample+'_K00018'] +
            dir[sample+'_K11529'] +
            dir[sample+'_K01689'] +
            dir[sample+'_K01595'] +
            dir[sample+'_K00024'] +
            dir[sample+'_K08692'] +
            dir[sample+'_K14067'])/9)
    return out_data


def Arsenic_reduction(dir, sample):
    out_data = {'Arsenic reduction': 0}
    ko_list = [sample+'_K00537', sample+'_K03741',
               sample+'_K18701', sample+'_K03325',
               sample+'_K03893', sample+'_K03892',
               sample+'_K01551']
    for ko in ko_list:
        if ko in dir:
            pass
        else:
            dir[ko] = 0
    out_data['Arsenic reduction'] = (
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

function_order = ['glycolysis',
                  'gluconeogenesis',
                  'TCA Cycle',
                  'NAD(P)H-quinone oxidoreductase',
                  'NADH-quinone oxidoreductase',
                  'F-type ATPase',
                  'V-type ATPase',
                  'Cytochrome c oxidase',
                  'Ubiquinol-cytochrome c reductase',
                  'Cytochrome o ubiquinol oxidase',
                  'Cytochrome aa3-600 menaquinol oxidase',
                  'Cytochrome c oxidase, cbb3-type',
                  'Cytochrome bd complex',
                  'RuBisCo',
                  'CBB Cycle', 'rTCA Cycle', 'Wood-Ljungdahl',
                  '3-Hydroxypropionate Bicycle',
                  '4-Hydroxybutyrate/3-hydroxypropionate',
                  'pectinesterase', 'diacetylchitobiose deacetylase',
                  'glucoamylase',
                  'D-galacturonate epimerase',
                  'exo-poly-alpha-galacturonosidase',
                  'oligogalacturonide lyase', 'cellulase',
                  'exopolygalacturonase',
                  'chitinase', 'basic endochitinase B',
                  'bifunctional chitinase/lysozyme',
                  'beta-N-acetylhexosaminidase',
                  'D-galacturonate isomerase',
                  'alpha-amylase', 'beta-glucosidase', 'pullulanase',
                  'ammonia oxidation (amo/pmmo)', 'hydroxylamine oxidation',
                  'nitrite oxidation',
                  'dissim nitrate reduction', 'DNRA', 'nitrite reduction',
                  'nitric oxide reduction', 'nitrous-oxide reduction',
                  'nitrogen fixation', 'hydrazine dehydrogenase',
                  'hydrazine synthase',
                  'dissimilatory sulfate < > APS',
                  'dissimilatory sulfite < > APS',
                  'dissimilatory sulfite < > sulfide',
                  'thiosulfate oxidation', 'alt thiosulfate oxidation tsdA',
                  'alt thiosulfate oxidation doxAD', 'sulfur reductase sreABC',
                  'thiosulfate/polysulfide reductase', 'sulfhydrogenase',
                  'sulfur disproportionation', 'sulfur dioxygenase',
                  'sulfite dehydrogenase', 'sulfite dehydrogenase (quinone)',
                  'sulfide oxidation', 'sulfur assimilation',
                  'DMSP demethylation', 'DMS dehydrogenase', 'DMSO reductase',
                  'NiFe hydrogenase', 'ferredoxin hydrogenase',
                  'membrane-bound hydrogenase',
                  'hydrogen:quinone oxidoreductase',
                  'NAD-reducing hydrogenase',
                  'NADP-reducing hydrogenase', 'NiFe hydrogenase Hyd-1',
                  'thiamin biosynthesis',
                  'riboflavin biosynthesis',
                  'cobalamin biosynthesis', 'transporter: vitamin B12',
                  'transporter: thiamin', 'transporter: urea',
                  'transporter: phosphonate', 'transporter: phosphate',
                  'Flagellum', 'Chemotaxis', 'Methanogenesis via methanol',
                  'Methanogenesis via acetate',
                  'Methanogenesis via dimethylsulfide, methanethiol, methylpropanoate',
                  'Methanogenesis via methylamine',
                  'Methanogenesis via trimethylamine',
                  'Methanogenesis via dimethylamine', 'Methanogenesis via CO2',
                  'Coenzyme B/Coenzyme M regeneration',
                  'Coenzyme M reduction to methane',
                  'Soluble methane monooxygenase',
                  'methanol dehydrogenase', 'alcohol oxidase',
                  'dimethylamine/trimethylamine dehydrogenase',
                  'Photosystem II', 'Photosystem I', 'Cytochrome b6/f complex',
                  'anoxygenic type-II reaction center',
                  'anoxygenic type-I reaction center',
                  'Retinal biosynthesis',
                  'Entner-Doudoroff Pathway', 'Mixed acid: Lactate',
                  'Mixed acid: Formate',
                  'Mixed acid: Formate to CO2 & H2', 'Mixed acid: Acetate',
                  'Mixed acid: Ethanol, Acetate to Acetylaldehyde',
                  'Mixed acid: Ethanol, Acetyl-CoA to Acetylaldehyde (reversible)',
                  'Mixed acid: Ethanol, Acetylaldehyde to Ethanol',
                  'Mixed acid: PEP to Succinate via OAA, malate & fumarate',
                  'Naphthalene degradation to salicylate',
                  'Biofilm PGA Synthesis protein',
                  'Colanic acid and Biofilm transcriptional regulator',
                  'Biofilm regulator BssS',
                  'Colanic acid and Biofilm protein A',
                  'Curli fimbriae biosynthesis', 'Adhesion',
                  'Competence-related core components',
                  'Competence-related related components',
                  'Competence factors',
                  'Glyoxylate shunt', 'Anaplerotic genes',
                  'Sulfolipid biosynthesis',
                  'C-P lyase cleavage PhnJ', 'CP-lyase complex',
                  'CP-lyase operon', 'Type I Secretion',
                  'Type II Secretion', 'Type III Secretion',
                  'Type IV Secretion', 'Type VI Secretion',
                  'Sec-SRP', 'Twin Arginine Targeting', 'Type Vabc Secretion',
                  'Serine pathway/formaldehyde assimilation',
                  'Arsenic reduction']

filehandle = str(arg_dict['Output'])
out_file = open(filehandle, "w")
out_file.write('Function'+"\t"+str("\t".join(function_order))+"\n")


for k in genome_data:
    # print(k)
    # print(reverse_tca(relative_abundance, k))
    pathway_data = {}
    pathway_data.update(glycolysis(relative_abundance, k))
    pathway_data.update(gluconeogenesis(relative_abundance, k))
    pathway_data.update(tca_cycle(relative_abundance, k))
    pathway_data.update(NADPH_quinone_oxidoreductase(relative_abundance, k))
    pathway_data.update(NADH_quinone_oxidoreductase(relative_abundance, k))
    pathway_data.update(F_type_ATPase(relative_abundance, k))
    pathway_data.update(V_type_ATPase(relative_abundance, k))
    pathway_data.update(Cytochrome_c_oxidase(relative_abundance, k))
    pathway_data.update(
        Ubiquinol_cytochrome_c_reductase(relative_abundance, k))
    pathway_data.update(Cytochrome_o_ubiquinol_oxidase(relative_abundance, k))
    pathway_data.update(
        Cytochrome_aa3_600_menaquinol_oxidase(relative_abundance, k))
    pathway_data.update(Cytochrome_c_oxidase_cbb3_type(relative_abundance, k))
    pathway_data.update(Cytochrome_bd_complex(relative_abundance, k))
    pathway_data.update(RuBisCo(relative_abundance, k))
    pathway_data.update(CBB_Cycle(relative_abundance, k))
    pathway_data.update(rTCA_Cycle(relative_abundance, k))
    pathway_data.update(Wood_Ljungdahl(relative_abundance, k))
    pathway_data.update(three_Hydroxypropionate_Bicycle(relative_abundance, k))
    pathway_data.update(
        four_Hydroxybutyrate_or_three_hydroxypropionate(relative_abundance, k))
    pathway_data.update(pectinesterase(relative_abundance, k))
    pathway_data.update(diacetylchitobiose_deacetylase(relative_abundance, k))
    pathway_data.update(glucoamylase(relative_abundance, k))
    pathway_data.update(D_galacturonate_epimerase(relative_abundance, k))
    pathway_data.update(
        exo_poly_alpha_galacturonosidase(relative_abundance, k))
    pathway_data.update(oligogalacturonide_lyase(relative_abundance, k))
    pathway_data.update(cellulase(relative_abundance, k))
    pathway_data.update(exopolygalacturonase(relative_abundance, k))
    pathway_data.update(chitinase(relative_abundance, k))
    pathway_data.update(basic_endochitinase_B(relative_abundance, k))
    pathway_data.update(
        bifunctional_chitinase_or_lysozyme(relative_abundance, k))
    pathway_data.update(beta_N_acetylhexosaminidase(relative_abundance, k))
    pathway_data.update(D_galacturonate_isomerase(relative_abundance, k))
    pathway_data.update(alpha_amylase(relative_abundance, k))
    pathway_data.update(beta_glucosidase(relative_abundance, k))
    pathway_data.update(pullulanase(relative_abundance, k))
    pathway_data.update(ammonia_oxidation_amo_pmmo(relative_abundance, k))
    pathway_data.update(nitrite_oxidation(relative_abundance, k))
    pathway_data.update(dissim_nitrate_reduction(relative_abundance, k))
    pathway_data.update(DNRA(relative_abundance, k))
    pathway_data.update(nitrite_reduction(relative_abundance, k))
    pathway_data.update(nitric_oxide_reduction(relative_abundance, k))
    pathway_data.update(nitrous_oxide_reduction(relative_abundance, k))
    pathway_data.update(nitrogen_fixation(relative_abundance, k))
    pathway_data.update(hydroxylamine_oxidation(relative_abundance, k))
    pathway_data.update(hydrazine_dehydrogenase(relative_abundance, k))
    pathway_data.update(hydrazine_synthase(relative_abundance, k))
    pathway_data.update(dissimilatory_sulfate_to_APS(relative_abundance, k))
    pathway_data.update(dissimilatory_sulfite_to_APS(relative_abundance, k))
    pathway_data.update(
        dissimilatory_sulfite_to_sulfide(relative_abundance, k))
    pathway_data.update(thiosulfate_oxidation(relative_abundance, k))
    pathway_data.update(alt_thiosulfate_oxidation_tsdA(relative_abundance, k))
    pathway_data.update(alt_thiosulfate_oxidation_doxAD(relative_abundance, k))
    pathway_data.update(sulfur_reductase_sreABC(relative_abundance, k))
    pathway_data.update(
        thiosulfate_or_polysulfide_reductase(relative_abundance, k))
    pathway_data.update(sulfhydrogenase(relative_abundance, k))
    pathway_data.update(sulfur_disproportionation(relative_abundance, k))
    pathway_data.update(sulfur_dioxygenase(relative_abundance, k))
    pathway_data.update(sulfite_dehydrogenase(relative_abundance, k))
    pathway_data.update(sulfite_dehydrogenase_quinone(relative_abundance, k))
    pathway_data.update(sulfide_oxidation(relative_abundance, k))
    pathway_data.update(sulfur_assimilation(relative_abundance, k))
    pathway_data.update(DMSP_demethylation(relative_abundance, k))
    pathway_data.update(DMS_dehydrogenase(relative_abundance, k))
    pathway_data.update(DMSO_reductase(relative_abundance, k))
    pathway_data.update(NiFe_hydrogenase(relative_abundance, k))
    pathway_data.update(ferredoxin_hydrogenase(relative_abundance, k))
    pathway_data.update(membrane_bound_hydrogenase(relative_abundance, k))
    pathway_data.update(hydrogen_quinone_oxidoreductase(relative_abundance, k))
    pathway_data.update(NAD_reducing_hydrogenase(relative_abundance, k))
    pathway_data.update(NADP_reducing_hydrogenase(relative_abundance, k))
    pathway_data.update(NiFe_hydrogenase_Hyd_one(relative_abundance, k))
    pathway_data.update(thiamin_biosynthesis(relative_abundance, k))
    pathway_data.update(riboflavin_biosynthesis(relative_abundance, k))
    pathway_data.update(cobalamin_biosynthesis(relative_abundance, k))
    pathway_data.update(transporter_vitamin_B12(relative_abundance, k))
    pathway_data.update(transporter_thiamin(relative_abundance, k))
    pathway_data.update(transporter_urea(relative_abundance, k))
    pathway_data.update(transporter_phosphonate(relative_abundance, k))
    pathway_data.update(transporter_phosphate(relative_abundance, k))
    pathway_data.update(Flagellum(relative_abundance, k))
    pathway_data.update(Chemotaxis(relative_abundance, k))
    pathway_data.update(Methanogenesis_via_methanol(relative_abundance, k))
    pathway_data.update(Methanogenesis_via_acetate(relative_abundance, k))
    pathway_data.update(Methanogenesis_via_dimethylsulfide_methanethiol_methylpropano(
        relative_abundance, k))
    pathway_data.update(Methanogenesis_via_methylamine(relative_abundance, k))
    pathway_data.update(
        Methanogenesis_via_trimethylamine(relative_abundance, k))
    pathway_data.update(
        Methanogenesis_via_dimethylamine(relative_abundance, k))
    pathway_data.update(Methanogenesis_via_CO2(relative_abundance, k))
    pathway_data.update(
        Coenzyme_B_Coenzyme_M_regeneration(relative_abundance, k))
    pathway_data.update(Coenzyme_M_reduction_to_methane(relative_abundance, k))
    pathway_data.update(
        dimethylamine_or_trimethylamine_dehydrogenase(relative_abundance, k))
    pathway_data.update(Soluble_methane_monooxygenase(relative_abundance, k))
    pathway_data.update(methanol_dehydrogenase(relative_abundance, k))
    pathway_data.update(alcohol_oxidase(relative_abundance, k))
    pathway_data.update(Photosystem_II(relative_abundance, k))
    pathway_data.update(Photosystem_I(relative_abundance, k))
    pathway_data.update(Cytochrome_b6_f_complex(relative_abundance, k))
    pathway_data.update(
        anoxygenic_type_II_reaction_center(relative_abundance, k))
    pathway_data.update(
        anoxygenic_type_I_reaction_center(relative_abundance, k))
    pathway_data.update(Retinal_biosynthesis(relative_abundance, k))
    pathway_data.update(Entner_Doudoroff_Pathway(relative_abundance, k))
    pathway_data.update(Mixed_acid_Lactate(relative_abundance, k))
    pathway_data.update(Mixed_acid_Formate(relative_abundance, k))
    pathway_data.update(
        Mixed_acid_Formate_to_CO2_and_H2(relative_abundance, k))
    pathway_data.update(Mixed_acid_Acetate(relative_abundance, k))
    pathway_data.update(
        Mixed_acid_Ethanol_Acetate_to_Acetylaldehyde(relative_abundance, k))
    pathway_data.update(
        Mixed_acid_Ethanol_Acetyl_CoA_to_Acetylaldehyde_revers(relative_abundance, k))
    pathway_data.update(
        Mixed_acid_Ethanol_Acetylaldehyde_to_Ethanol(relative_abundance, k))
    pathway_data.update(
        Mixed_acid_PEP_to_Succ_via_OAA_malate_fuma(relative_abundance, k))
    pathway_data.update(
        Naphthalene_degradation_to_salicylate(relative_abundance, k))
    pathway_data.update(Biofilm_PGA_Synthesis_protein(relative_abundance, k))
    pathway_data.update(
        Colanic_acid_and_Biofilm_transcriptional_regulator(relative_abundance, k))
    pathway_data.update(Biofilm_regulator_BssS(relative_abundance, k))
    pathway_data.update(
        Colanic_acid_and_Biofilm_protein_A(relative_abundance, k))
    pathway_data.update(Curli_fimbriae_biosynthesis(relative_abundance, k))
    pathway_data.update(Adhesion(relative_abundance, k))
    pathway_data.update(
        Competence_related_core_components(relative_abundance, k))
    pathway_data.update(
        Competence_related_related_components(relative_abundance, k))
    pathway_data.update(Competence_factors(relative_abundance, k))
    pathway_data.update(Glyoxylate_shunt(relative_abundance, k))
    pathway_data.update(Anaplerotic_genes(relative_abundance, k))
    pathway_data.update(Sulfolipid_biosynthesis(relative_abundance, k))
    pathway_data.update(C_P_lyase_cleavage_PhnJ(relative_abundance, k))
    pathway_data.update(CP_lyase_complex(relative_abundance, k))
    pathway_data.update(CP_lyase_operon(relative_abundance, k))
    pathway_data.update(Type_I_Secretion(relative_abundance, k))
    pathway_data.update(Type_III_Secretion(relative_abundance, k))
    pathway_data.update(Type_II_Secretion(relative_abundance, k))
    pathway_data.update(Type_IV_Secretion(relative_abundance, k))
    pathway_data.update(Type_VI_Secretion(relative_abundance, k))
    pathway_data.update(Sec_SRP(relative_abundance, k))
    pathway_data.update(Twin_Arginine_Targeting(relative_abundance, k))
    pathway_data.update(Type_Vabc_Secretion(relative_abundance, k))
    pathway_data.update(
        Serine_pathway_or_formaldehyde_assimilation(relative_abundance, k))
    pathway_data.update(Arsenic_reduction(relative_abundance, k))

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
