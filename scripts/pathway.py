"""
Provides formulas calculating the abundance of every pathway
"""


class Pathway:
    """
    Define pathways
    """

    def __init__(self, abundance, bn):
        self.abundance = abundance  # input relative abundance dictionary
        self.bn = bn  # input sample's basename
        self.out_data = {}  # output calculated dictionary

    def Photosystem_II(self):
        ko_list = [self.bn+'_K02703', self.bn+'_K02704',
                   self.bn+'_K02705', self.bn+'_K02706',
                   self.bn+'_K02707', self.bn+'_K02708']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Photosystem II (psbABCDEF)'] = (
            self.abundance[self.bn+'_K02703'] +
            self.abundance[self.bn+'_K02704'] +
            self.abundance[self.bn+'_K02705'] +
            self.abundance[self.bn+'_K02706'] +
            self.abundance[self.bn+'_K02707'] +
            self.abundance[self.bn+'_K02708'])/6

    def Photosystem_I(self):
        ko_list = [self.bn+'_K02689', self.bn+'_K02690',
                   self.bn+'_K02691', self.bn+'_K02692',
                   self.bn+'_K02693', self.bn+'_K02694']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Photosystem I (psaABCDEF)'] = (
            self.abundance[self.bn+'_K02689'] +
            self.abundance[self.bn+'_K02690'] +
            self.abundance[self.bn+'_K02691'] +
            self.abundance[self.bn+'_K02692'] +
            self.abundance[self.bn+'_K02693'] +
            self.abundance[self.bn+'_K02694'])/6

    def Cytochrome_b6_f_complex(self):
        ko_list = [self.bn+'_K02635', self.bn+'_K02637',
                   self.bn+'_K02634', self.bn+'_K02636',
                   self.bn+'_K02642', self.bn+'_K02643',
                   self.bn+'_K03689', self.bn+'_K02640']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Cytochrome b6/f complex (petABCDGLMN)'] = (
            self.abundance[self.bn+'_K02635'] +
            self.abundance[self.bn+'_K02637'] +
            self.abundance[self.bn+'_K02634'] +
            self.abundance[self.bn+'_K02636'] +
            self.abundance[self.bn+'_K02642'] +
            self.abundance[self.bn+'_K02643'] +
            self.abundance[self.bn+'_K03689'] +
            self.abundance[self.bn+'_K02640'])/8

    def anoxygenic_photosystem_II_pufML(self):
        ko_list = [self.bn+'_K08929', self.bn+'_K08928']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Anoxygenic photosystem II (pufML)'] = (
            self.abundance[self.bn+'_K08928'] +
            self.abundance[self.bn+'_K08929'])/2

    def anoxygenic_photosystem_I_pscABCD(self):
        ko_list = [self.bn+'_K08940', self.bn+'_K08941',
                   self.bn+'_K08942', self.bn+'_K08943']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Anoxygenic photosystem I (pscABCD)'] = (
            self.abundance[self.bn+'_K08940'] +
            self.abundance[self.bn+'_K08941'] +
            self.abundance[self.bn+'_K08942'] +
            self.abundance[self.bn+'_K08943'])/4

    def RuBisCo(self):
        ko_list = [self.bn+'_K01601']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['RuBisCo'] = self.abundance[self.bn+'_K01601']

    #def CBB_Cycle(self):
        #ko_list = [self.bn+'_K00855', self.bn+'_K01601', self.bn+'_K00927',
                   #self.bn+'_K05298', self.bn+'_K00150', self.bn+'_K00134',
                   #self.bn+'_K01623', self.bn+'_K01624', self.bn+'_K03841',
                   #self.bn+'_K02446', self.bn+'_K11532', self.bn+'_K01086',
                   #self.bn+'_K04041', self.bn+'_K00615', self.bn+'_K01100',
                   #self.bn+'_K01807', self.bn+'_K01808']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['CBB cycle'] = (
          #self.abundance[self.bn+'_K00855'] +
          #self.abundance[self.bn+'_K01601'] +
          #self.abundance[self.bn+'_K00927'] +
          #self.abundance[self.bn+'_K05298'] +
          #self.abundance[self.bn+'_K00150'] +
          #self.abundance[self.bn+'_K00134'] +
          #self.abundance[self.bn+'_K01623'] +
          #self.abundance[self.bn+'_K01624'] +
          #self.abundance[self.bn+'_K03841'] +
          #self.abundance[self.bn+'_K02446'] +
          #self.abundance[self.bn+'_K11532'] +
          #self.abundance[self.bn+'_K01086'] +
          #self.abundance[self.bn+'_K04041'] +
          #self.abundance[self.bn+'_K00615'] +
          #self.abundance[self.bn+'_K01623'] +
          #self.abundance[self.bn+'_K01624'] +
          #self.abundance[self.bn+'_K01100'] +
          #self.abundance[self.bn+'_K11532'] +
          #self.abundance[self.bn+'_K01086'] +
          #self.abundance[self.bn+'_K00615'] +
          #self.abundance[self.bn+'_K01623'] +
          #self.abundance[self.bn+'_K01624'] +
          #self.abundance[self.bn+'_K01100'] +
          #self.abundance[self.bn+'_K11532'] +
          #self.abundance[self.bn+'_K01086'] +
          #self.abundance[self.bn+'_K00615'] +
          #self.abundance[self.bn+'_K01807'] +
          #self.abundance[self.bn+'_K01808'])/11

    def CBB_Cycle(self):
        ko_list = [self.bn+'_K00855']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['CBB cycle (prkB)'] = self.abundance[self.bn+'_K00855']

    def rTCA_Cycle(self):
        ko_list = [self.bn+'_K15230', self.bn+'_K15231',
                   self.bn+'_K15232', self.bn+'_K15233',
                   self.bn+'_K15234']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['rTCA cycle (aclAB, ccsAB, ccl)'] = (
            (self.abundance[self.bn+'_K15230'] +
             self.abundance[self.bn+'_K15231'])/2 +
            ((self.abundance[self.bn+'_K15232'] +
              self.abundance[self.bn+'_K15233'])/2 +
             self.abundance[self.bn+'_K15234'])/2)

    #def Wood_Ljungdahl(self):
        #ko_list = [self.bn+'_K00198', self.bn+'_K05299', self.bn+'_K01938',
                   #self.bn+'_K01491', self.bn+'_K00297', self.bn+'_K15023',
                   #self.bn+'_K14138', self.bn+'_K00197', self.bn+'_K00194']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Wood-Ljungdahl'] = (
          #self.abundance[self.bn+'_K00198'] +
          #self.abundance[self.bn+'_K05299'] +
          #self.abundance[self.bn+'_K01938'] +
          #self.abundance[self.bn+'_K01491'] +
          #self.abundance[self.bn+'_K00297'] +
          #self.abundance[self.bn+'_K15023'] +
          #(self.abundance[self.bn+'_K14138'] +
           #self.abundance[self.bn+'_K00197'] +
           #self.abundance[self.bn+'_K00194'])/3)/7

    def Wood_Ljungdahl(self):
        ko_list = [self.bn+'_K00198', self.bn+'_K14138',
                   self.bn+'_K00197', self.bn+'_K00194',
                   self.bn+'_K15023']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Wood-Ljungdahl pathway (acsABCDE)'] = (
            self.abundance[self.bn+'_K00198'] +
            self.abundance[self.bn+'_K14138'] +
            self.abundance[self.bn+'_K00197'] +
            self.abundance[self.bn+'_K00194'] +
            self.abundance[self.bn+'_K15023'])/5

    #def three_Hydroxypropionate_Bicycle(self):
        #ko_list = [self.bn+'_K02160', self.bn+'_K01961', self.bn+'_K01962',
                   #self.bn+'_K01963', self.bn+'_K14468', self.bn+'_K14469',
                   #self.bn+'_K08691', self.bn+'_K14449', self.bn+'_K14470',
                   #self.bn+'_K09709', self.bn+'_K15052', self.bn+'_K05606',
                   #self.bn+'_K01847', self.bn+'_K01848', self.bn+'_K01849',
                   #self.bn+'_K14471', self.bn+'_K14472', self.bn+'_K00239',
                   #self.bn+'_K00240', self.bn+'_K00241', self.bn+'_K01679']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['3-Hydroxypropionate Bicycle'] = (
          #(self.abundance[self.bn+'_K02160'] +
           #self.abundance[self.bn+'_K01961'] +
           #self.abundance[self.bn+'_K01962'] +
           #self.abundance[self.bn+'_K01963'])/4 +
          #self.abundance[self.bn+'_K14468'] +
          #self.abundance[self.bn+'_K14469'] +
          #self.abundance[self.bn+'_K08691'] +
          #self.abundance[self.bn+'_K14449'] +
          #self.abundance[self.bn+'_K14470'] +
          #self.abundance[self.bn+'_K09709'] +
          #self.abundance[self.bn+'_K08691'] +
          #self.abundance[self.bn+'_K15052'] +
          #self.abundance[self.bn+'_K05606'] +
          #self.abundance[self.bn+'_K01847'] +
          #(self.abundance[self.bn+'_K01848'] +
           #self.abundance[self.bn+'_K01849'])/2 +
          #(self.abundance[self.bn+'_K14471'] +
           #self.abundance[self.bn+'_K14472'])/2 +
          #(self.abundance[self.bn+'_K00239'] +
           #self.abundance[self.bn+'_K00240'] +
           #self.abundance[self.bn+'_K00241'])/3 +
          #self.abundance[self.bn+'_K01679'] +
          #(self.abundance[self.bn+'_K14471'] +
           #self.abundance[self.bn+'_K14472'])/2 +
          #self.abundance[self.bn+'_K08691'])/16

    def three_Hydroxypropionate_Bicycle(self):
        ko_list = [self.bn+'_K14468', self.bn+'_K15052',
                   self.bn+'_K08691', self.bn+'_K14469',
                   self.bn+'_K14470', self.bn+'_K09709']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['3-Hydroxypropionate Bicycle'] = (
            self.abundance[self.bn+'_K14468'] +
            self.abundance[self.bn+'_K15052'] +
            self.abundance[self.bn+'_K08691'] +
            self.abundance[self.bn+'_K14469'] +
            self.abundance[self.bn+'_K14470'] +
            self.abundance[self.bn+'_K09709'])/6

    #def Dicarboxylate_hydroxybutyrate_cycle(self):
        #ko_list = [self.bn+'_K00169', self.bn+'_K00170', self.bn+'_K00171',
                   #self.bn+'_K00172', self.bn+'_K01007', self.bn+'_K01595',
                   #self.bn+'_K00024', self.bn+'_K01676', self.bn+'_K01677',
                   #self.bn+'_K01678', self.bn+'_K00239', self.bn+'_K00240',
                   #self.bn+'_K01902', self.bn+'_K01903', self.bn+'_K15038',
                   #self.bn+'_K15017', self.bn+'_K14465', self.bn+'_K14467',
                   #self.bn+'_K18861', self.bn+'_K14534', self.bn+'_K15016',
                   #self.bn+'_K00626']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Dicarboxylate-hydroxybutyrate cycle'] = (
          #(self.abundance[self.bn+'_K00169'] +
           #self.abundance[self.bn+'_K00170'] +
           #self.abundance[self.bn+'_K00171'] +
           #self.abundance[self.bn+'_K00172'])/4 +
          #self.abundance[self.bn+'_K01007'] +
          #self.abundance[self.bn+'_K01595'] +
          #self.abundance[self.bn+'_K00024'] +
          #self.abundance[self.bn+'_K01676'] +
          #(self.abundance[self.bn+'_K01677'] +
           #self.abundance[self.bn+'_K01678'])/2 +
          #(self.abundance[self.bn+'_K00239'] +
           #self.abundance[self.bn+'_K00240'])/2 +
          #(self.abundance[self.bn+'_K01902'] +
           #self.abundance[self.bn+'_K01903'])/2 +
          #self.abundance[self.bn+'_K15038'] +
          #self.abundance[self.bn+'_K15017'] +
          #self.abundance[self.bn+'_K14465'] +
          #self.abundance[self.bn+'_K14467'] +
          #self.abundance[self.bn+'_K18861'] +
          #self.abundance[self.bn+'_K14534'] +
          #self.abundance[self.bn+'_K15016'] +
          #self.abundance[self.bn+'_K15016'] +
          #self.abundance[self.bn+'_K00626'])/14

    #def pectinesterase(self):
        #ko_list = [self.bn+'_K01051']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Pectinesterase'] = self.abundance[self.bn+'_K01051']

    #def diacetylchitobiose_deacetylase(self):
        #ko_list = [self.bn+'_K18454', self.bn+'_K03478']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Diacetylchitobiose deacetylase'] = (self.abundance[self.bn+'_K18454'] +
                                                           #self.abundance[self.bn+'_K03478'])

    #def glucoamylase(self):
        #ko_list = [self.bn+'_K01178']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Glucoamylase'] = self.abundance[self.bn+'_K01178']

    #def D_galacturonate_epimerase(self):
        #ko_list = [self.bn+'_K08679']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['D-galacturonate epimerase'] = self.abundance[self.bn+'_K08679']

    #def exo_poly_alpha_galacturonosidase(self):
        #ko_list = [self.bn+'_K18650']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['exo-poly-alpha-galacturonosidase'] = self.abundance[self.bn+'_K18650']

    #def oligogalacturonide_lyase(self):
        #ko_list = [self.bn+'_K01730']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Oligogalacturonide lyase'] = self.abundance[self.bn+'_K01730']

    #def cellulase(self):
        #ko_list = [self.bn+'_K19668', self.bn+'_K01225']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Cellulase'] = self.abundance[self.bn+'_K19668']+self.abundance[self.bn+'_K01225']

    #def exopolygalacturonase(self):
        #ko_list = [self.bn+'_K01184']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['exopolygalacturonase'] = self.abundance[self.bn+'_K01184']

    #def chitinase(self):
        #ko_list = [self.bn+'_K01183']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Chitinase'] = self.abundance[self.bn+'_K01183']

    #def basic_endochitinase_B(self):
        #ko_list = [self.bn+'_K20547']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Basic endochitinase B'] = self.abundance[self.bn+'_K20547']

    #def bifunctional_chitinase_or_lysozyme(self):
        #ko_list = [self.bn+'_K13381']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Bifunctional chitinase/lysozyme'] = self.abundance[self.bn+'_K13381']

    #def beta_N_acetylhexosaminidase(self):
        #ko_list = [self.bn+'_K01207']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Beta-N-acetylhexosaminidase'] = self.abundance[self.bn+'_K01207']

    #def D_galacturonate_isomerase(self):
        #ko_list = [self.bn+'_K01812']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['D-galacturonate isomerase'] = self.abundance[self.bn+'_K01812']

    #def alpha_amylase(self):
        #ko_list = [self.bn+'_K01176']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Alpha-amylase'] = self.abundance[self.bn+'_K01176']

    #def beta_glucosidase(self):
        #ko_list = [self.bn+'_K05349', self.bn+'_K05350']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Beta-glucosidase'] = self.abundance[self.bn+'_K05350']+self.abundance[self.bn+'_K05349']

    #def pullulanase(self):
        #ko_list = [self.bn+'_K01200']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Pullulanase'] = self.abundance[self.bn+'_K01200']

    #def glycolysis(self):
        #ko_list = [self.bn+'_K00844', self.bn+'_K12407', self.bn+'_K00845',
                   #self.bn+'_K00886', self.bn+'_K08074', self.bn+'_K01810',
                   #self.bn+'_K06859', self.bn+'_K13810', self.bn+'_K12406',
                   #self.bn+'_K15916', self.bn+'_K00850', self.bn+'_K16370',
                   #self.bn+'_K00918', self.bn+'_K01623', self.bn+'_K01689',
                   #self.bn+'_K11645', self.bn+'_K16305', self.bn+'_K16306',
                   #self.bn+'_K00873', self.bn+'_K01624', self.bn+'_K15635',
                   #self.bn+'_K16305', self.bn+'_K01803', self.bn+'_K11389',
                   #self.bn+'_K00134', self.bn+'_K15633', self.bn+'_K00927',
                   #self.bn+'_K01834', self.bn+'_K15634']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Glycolysis'] = (self.abundance[self.bn+'_K00844'] +
                                  #self.abundance[self.bn+'_K12407'] +
                                  #self.abundance[self.bn+'_K00845'] +
                                  #self.abundance[self.bn+'_K00886'] +
                                  #self.abundance[self.bn+'_K08074'] +
                                  #self.abundance[self.bn+'_K00918'] +
                                  #self.abundance[self.bn+'_K01810'] +
                                  #self.abundance[self.bn+'_K06859'] +
                                  #self.abundance[self.bn+'_K13810'] +
                                  #self.abundance[self.bn+'_K15916'] +
                                  #self.abundance[self.bn+'_K00850'] +
                                  #self.abundance[self.bn+'_K16370'] +
                                  #self.abundance[self.bn+'_K00918'] +
                                  #(self.abundance[self.bn+'_K01623'] +
                                   #self.abundance[self.bn+'_K01624'] +
                                   #self.abundance[self.bn+'_K11645'] +
                                   #self.abundance[self.bn+'_K16305'] +
                                   #self.abundance[self.bn+'_K16306']) +
                                  #(self.abundance[self.bn+'_K01623'] +
                                   #self.abundance[self.bn+'_K01624'] +
                                   #self.abundance[self.bn+'_K11645'] +
                                   #self.abundance[self.bn+'_K16305'] +
                                   #self.abundance[self.bn+'_K16306'] +
                                   #self.abundance[self.bn+'_K01803'])/2 +
                                  #self.abundance[self.bn+'_K11389'] +
                                  #(self.abundance[self.bn+'_K00134'] +
                                   #self.abundance[self.bn+'_K15633'] +
                                   #self.abundance[self.bn+'_K00927'])/2 +
                                  #self.abundance[self.bn+'_K01834'] +
                                  #self.abundance[self.bn+'_K15633'] +
                                  #self.abundance[self.bn+'_K15634'] +
                                  #self.abundance[self.bn+'_K15635'] +
                                  #self.abundance[self.bn+'_K01689'] +
                                  #self.abundance[self.bn+'_K00873'] +
                                  #self.abundance[self.bn+'_K12406'])/8
    def glycolysis(self):
        ko_list = [self.bn+'_K00845', self.bn+'_K00844', self.bn+'_K00918',
                   self.bn+'_K00886', self.bn+'_K08074', self.bn+'_K00846',
                   self.bn+'_K00882', self.bn+'_K00918', self.bn+'_K00895',
                   self.bn+'_K21071', self.bn+'_K00850', self.bn+'_K16370',
                   self.bn+'_K00873']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Glycolysis (glk, pfk, pyk)'] = (self.abundance[self.bn+'_K00845'] +
                                  self.abundance[self.bn+'_K00844'] +
                                  self.abundance[self.bn+'_K00918'] +
                                  self.abundance[self.bn+'_K00886'] +
                                  self.abundance[self.bn+'_K08074'] +
                                  self.abundance[self.bn+'_K00846'] +
                                  self.abundance[self.bn+'_K00882'] +
                                  self.abundance[self.bn+'_K00918'] +
                                  self.abundance[self.bn+'_K00895'] +
                                  self.abundance[self.bn+'_K21071'] +
                                  self.abundance[self.bn+'_K00850'] +
                                  self.abundance[self.bn+'_K16370'] +
                                  self.abundance[self.bn+'_K00873'])/3

    def Entner_Doudoroff_Pathway(self):
        ko_list = [self.bn+'_K00036', self.bn+'_K01057',
                   self.bn+'_K07404', self.bn+'_K01690',
                   self.bn+'_K01625']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Entner-Doudoroff pathway, glucose-6P -> glyceraldehyde-3P + pyruvate'] = (
            self.abundance[self.bn+'_K00036'] +
            self.abundance[self.bn+'_K01057'] +
            self.abundance[self.bn+'_K07404'] +
            self.abundance[self.bn+'_K01690'] +
            self.abundance[self.bn+'_K01625'])/4

    #def gluconeogenesis(self):
        #ko_list = [self.bn+'_K01596', self.bn+'_K01610', self.bn+'_K01689',
                   #self.bn+'_K01834', self.bn+'_K15633', self.bn+'_K15634',
                   #self.bn+'_K15635', self.bn+'_K00927', self.bn+'_K00134',
                   #self.bn+'_K00150', self.bn+'_K01803', self.bn+'_K11645',
                   #self.bn+'_K01623', self.bn+'_K01624', self.bn+'_K01622',
                   #self.bn+'_K03841', self.bn+'_K02446', self.bn+'_K11532',
                   #self.bn+'_K01086', self.bn+'_K04041']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Gluconeogenesis, oxaloacetate -> fructose-6P'] = (self.abundance[self.bn+'_K01596'] +
                                       #self.abundance[self.bn+'_K01610'] +
                                       #self.abundance[self.bn+'_K01689'] +
                                       #self.abundance[self.bn+'_K01834'] +
                                       #self.abundance[self.bn+'_K15633'] +
                                       #self.abundance[self.bn+'_K15634'] +
                                       #self.abundance[self.bn+'_K15635'] +
                                       #self.abundance[self.bn+'_K00927'] +
                                       #self.abundance[self.bn+'_K00134'] +
                                       #self.abundance[self.bn+'_K00150'] +
                                       #(self.abundance[self.bn+'_K01803'] +
                                        #self.abundance[self.bn+'_K01623'] +
                                        #self.abundance[self.bn+'_K01624'] +
                                        #self.abundance[self.bn+'_K11645'])/2 +
                                       #self.abundance[self.bn+'_K01623'] +
                                       #self.abundance[self.bn+'_K01624'] +
                                       #self.abundance[self.bn+'_K11645'] +
                                       #self.abundance[self.bn+'_K01622'] +
                                       #self.abundance[self.bn+'_K03841'] +
                                       #self.abundance[self.bn+'_K02446'] +
                                       #self.abundance[self.bn+'_K11532'] +
                                       #self.abundance[self.bn+'_K01086'] +
                                       #self.abundance[self.bn+'_K04041'])/7

    def gluconeogenesis(self):
        ko_list = [self.bn+'_K03841', self.bn+'_K02446',
                   self.bn+'_K04041', self.bn+'_K01622',
                   self.bn+'_K00895', self.bn+'_K21071',
                   self.bn+'_K01610', self.bn+'_K01596']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Gluconeogenesis (fbp, pck)'] = (
            self.abundance[self.bn+'_K03841'] +
            self.abundance[self.bn+'_K02446'] +
            self.abundance[self.bn+'_K04041'] +
            self.abundance[self.bn+'_K01622'] +
            self.abundance[self.bn+'_K00895'] +
            self.abundance[self.bn+'_K21071'] +
            self.abundance[self.bn+'_K01610'] +
            self.abundance[self.bn+'_K01596'])/2


    def tca_cycle(self):
        ko_list = [self.bn+'_K01647', self.bn+'_K05942', self.bn+'_K01681',
                   self.bn+'_K01682', self.bn+'_K00031', self.bn+'_K00030',
                   self.bn+'_K00174', self.bn+'_K00175', self.bn+'_K00164',
                   self.bn+'_K00658', self.bn+'_K00382', self.bn+'_K01902',
                   self.bn+'_K01903', self.bn+'_K01899', self.bn+'_K01900',
                   self.bn+'_K18118', self.bn+'_K00234', self.bn+'_K00235',
                   self.bn+'_K00236', self.bn+'_K00237', self.bn+'_K00239',
                   self.bn+'_K00240', self.bn+'_K00241', self.bn+'_K00244',
                   self.bn+'_K00245', self.bn+'_K00246', self.bn+'_K01676',
                   self.bn+'_K01679', self.bn+'_K01677', self.bn+'_K01678',
                   self.bn+'_K00026', self.bn+'_K00025', self.bn+'_K00024',
                   self.bn+'_K00116']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['TCA cycle'] = (
            (self.abundance[self.bn+'_K01647'] +
             self.abundance[self.bn+'_K05942']) +
            (self.abundance[self.bn+'_K01681'] +
             self.abundance[self.bn+'_K01682']) +
            (self.abundance[self.bn+'_K00031'] +
             self.abundance[self.bn+'_K00030']) +
            (self.abundance[self.bn+'_K00174'] +
             self.abundance[self.bn+'_K00175'])/2 +
            (self.abundance[self.bn+'_K00164'] +
             self.abundance[self.bn+'_K00658'] +
             self.abundance[self.bn+'_K00382'])/3 +
            (self.abundance[self.bn+'_K01902'] +
             self.abundance[self.bn+'_K01903'])/2 +
            (self.abundance[self.bn+'_K01899'] +
             self.abundance[self.bn+'_K01900'])/2 +
            self.abundance[self.bn+'_K18118'] +
            (self.abundance[self.bn+'_K00234'] +
             self.abundance[self.bn+'_K00235'] +
             self.abundance[self.bn+'_K00236'] +
             self.abundance[self.bn+'_K00237'])/4 +
            (self.abundance[self.bn+'_K00239'] +
             self.abundance[self.bn+'_K00240'] +
             self.abundance[self.bn+'_K00241'])/3 +
            (self.abundance[self.bn+'_K00244'] +
             self.abundance[self.bn+'_K00245'] +
             self.abundance[self.bn+'_K00246'])/3 +
            self.abundance[self.bn+'_K01676'] +
            self.abundance[self.bn+'_K01679'] +
            (self.abundance[self.bn+'_K01677'] +
             self.abundance[self.bn+'_K01678'])/2 +
            self.abundance[self.bn+'_K00026'] +
            self.abundance[self.bn+'_K00025'] +
            self.abundance[self.bn+'_K00024'] +
            self.abundance[self.bn+'_K00116'])/8

    def Methanogenesis(self):
        ko_list = [self.bn+'_K00399', self.bn+'_K00401',
                   self.bn+'_K00402']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Methanogenesis (mcrABG)'] = (
            self.abundance[self.bn+'_K00399'] +
            self.abundance[self.bn+'_K00401'] +
            self.abundance[self.bn+'_K00402'])/3

    def Methanogenesis_via_methanol(self):
        ko_list = [self.bn+'_K04480', self.bn+'_K14080',
                   self.bn+'_K14081']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Methanogenesis, methanol -> methane (mtaABC)'] = (
            self.abundance[self.bn+'_K04480'] +
            self.abundance[self.bn+'_K14080'] +
            self.abundance[self.bn+'_K14081'])/3

    #def Methanogenesis_via_methylamine(self):
        #ko_list = [self.bn+'_K14082', self.bn+'_K16177',
                   #self.bn+'_K00399', self.bn+'_K00401',
                   #self.bn+'_K00402']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Methanogenesis, methylamine -> methane'] = (
          #(self.abundance[self.bn+'_K14082'] +
           #self.abundance[self.bn+'_K16177'])/2 +
          #(self.abundance[self.bn+'_K00399'] +
           #self.abundance[self.bn+'_K00401'] +
           #self.abundance[self.bn+'_K00402'])/3)/2

    #def Methanogenesis_via_dimethylamine(self):
        #ko_list = [self.bn+'_K14082', self.bn+'_K16179',
                   #self.bn+'_K00399', self.bn+'_K00401',
                   #self.bn+'_K00402']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Methanogenesis, dimethylamine -> methane'] = (
          #(self.abundance[self.bn+'_K14082'] +
           #self.abundance[self.bn+'_K16179'])/2 +
          #(self.abundance[self.bn+'_K00399'] +
           #self.abundance[self.bn+'_K00401'] +
           #self.abundance[self.bn+'_K00402'])/3)/2

    #def Methanogenesis_via_trimethylamine(self):
        #ko_list = [self.bn+'_K14082', self.bn+'_K14084',
                   #self.bn+'_K00399', self.bn+'_K00401',
                   #self.bn+'_K00402']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Methanogenesis, trimethylamine -> methane'] = (
          #(self.abundance[self.bn+'_K14082'] +
           #self.abundance[self.bn+'_K14084'])/2 +
          #(self.abundance[self.bn+'_K00399'] +
           #self.abundance[self.bn+'_K00401'] +
           #self.abundance[self.bn+'_K00402'])/3)/2

    def Methanogenesis_via_amines(self):
        ko_list = [self.bn+'_K14082', self.bn+'_K14084',
                   self.bn+'_K16179', self.bn+'_K16177']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Methanogenesis, amines -> methane (mtbA, mtmC, mtbC, mttC)'] = (
            self.abundance[self.bn+'_K14082'] +
            self.abundance[self.bn+'_K14084'] +
            self.abundance[self.bn+'_K16179'] +
            self.abundance[self.bn+'_K16177'])/4


    #def Methanogenesis_via_acetate(self):
        #ko_list = [self.bn+'_K00925', self.bn+'_K00625', self.bn+'_K13788',
                   #self.bn+'_K01895', self.bn+'_K00193', self.bn+'_K00194',
                   #self.bn+'_K00197', self.bn+'_K00577', self.bn+'_K00578',
                   #self.bn+'_K00579', self.bn+'_K00580', self.bn+'_K00581',
                   #self.bn+'_K00584', self.bn+'_K00399', self.bn+'_K00401',
                   #self.bn+'_K00402']
        #for ko in ko_list:
            #if ko not in self.abundance:
                #self.abundance[ko] = 0
        #self.out_data['Methanogenesis, acetate -> methane'] = (
          #(self.abundance[self.bn+'_K00925'] +
           #self.abundance[self.bn+'_K00625'] +
           #self.abundance[self.bn+'_K13788'])/2 +
          #self.abundance[self.bn+'_K01895'] +
          #(self.abundance[self.bn+'_K00193'] +
           #self.abundance[self.bn+'_K00194'] +
           #self.abundance[self.bn+'_K00197'])/3 +
          #(self.abundance[self.bn+'_K00577'] +
           #self.abundance[self.bn+'_K00578'] +
           #self.abundance[self.bn+'_K00579'] +
           #self.abundance[self.bn+'_K00580'] +
           #self.abundance[self.bn+'_K00581'] +
           #self.abundance[self.bn+'_K00584'])/6 +
          #(self.abundance[self.bn+'_K00399'] +
           #self.abundance[self.bn+'_K00401'] +
           #self.abundance[self.bn+'_K00402'])/3)/4

    def Methanogenesis_via_acetate(self):
        ko_list = [self.bn+'_K00193', self.bn+'_K00194',
                   self.bn+'_K00197']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Methanogenesis, acetate -> methane (cdhCDE)'] = (
            self.abundance[self.bn+'_K00193'] +
            self.abundance[self.bn+'_K00194'] +
            self.abundance[self.bn+'_K00197'])/3

    def Methanogenesis_CO2_methane(self):
        ko_list = [self.bn+'_K00200', self.bn+'_K00201', self.bn+'_K00202',
                   self.bn+'_K00203', self.bn+'_K11261', self.bn+'_K00205',
                   self.bn+'_K11260', self.bn+'_K00204', self.bn+'_K00672',
                   self.bn+'_K01499', self.bn+'_K00319', self.bn+'_K13942',
                   self.bn+'_K00320', self.bn+'_K00577', self.bn+'_K00578',
                   self.bn+'_K00579', self.bn+'_K00580', self.bn+'_K00581',
                   self.bn+'_K00584']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Methanogenesis, CO2 -> methane'] = (
          (self.abundance[self.bn+'_K00200'] +
           self.abundance[self.bn+'_K00201'] +
           self.abundance[self.bn+'_K00202'] +
           self.abundance[self.bn+'_K00203'] +
           self.abundance[self.bn+'_K11261'] +
           self.abundance[self.bn+'_K00205'] +
           self.abundance[self.bn+'_K11260'] +
           self.abundance[self.bn+'_K00204'])/6 +
          self.abundance[self.bn+'_K00672'] +
          self.abundance[self.bn+'_K01499'] +
          self.abundance[self.bn+'_K00319'] +
          self.abundance[self.bn+'_K13942'] +
          self.abundance[self.bn+'_K00320'] +
          (self.abundance[self.bn+'_K00577'] +
           self.abundance[self.bn+'_K00578'] +
           self.abundance[self.bn+'_K00579'] +
           self.abundance[self.bn+'_K00580'] +
           self.abundance[self.bn+'_K00581'] +
           self.abundance[self.bn+'_K00584'])/6)/6

    def Methane_oxidation_methane_methanol(self):
        ko_list = [self.bn+'_K16157', self.bn+'_K16158', self.bn+'_K16159',
                   self.bn+'_K16160', self.bn+'_K16161', self.bn+'_K16162',
                   self.bn+'_K10944', self.bn+'_K10945', self.bn+'_K10946']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Methane oxidation, methane -> methanol (mmoBCDXYZ, amoABC)'] = (
          (self.abundance[self.bn+'_K16157'] +
           self.abundance[self.bn+'_K16158'] +
           self.abundance[self.bn+'_K16159'] +
           self.abundance[self.bn+'_K16160'] +
           self.abundance[self.bn+'_K16161'] +
           self.abundance[self.bn+'_K16162'])/6 +
          (self.abundance[self.bn+'_K10944'] +
           self.abundance[self.bn+'_K10945'] +
           self.abundance[self.bn+'_K10946'])/3)

    def Methane_oxidation_methanol_Formaldehyde(self):
        ko_list = [self.bn+'_K14028', self.bn+'_K14029',
                   self.bn+'_K17066']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Methane oxidation, methanol -> formaldehyde (mxaFI, xoxF)'] = (
          (self.abundance[self.bn+'_K14028'] +
           self.abundance[self.bn+'_K14029'])/2 +
          self.abundance[self.bn+'_K17066'])

    def Mixed_acid_lactate(self):
        ko_list = [self.bn+'_K00016']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Fermentation to lactate, pyruvate -> lactate (LDH)'] = (
          self.abundance[self.bn+'_K00016'])

    def Mixed_acid_formate(self):
        ko_list = [self.bn+'_K00656']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Fermentation to formate, pyruvate -> formate (pf1D)'] = (
          self.abundance[self.bn+'_K00656'])

    def Mixed_acid_Formate_to_CO2_H2(self):
        ko_list = [self.bn+'_K00122', self.bn+'_K00123', self.bn+'_K00124',
                   self.bn+'_K00126', self.bn+'_K00127', self.bn+'_K22515',
                   self.bn+'_K22516', self.bn+'_K00125']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Fermentation to formate -> CO2 & H2 (fdh)'] = (
          (self.abundance[self.bn+'_K00122'] +
           self.abundance[self.bn+'_K00123'] +
           self.abundance[self.bn+'_K00124'] +
           self.abundance[self.bn+'_K00126'] +
           self.abundance[self.bn+'_K00127'] +
           self.abundance[self.bn+'_K22515'])/6 +
          (self.abundance[self.bn+'_K22516'] +
           self.abundance[self.bn+'_K00125'])/2)

    def Mixed_acid_acetate(self):
        ko_list = [self.bn+'_K00156', self.bn+'_K00158', self.bn+'_K01512',
                   self.bn+'_K00467', self.bn+'_K01067', self.bn+'_K04020',
                   self.bn+'_K13788', self.bn+'_K00625']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Fermentation to acetate'] = (
          self.abundance[self.bn+'_K00156'] +
          (self.abundance[self.bn+'_K00158'] +
           self.abundance[self.bn+'_K01512'])/2 +
          self.abundance[self.bn+'_K00467'] +
          self.abundance[self.bn+'_K01067'] +
          (self.abundance[self.bn+'_K04020'] +
           self.abundance[self.bn+'_K13788'] +
           self.abundance[self.bn+'_K00625'] +
           self.abundance[self.bn+'_K01512'])/2)

    def Mixed_acid_pyruvate_to_acetate_include_via_acetylP(self):
      ko_list = [self.bn+'_K00156', self.bn+'_K00158', self.bn+'_K01512']
      for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
      self.out_data['Fermentation to acetate, pyruvate -> acetate (poxB, poxL, acyP)'] = (
        self.abundance[self.bn+'_K00156'] +
        (self.abundance[self.bn+'_K00158'] +
         self.abundance[self.bn+'_K01512'])/2)

    def Mixed_acid_acetyl_CoA_to_acetate_include_via_acetylP(self):
      ko_list = [self.bn+'_K01067', self.bn+'_K04020', self.bn+'_K13788',
                 self.bn+'_K00625', self.bn+'_K01512']
      for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
      self.out_data['Fermentation to acetate, acetyl-CoA -> acetate (ach1, eutD, pta, acyP)'] = (
        self.abundance[self.bn+'_K01067'] +
        (self.abundance[self.bn+'_K04020'] +
         self.abundance[self.bn+'_K13788'] +
         self.abundance[self.bn+'_K00625'] +
         self.abundance[self.bn+'_K01512'])/2)

    def Mixed_acid_lactate_to_acetate(self):
      ko_list = [self.bn+'_K00467']
      for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
      self.out_data['Fermentation to acetate, lactate -> acetate (EC:1.13.12.4)'] = (
        self.abundance[self.bn+'_K00467'])

    def Mixed_acid_Ethanol_Acetate_to_Acetylaldehyde(self):
        ko_list = [self.bn+'_K00128', self.bn+'_K14085', self.bn+'_K00149',
                   self.bn+'_K00129', self.bn+'_K00138']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Fermentation to ethanol, acetate to acetylaldehyde (ald)'] = (
          self.abundance[self.bn+'_K00128'] +
          self.abundance[self.bn+'_K14085'] +
          self.abundance[self.bn+'_K00149'] +
          self.abundance[self.bn+'_K00129'] +
          self.abundance[self.bn+'_K00138'])

    def Mixed_acid_Ethanol_Acetyl_CoA_to_Acetylaldehyde(self):
        ko_list = [self.bn+'_K00132', self.bn+'_K04072', self.bn+'_K04073',
                   self.bn+'_K18366', self.bn+'_K04021']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Fermentation to ethanol, acetyl-CoA to acetylaldehyde (reversible)'] = (
          self.abundance[self.bn+'_K00132'] +
          self.abundance[self.bn+'_K04072'] +
          self.abundance[self.bn+'_K04073'] +
          self.abundance[self.bn+'_K18366'] +
          self.abundance[self.bn+'_K04021'])

    def Mixed_acid_Ethanol_Acetylaldehyde_to_Ethanol(self):
        ko_list = [self.bn+'_K13951', self.bn+'_K13980', self.bn+'_K13952',
                   self.bn+'_K13953', self.bn+'_K13954', self.bn+'_K00001',
                   self.bn+'_K00121', self.bn+'_K04072', self.bn+'_K18857',
                   self.bn+'_K14028', self.bn+'_K14029', self.bn+'_K00114',
                   self.bn+'_K00002', self.bn+'_K04022']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Fermentation to ethanol, acetylaldehyde to ethanol (adh, mdh)'] = (
          self.abundance[self.bn+'_K13951'] +
          self.abundance[self.bn+'_K13980'] +
          self.abundance[self.bn+'_K13952'] +
          self.abundance[self.bn+'_K13953'] +
          self.abundance[self.bn+'_K13954'] +
          self.abundance[self.bn+'_K00001'] +
          self.abundance[self.bn+'_K00121'] +
          self.abundance[self.bn+'_K04072'] +
          self.abundance[self.bn+'_K18857'] +
          (self.abundance[self.bn+'_K14028'] +
           self.abundance[self.bn+'_K14029'])/2 +
          self.abundance[self.bn+'_K00114'] +
          self.abundance[self.bn+'_K00002'] +
          self.abundance[self.bn+'_K04022'])

    def Mixed_acid_succinate(self):
        ko_list = [self.bn+'_K01595', self.bn+'_K01596', self.bn+'_K20370',
                   self.bn+'_K01610', self.bn+'_K00024', self.bn+'_K00025',
                   self.bn+'_K00026', self.bn+'_K00051', self.bn+'_K00116',
                   self.bn+'_K01676', self.bn+'_K01679', self.bn+'_K01677',
                   self.bn+'_K01678', self.bn+'_K00244', self.bn+'_K00245',
                   self.bn+'_K00246', self.bn+'_K00247']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Fermentation to succinate (phosphoenolpyruvate to succinate via oxaloacetate, malate & fumarate)'] = (
          self.abundance[self.bn+'_K01595'] +
          self.abundance[self.bn+'_K01596'] +
          self.abundance[self.bn+'_K20370'] +
          self.abundance[self.bn+'_K01610'] +
          self.abundance[self.bn+'_K00024'] +
          self.abundance[self.bn+'_K00025'] +
          self.abundance[self.bn+'_K00026'] +
          self.abundance[self.bn+'_K00051'] +
          self.abundance[self.bn+'_K00116'] +
          self.abundance[self.bn+'_K01676'] +
          self.abundance[self.bn+'_K01679'] +
          (self.abundance[self.bn+'_K01677'] +
           self.abundance[self.bn+'_K01678'])/2 +
          (self.abundance[self.bn+'_K00244'] +
           self.abundance[self.bn+'_K00245'] +
           self.abundance[self.bn+'_K00246'] +
           self.abundance[self.bn+'_K00247'])/4)/4

    def Glyoxylate_shunt(self):
        ko_list = [self.bn+'_K01637', self.bn+'_K01638', self.bn+'_K19282']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Glyoxylate shunt'] = (
          self.abundance[self.bn+'_K01637'] +
          self.abundance[self.bn+'_K01638'] +
          self.abundance[self.bn+'_K19282'])/2

    def Anaplerotic_genes(self):
        ko_list = [self.bn+'_K00027', self.bn+'_K00028', self.bn+'_K00029',
                   self.bn+'_K01958', self.bn+'_K01959', self.bn+'_K01960',
                   self.bn+'_K01595', self.bn+'_K01610', self.bn+'_K01596',
                   self.bn+'_K20370']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Anaplerotic genes (pyruvate -> oxaloacetate)'] = (
          self.abundance[self.bn+'_K00027'] +
          self.abundance[self.bn+'_K00028'] +
          self.abundance[self.bn+'_K00029'] +
          self.abundance[self.bn+'_K01958'] +
          (self.abundance[self.bn+'_K01959'] +
           self.abundance[self.bn+'_K01960'])/2 +
          self.abundance[self.bn+'_K01595'] +
          self.abundance[self.bn+'_K01610'] +
          self.abundance[self.bn+'_K01596'] +
          self.abundance[self.bn+'_K20370'])

    def Dissimilatory_nitrate_reduction_to_nitrite(self):
        ko_list = [self.bn+'_K00370', self.bn+'_K00371', self.bn+'_K00374',
                   self.bn+'_K02567', self.bn+'_K02568']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Dissimilatory nitrate reduction, nitrate -> nitrite (narGHI or napAB)'] = (
            (self.abundance[self.bn+'_K00370'] +
             self.abundance[self.bn+'_K00371'] +
             self.abundance[self.bn+'_K00374'])/3 +
            (self.abundance[self.bn+'_K02567'] +
             self.abundance[self.bn+'_K02568'])/2)

    def Dissimilatory_nitrite_reduction_to_ammonia(self):
        ko_list = [self.bn+'_K00362', self.bn+'_K00363', self.bn+'_K03385',
                   self.bn+'_K15876']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Dissimilatory nitrate reduction, nitrite -> ammonia (nirBD or nrfAH)'] = (
          (self.abundance[self.bn+'_K00362'] +
           self.abundance[self.bn+'_K00363'])/2 +
          (self.abundance[self.bn+'_K03385'] +
           self.abundance[self.bn+'_K15876'])/2)

    def DNRA(self):
        ko_list = [self.bn+'_K00370', self.bn+'_K00371', self.bn+'_K00374',
                   self.bn+'_K02567', self.bn+'_K02568', self.bn+'_K00362',
                   self.bn+'_K00363', self.bn+'_K03385', self.bn+'_K15876']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['DNRA'] = (
            (self.abundance[self.bn+'_K00370'] +
             self.abundance[self.bn+'_K00371'] +
             self.abundance[self.bn+'_K00374'])/3 +
            (self.abundance[self.bn+'_K02567'] +
             self.abundance[self.bn+'_K02568'])/2 +
            (self.abundance[self.bn+'_K00362'] +
             self.abundance[self.bn+'_K00363'])/2 +
            (self.abundance[self.bn+'_K03385'] +
             self.abundance[self.bn+'_K15876'])/2)/2

    def Assimilatory_nitrate_reduction_to_nitrite(self):
        ko_list = [self.bn+'_K00367', self.bn+'_K10534', self.bn+'_K00372',
                   self.bn+'_K00360']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Assimilatory nitrate reduction, nitrate -> nitrite (narB or NR or nasAB)'] = (
          self.abundance[self.bn+'_K00367'] +
          self.abundance[self.bn+'_K10534'] +
          (self.abundance[self.bn+'_K00372'] +
           self.abundance[self.bn+'_K00360'])/2)

    def Assimilatory_nitrite_reduction_to_ammonia(self):
        ko_list = [self.bn+'_K17877', self.bn+'_K00366']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Assimilatory nitrate reduction, nitrite -> ammonia (NIT-6 or nirA)'] = (
          self.abundance[self.bn+'_K17877'] +
          self.abundance[self.bn+'_K00366'])

    def Assimilatory_nitrate_reduction_to_ammonia(self):
        ko_list = [self.bn+'_K00367', self.bn+'_K10534', self.bn+'_K00372',
                   self.bn+'_K00360', self.bn+'_K17877', self.bn+'_K00366']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Assimilatory nitrate reduction to ammonia'] = (
          self.abundance[self.bn+'_K00367'] +
          self.abundance[self.bn+'_K10534'] +
          (self.abundance[self.bn+'_K00372'] +
           self.abundance[self.bn+'_K00360'])/2 +
          self.abundance[self.bn+'_K17877'] +
          self.abundance[self.bn+'_K00366'])/2

    def Denitrification_NO2_NO(self):
        ko_list = [self.bn+'_K00368', self.bn+'_K15864']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Denitrification, nitrite -> nitric oxide (nirK or nirS)'] = (
          self.abundance[self.bn+'_K00368'] +
          self.abundance[self.bn+'_K15864'])

    def Denitrification_NO_N2O(self):
        ko_list = [self.bn+'_K04561', self.bn+'_K02305']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Denitrification, nitric oxide -> nitrous oxide (norBC)'] = (
          self.abundance[self.bn+'_K04561'] +
          self.abundance[self.bn+'_K02305'])

    def Denitrification_N2O_N2(self):
        ko_list = [self.bn+'_K00376']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Denitrification, nitrous oxide -> nitrogen (nosZ)'] = (
          self.abundance[self.bn+'_K00376'])

    def Nitrogen_fixation(self):
        ko_list = [self.bn+'_K02586', self.bn+'_K02591', self.bn+'_K02588',
                   self.bn+'_K22896', self.bn+'_K22897', self.bn+'_K22898',
                   self.bn+'_K22899']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Nitrogen fixation, nitrogen -> ammonia (nifKDH)'] = (
            (self.abundance[self.bn+'_K02586'] +
             self.abundance[self.bn+'_K02588'] +
             self.abundance[self.bn+'_K02591'])/3 +
            (self.abundance[self.bn+'_K22896'] +
             self.abundance[self.bn+'_K22897'] +
             self.abundance[self.bn+'_K22898'] +
             self.abundance[self.bn+'_K22899'])/4)

    def Nitrification_ammonia_to_hydroxylamine(self):
        ko_list = [self.bn+'_K10944', self.bn+'_K10945', self.bn+'_K10946']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Nitrification, ammonia -> hydroxylamine (amoABC)'] = (
          self.abundance[self.bn+'_K10944'] +
          self.abundance[self.bn+'_K10945'] +
          self.abundance[self.bn+'_K10946'])/3

    def Nitrification_hydroxylamine_to_nitrite(self):
        ko_list = [self.bn+'_K10535']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Nitrification, hydroxylamine -> nitrite (hao)'] = (
          self.abundance[self.bn+'_K10535'])

    def Nitrification_nitrite_to_nitrate(self):
        ko_list = [self.bn+'_K00370', self.bn+'_K00371']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Nitrification, nitrite -> nitrate (nxrAB)'] = (
          self.abundance[self.bn+'_K00370'] +
          self.abundance[self.bn+'_K00371'])/2

    def Nitrification(self):
        ko_list = [self.bn+'_K10944', self.bn+'_K10945', self.bn+'_K10946',
                   self.bn+'_K10535', self.bn+'_K00370', self.bn+'_K00371']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Nitrification'] = (
          (self.abundance[self.bn+'_K10944'] +
           self.abundance[self.bn+'_K10945'] +
           self.abundance[self.bn+'_K10946'])/3 +
          self.abundance[self.bn+'_K10535'] +
          (self.abundance[self.bn+'_K00370'] +
           self.abundance[self.bn+'_K00371'])/2)/3

    def Anammox(self):
        ko_list = [self.bn+'_K15864', self.bn+'_K20932', self.bn+'_K20933',
                   self.bn+'_K20934', self.bn+'_K20935', self.bn+'_K00368']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Anammox (anaerobic ammonium oxidation)'] = (
          self.abundance[self.bn+'_K00368'] +
          self.abundance[self.bn+'_K15864'] +
          (self.abundance[self.bn+'_K20932'] +
           self.abundance[self.bn+'_K20933'] +
           self.abundance[self.bn+'_K20934'])/3 +
          self.abundance[self.bn+'_K20935'])/3

    def Anammox_of_ammonia_to_hydrazine(self):
        ko_list = [self.bn+'_K20932', self.bn+'_K20933', self.bn+'_K20934']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Anammox, nitric oxide + ammonia -> hydrazine (hzs)'] = (
          self.abundance[self.bn+'_K20932'] +
          self.abundance[self.bn+'_K20933'] +
          self.abundance[self.bn+'_K20934'])/3

    def Anammox_of_hydrazine_to_nitrogen(self):
        ko_list = [self.bn+'_K20935']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Anammox, hydrazine -> nitrogen (hdh)'] = (
          self.abundance[self.bn+'_K20935'])

    def Assimilatory_sulfate_reduction_to_sulfite(self):
        ko_list = [self.bn+'_K13811', self.bn+'_K00958', self.bn+'_K00860',
                   self.bn+'_K00955', self.bn+'_K00957', self.bn+'_K00956',
                   self.bn+'_K13911']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Assimilatory sulfate reduction, sulfate -> sulfite'] = (
          self.abundance[self.bn+'_K13811'] +
          (self.abundance[self.bn+'_K00958'] +
           self.abundance[self.bn+'_K00860'])/2 +
          (self.abundance[self.bn+'_K00955'] +
           self.abundance[self.bn+'_K00957'])/2 +
          (self.abundance[self.bn+'_K00956'] +
           self.abundance[self.bn+'_K00957'] +
           self.abundance[self.bn+'_K00860'])/3 +
          self.abundance[self.bn+'_K13911'])/2

    def Assimilatory_sulfite_reduction_to_sulfide(self):
        ko_list = [self.bn+'_K00380', self.bn+'_K00381', self.bn+'_K00392']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Assimilatory sulfate reduction, sulfite -> sulfide (cysJI or sir)'] = (
          (self.abundance[self.bn+'_K00380'] +
           self.abundance[self.bn+'_K00381'])/2 +
          self.abundance[self.bn+'_K00392'])

    def Dissimilatory_sulfate_reduction_to_sulfite(self):
        ko_list = [self.bn+'_K00956', self.bn+'_K00957', self.bn+'_K00958',
                   self.bn+'_K00394', self.bn+'_K00395']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Dissimilatory sulfate reduction, sulfate -> sulfite (reversible) (sat and aprAB)'] = (
          (self.abundance[self.bn+'_K00956'] +
           self.abundance[self.bn+'_K00957'])/2 +
          self.abundance[self.bn+'_K00958'] +
          (self.abundance[self.bn+'_K00394'] +
           self.abundance[self.bn+'_K00395'])/2)/2

    def Dissimilatory_sulfite_reduction_to_sulfide(self):
        ko_list = [self.bn+'_K11180', self.bn+'_K11181']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Dissimilatory sulfate reduction, sulfite -> sulfide (reversible) (dsrAB)'] = (
          self.abundance[self.bn+'_K11180'] +
          self.abundance[self.bn+'_K11181'])/2

    def Thiosulfate_oxidation_by_SOX_complex_thiosulfate_sulfate(self):
        ko_list = [self.bn+'_K17222', self.bn+'_K17223', self.bn+'_K17224',
                   self.bn+'_K17226', self.bn+'_K17227']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Thiosulfate oxidation by SOX complex, thiosulfate -> sulfate'] = (
          self.abundance[self.bn+'_K17222'] +
          self.abundance[self.bn+'_K17223'] +
          self.abundance[self.bn+'_K17224'] +
          self.abundance[self.bn+'_K17226'] +
          self.abundance[self.bn+'_K17227'])/5

    def Alternative_thiosulfate_oxidation_doxAD(self):
        ko_list = [self.bn+'_K16936', self.bn+'_K16937']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Alternative thiosulfate oxidation (doxAD)'] = (
          self.abundance[self.bn+'_K16936'] +
          self.abundance[self.bn+'_K16937'])/2

    def Alternative_thiosulfate_oxidation_tsdA(self):
        ko_list = [self.bn+'_K19713']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Alternative thiosulfate oxidation (tsdA)'] = (
          self.abundance[self.bn+'_K19713'])

    def Thiosulfate_oxidation_total(self):
        ko_list = [self.bn+'_K17222', self.bn+'_K17223', self.bn+'_K17224',
                   self.bn+'_K17226', self.bn+'_K17227', self.bn+'_K16936', 
                   self.bn+'_K16937', self.bn+'_K19713']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Thiosulfate oxidation (SOX, doxAD and tsdA)'] = (
          (self.abundance[self.bn+'_K17222'] +
           self.abundance[self.bn+'_K17223'] +
           self.abundance[self.bn+'_K17224'] +
           self.abundance[self.bn+'_K17226'] +
           self.abundance[self.bn+'_K17227'])/5 +
          (self.abundance[self.bn+'_K16936'] +
           self.abundance[self.bn+'_K16937'])/2 +
          self.abundance[self.bn+'_K19713'])

    def sulfur_reduction_sulfur_sulfide_sreABC(self):
        ko_list = [self.bn+'_K17219', self.bn+'_K17220', self.bn+'_K17221']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Sulfur reduction, sulfur -> sulfide (sreABC)'] = (
          self.abundance[self.bn+'_K17219'] +
          self.abundance[self.bn+'_K17220'] +
          self.abundance[self.bn+'_K17221'])/3

    def thiosulfate_disproportionation_thiosulfate_sulfide_sulfite_phsABC(self):
        ko_list = [self.bn+'_K08352', self.bn+'_K08353', self.bn+'_K08354']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Thiosulfate disproportionation, thiosulfate -> sulfide & sulfite (phsABC)'] = (
          self.abundance[self.bn+'_K08352'] +
          self.abundance[self.bn+'_K08353'] +
          self.abundance[self.bn+'_K08354'])/3

    def sulfhydrogenase(self):
        ko_list = [self.bn+'_K17993', self.bn+'_K17994', self.bn+'_K17995',
                   self.bn+'_K17996']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Sulfhydrogenase, (sulfide)n -> (sulfide)n-1'] = (
          self.abundance[self.bn+'_K17993'] +
          self.abundance[self.bn+'_K17994'] +
          self.abundance[self.bn+'_K17995'] +
          self.abundance[self.bn+'_K17996'])/4

    def sulfur_disproportionation_sulfur_sulfide_sulfite(self):
        ko_list = [self.bn+'_K16952']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Sulfur disproportionation, sulfur -> sulfide & sulfite'] = (
          self.abundance[self.bn+'_K16952'])

    def sulfur_dioxygenase(self):
        ko_list = [self.bn+'_K17725']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Sulfur dioxygenase'] = (
          self.abundance[self.bn+'_K17725'])

    def sulfite_oxidation_sulfite_sulfate_sor_SUOX_soeABC(self):
        ko_list = [self.bn+'_K05301', self.bn+'_K00387', self.bn+'_K21307',
                   self.bn+'_K21308', self.bn+'_K21309']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Sulfite oxidation, sulfite -> sulfate (sorB, SUOX, soeABC)'] = (
          self.abundance[self.bn+'_K05301'] +
          self.abundance[self.bn+'_K00387'] +
          (self.abundance[self.bn+'_K21307'] +
           self.abundance[self.bn+'_K21308'] +
           self.abundance[self.bn+'_K21309'])/3)

    def sulfide_oxidation_sulfide_sulfur_fccAB(self):
        ko_list = [self.bn+'_K17229', self.bn+'_K17230']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Sulfide oxidation, sulfide -> sulfur (fccAB)'] = (
          self.abundance[self.bn+'_K17229'] +
          self.abundance[self.bn+'_K17230'])/2

    def DMSP_biosynthesis_LMet_to_DMSP(self):
        ko_list = [self.bn+'_MmtN', self.bn+'_DSYB',
                   self.bn+'_DsyB']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['DMSP biosynthesis, L-Met -> DMSP (DSYB or dsyB or mmtN)'] = (
          self.abundance[self.bn+'_MmtN'] +
          self.abundance[self.bn+'_DSYB'] +
          self.abundance[self.bn+'_DsyB'])

    def DMSP_demethylation_DMSP_to_MMPA(self):
        ko_list = [self.bn+'_DmdA']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['DMSP demethylation, DMSP -> MMPA (dmdA)'] = (
          self.abundance[self.bn+'_DmdA'])

    def DMSP_demethylation_MMPA_to_MeSH(self):
        ko_list = [self.bn+'_DmdB', self.bn+'_DmdC',
                   self.bn+'_DmdD', self.bn+'_AcuH']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['DMSP demethylation, MMPA -> MeSH (dmdBCD or acuH)'] = (
          self.abundance[self.bn+'_DmdB'] +
          self.abundance[self.bn+'_DmdC'] +
          self.abundance[self.bn+'_DmdD'] +
          self.abundance[self.bn+'_AcuH'])

    def DMSP_cleavage(self):
        ko_list = [self.bn+'_Alma1', self.bn+'_DddD',
                   self.bn+'_DddK', self.bn+'_DddL',
                   self.bn+'_DddP', self.bn+'_DddQ',
                   self.bn+'_DddW', self.bn+'_DddY']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['DMSP cleavage, DMSP -> DMS (ddds or alma1)'] = (
          self.abundance[self.bn+'_Alma1'] +
          self.abundance[self.bn+'_DddD'] +
          self.abundance[self.bn+'_DddK'] +
          self.abundance[self.bn+'_DddL'] +
          self.abundance[self.bn+'_DddP'] +
          self.abundance[self.bn+'_DddQ'] +
          self.abundance[self.bn+'_DddW'] +
          self.abundance[self.bn+'_DddY'])

    def DMS_oxidation_DMS_to_MeSH(self):
        ko_list = [self.bn+'_DmoA']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['DMS oxidation, DMS -> MeSH (dmoA)'] = (
          self.abundance[self.bn+'_DmoA'])

    def DMS_oxidation_DMS_to_DMSO(self):
        ko_list = [self.bn+'_DdhA', self.bn+'_Tmm']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['DMS oxidation, DMS -> DMSO (ddhA or tmm)'] = (
          self.abundance[self.bn+'_DdhA'] +
          self.abundance[self.bn+'_Tmm'])

    def DMSO_reduction_DMSO_to_DMS(self):
        ko_list = [self.bn+'_DMSOR']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['DMSO reduction, DMSO -> DMS (dMSOR)'] = (
          self.abundance[self.bn+'_DMSOR'])

    def MddA_pathway_MeSH_to_DMS(self):
        ko_list = [self.bn+'_MddA']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['MddA pathway, MeSH -> DMS (mddA)'] = (
          self.abundance[self.bn+'_MddA'])

    def MeSH_oxidation_MeSH_to_Formaldehyde(self):
        ko_list = [self.bn+'_MTO']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['MeSH oxidation, MeSH -> Formaldehyde (mTO)'] = (
          self.abundance[self.bn+'_MTO'])


    def F_type_ATPase(self):
        ko_list = [self.bn+'_K02111', self.bn+'_K02112',
                   self.bn+'_K02115', self.bn+'_K02113',
                   self.bn+'_K02114', self.bn+'_K02108',
                   self.bn+'_K02109', self.bn+'_K02110']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['F-type ATPase'] = (self.abundance[self.bn+'_K02111'] +
                                     self.abundance[self.bn+'_K02112'] +
                                     self.abundance[self.bn+'_K02115'] +
                                     self.abundance[self.bn+'_K02113'] +
                                     self.abundance[self.bn+'_K02114'] +
                                     self.abundance[self.bn+'_K02108'] +
                                     self.abundance[self.bn+'_K02109'] +
                                     self.abundance[self.bn+'_K02110'])/8

    def V_type_ATPase(self):
        ko_list = [self.bn+'_K02117', self.bn+'_K02118',
                   self.bn+'_K02119', self.bn+'_K02120',
                   self.bn+'_K02121', self.bn+'_K02122',
                   self.bn+'_K02107', self.bn+'_K02123',
                   self.bn+'_K02124']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['V/A-type ATPase'] = (
            self.abundance[self.bn+'_K02117'] +
            self.abundance[self.bn+'_K02118'] +
            self.abundance[self.bn+'_K02119'] +
            self.abundance[self.bn+'_K02120'] +
            self.abundance[self.bn+'_K02121'] +
            self.abundance[self.bn+'_K02122'] +
            self.abundance[self.bn+'_K02107'] +
            self.abundance[self.bn+'_K02123'] +
            self.abundance[self.bn+'_K02124'])/9

    def NADH_quinone_oxidoreductase(self):
        ko_list = [self.bn+'_K00330', self.bn+'_K00331', self.bn+'_K00332',
                   self.bn+'_K00333', self.bn+'_K00334', self.bn+'_K00335',
                   self.bn+'_K00336', self.bn+'_K00337', self.bn+'_K00338',
                   self.bn+'_K00339', self.bn+'_K00340', self.bn+'_K00341',
                   self.bn+'_K00342', self.bn+'_K00343', self.bn+'_K13378',
                   self.bn+'_K13380', self.bn+'_K15863']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['NADH-quinone oxidoreductase'] = (
            self.abundance[self.bn+'_K00330'] +
            (self.abundance[self.bn+'_K00331'] +
             self.abundance[self.bn+'_K00332'] +
             self.abundance[self.bn+'_K00333'])/3 +
            (self.abundance[self.bn+'_K00331'] +
             self.abundance[self.bn+'_K13378'])/2 +
            self.abundance[self.bn+'_K13380'] +
            self.abundance[self.bn+'_K00334'] +
            self.abundance[self.bn+'_K00335'] +
            self.abundance[self.bn+'_K00336'] +
            self.abundance[self.bn+'_K00337'] +
            self.abundance[self.bn+'_K00338'] +
            self.abundance[self.bn+'_K00339'] +
            self.abundance[self.bn+'_K00340'] +
            (self.abundance[self.bn+'_K00341'] +
             self.abundance[self.bn+'_K00342'])/2 +
            self.abundance[self.bn+'_K15863'] +
            self.abundance[self.bn+'_K00343'])/11

    def NADPH_quinone_oxidoreductase(self):
        ko_list = [self.bn+'_K05574', self.bn+'_K05582',
                   self.bn+'_K05581', self.bn+'_K05579',
                   self.bn+'_K05572', self.bn+'_K05580',
                   self.bn+'_K05578', self.bn+'_K05576',
                   self.bn+'_K05577', self.bn+'_K05575',
                   self.bn+'_K05573']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['NAD(P)H-quinone oxidoreductase'] = (
            self.abundance[self.bn+'_K05574'] +
            self.abundance[self.bn+'_K05582'] +
            self.abundance[self.bn+'_K05581'] +
            self.abundance[self.bn+'_K05579'] +
            self.abundance[self.bn+'_K05572'] +
            self.abundance[self.bn+'_K05580'] +
            self.abundance[self.bn+'_K05578'] +
            self.abundance[self.bn+'_K05576'] +
            self.abundance[self.bn+'_K05577'] +
            self.abundance[self.bn+'_K05575'] +
            self.abundance[self.bn+'_K05573'])/11

    def succinate_dehydrogenase_ubiquinone(self):
        ko_list = [self.bn+'_K00236', self.bn+'_K00237',
                   self.bn+'_K00234', self.bn+'_K00235']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Succinate dehydrogenase (ubiquinone)'] = (
            self.abundance[self.bn+'_K00234'] +
            self.abundance[self.bn+'_K00235'] +
            self.abundance[self.bn+'_K00236'] +
            self.abundance[self.bn+'_K00237'])/4

    def Cytochrome_c_oxidase_cbb3_type(self):
        ko_list = [self.bn+'_K00404', self.bn+'_K00405',
                   self.bn+'_K00406', self.bn+'_K00407',
                   self.bn+'_K15862']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Cytochrome c oxidase, cbb3-type'] = (
            (self.abundance[self.bn+'_K00404'] +
             self.abundance[self.bn+'_K00405'])/2 +
            self.abundance[self.bn+'_K15862'] +
            self.abundance[self.bn+'_K00406'] +
            self.abundance[self.bn+'_K00407'])/3

    def Cytochrome_bd_ubiquinol_oxidase(self):
        ko_list = [self.bn+'_K00425', self.bn+'_K00426',
                   self.bn+'_K00424', self.bn+'_K22501']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Cytochrome bd ubiquinol oxidase'] = (
            self.abundance[self.bn+'_K00425'] +
            self.abundance[self.bn+'_K00426'] +
            self.abundance[self.bn+'_K00424'] +
            self.abundance[self.bn+'_K22501'])/3

    def Cytochrome_o_ubiquinol_oxidase(self):
        ko_list = [self.bn+'_K02300', self.bn+'_K02299',
                   self.bn+'_K02298', self.bn+'_K02297']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Cytochrome o ubiquinol oxidase'] = (
          self.abundance[self.bn+'_K02300'] +
          self.abundance[self.bn+'_K02299'] +
          self.abundance[self.bn+'_K02298'] +
          self.abundance[self.bn+'_K02297'])/4

    def Cytochrome_c_oxidase_prokaryotes(self):
        ko_list = [self.bn+'_K02274', self.bn+'_K02275',
                   self.bn+'_K02276', self.bn+'_K15408']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Cytochrome c oxidase, prokaryotes, aa3-type'] = (
            self.abundance[self.bn+'_K02275'] +
            (self.abundance[self.bn+'_K02274'] +
             self.abundance[self.bn+'_K02276'])/2 +
            self.abundance[self.bn+'_K15408'])/2

    def Cytochrome_aa3_600_menaquinol_oxidase(self):
        ko_list = [self.bn+'_K02829', self.bn+'_K02828',
                   self.bn+'_K02827', self.bn+'_K02826']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Cytochrome aa3-600 menaquinol oxidase'] = (
            self.abundance[self.bn+'_K02829'] +
            self.abundance[self.bn+'_K02828'] +
            self.abundance[self.bn+'_K02827'] +
            self.abundance[self.bn+'_K02826'])/4

    def cytochrome_bc1_complex(self):
        ko_list = [self.bn+'_K00412', self.bn+'_K00413', self.bn+'_K00410',
                   self.bn+'_K00411', self.bn+'_K00414', self.bn+'_K00415',
                   self.bn+'_K00416', self.bn+'_K00417', self.bn+'_K00418',
                   self.bn+'_K00419', self.bn+'_K00420']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Cytochrome bc1 complex'] = (
            (self.abundance[self.bn+'_K00412'] +
             self.abundance[self.bn+'_K00413'])/2 +
            self.abundance[self.bn+'_K00410'] +
            self.abundance[self.bn+'_K00411'] +
            self.abundance[self.bn+'_K00414'] +
            self.abundance[self.bn+'_K00415'] +
            self.abundance[self.bn+'_K00416'] +
            self.abundance[self.bn+'_K00417'] +
            self.abundance[self.bn+'_K00418'] +
            self.abundance[self.bn+'_K00419'] +
            self.abundance[self.bn+'_K00420'])/9

    def Phosphate_transporter(self):
        ko_list = [self.bn+'_K02037', self.bn+'_K02038',
                   self.bn+'_K02036', self.bn+'_K02040']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Phosphate transporter'] = (
            self.abundance[self.bn+'_K02040'] +
            self.abundance[self.bn+'_K02036'] +
            self.abundance[self.bn+'_K02037'] +
            self.abundance[self.bn+'_K02038'])/3

    def Phosphonate_transporter(self):
        ko_list = [self.bn+'_K02042', self.bn+'_K02041', self.bn+'_K02044']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Phosphonate transporter'] = (
            self.abundance[self.bn+'_K02041'] +
            self.abundance[self.bn+'_K02042'] +
            self.abundance[self.bn+'_K02044'])/3

    def Thiamin_transporter(self):
        ko_list = [self.bn+'_K02062', self.bn+'_K02063',
                   self.bn+'_K02064']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Thiamin transporter'] = (
            self.abundance[self.bn+'_K02064'] +
            self.abundance[self.bn+'_K02063'] +
            self.abundance[self.bn+'_K02062'])/3

    def Vitamin_B12_transporter(self):
        ko_list = [self.bn+'_K06858', self.bn+'_K06073',
                   self.bn+'_K06074']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Vitamin B12 transporter'] = (
            self.abundance[self.bn+'_K06074'] +
            self.abundance[self.bn+'_K06073'] +
            self.abundance[self.bn+'_K06858'])/3

    def Urea_transporter(self):
        ko_list = [self.bn+'_K11959', self.bn+'_K11960',
                   self.bn+'_K11961', self.bn+'_K11962',
                   self.bn+'_K11963']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Urea transporter'] = (
            self.abundance[self.bn+'_K11959'] +
            self.abundance[self.bn+'_K11960'] +
            self.abundance[self.bn+'_K11961'] +
            self.abundance[self.bn+'_K11962'] +
            self.abundance[self.bn+'_K11963'])/5

    def Type_I_Secretion(self):
        ko_list = [self.bn+'_K12340', self.bn+'_K11003',
                   self.bn+'_K11004']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Type I Secretion'] = (
            self.abundance[self.bn+'_K12340'] +
            self.abundance[self.bn+'_K11003'] +
            self.abundance[self.bn+'_K11004'])/3

    def Type_III_Secretion(self):
        ko_list = [self.bn+'_K03221', self.bn+'_K04056',
                   self.bn+'_K04057', self.bn+'_K04059',
                   self.bn+'_K03219', self.bn+'_K04058',
                   self.bn+'_K03222', self.bn+'_K03223',
                   self.bn+'_K03224', self.bn+'_K03225',
                   self.bn+'_K03226', self.bn+'_K03227',
                   self.bn+'_K03228', self.bn+'_K03229',
                   self.bn+'_K03230']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Type III Secretion'] = (
            self.abundance[self.bn+'_K03221'] +
            self.abundance[self.bn+'_K04056'] +
            self.abundance[self.bn+'_K04057'] +
            self.abundance[self.bn+'_K04058'] +
            self.abundance[self.bn+'_K04059'] +
            self.abundance[self.bn+'_K03219'] +
            self.abundance[self.bn+'_K03222'] +
            self.abundance[self.bn+'_K03223'] +
            self.abundance[self.bn+'_K03224'] +
            self.abundance[self.bn+'_K03225'] +
            self.abundance[self.bn+'_K03226'] +
            self.abundance[self.bn+'_K03227'] +
            self.abundance[self.bn+'_K03228'] +
            self.abundance[self.bn+'_K03229'] +
            self.abundance[self.bn+'_K03230'])/15

    def Type_II_Secretion(self):
        ko_list = [self.bn+'_K02452', self.bn+'_K02453',
                   self.bn+'_K02454', self.bn+'_K02455',
                   self.bn+'_K02456', self.bn+'_K02457',
                   self.bn+'_K02458', self.bn+'_K02459',
                   self.bn+'_K02460', self.bn+'_K02461',
                   self.bn+'_K02462', self.bn+'_K02464',
                   self.bn+'_K02465']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Type II Secretion'] = (
            self.abundance[self.bn+'_K02452'] +
            self.abundance[self.bn+'_K02453'] +
            self.abundance[self.bn+'_K02454'] +
            self.abundance[self.bn+'_K02455'] +
            self.abundance[self.bn+'_K02456'] +
            self.abundance[self.bn+'_K02457'] +
            self.abundance[self.bn+'_K02458'] +
            self.abundance[self.bn+'_K02459'] +
            self.abundance[self.bn+'_K02460'] +
            self.abundance[self.bn+'_K02461'] +
            self.abundance[self.bn+'_K02462'] +
            self.abundance[self.bn+'_K02464'] +
            self.abundance[self.bn+'_K02465'])/13

    def Type_IV_Secretion(self):
        ko_list = [self.bn+'_K03194', self.bn+'_K03195',
                   self.bn+'_K03196', self.bn+'_K03197',
                   self.bn+'_K03198', self.bn+'_K03199',
                   self.bn+'_K03200', self.bn+'_K03201',
                   self.bn+'_K03202', self.bn+'_K03203',
                   self.bn+'_K03204', self.bn+'_K03205']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Type IV Secretion'] = (
            self.abundance[self.bn+'_K03194'] +
            self.abundance[self.bn+'_K03197'] +
            self.abundance[self.bn+'_K03198'] +
            self.abundance[self.bn+'_K03200'] +
            self.abundance[self.bn+'_K03202'] +
            self.abundance[self.bn+'_K03204'] +
            self.abundance[self.bn+'_K03201'] +
            self.abundance[self.bn+'_K03203'] +
            self.abundance[self.bn+'_K03195'] +
            self.abundance[self.bn+'_K03199'] +
            self.abundance[self.bn+'_K03196'] +
            self.abundance[self.bn+'_K03205'])/12

    def Type_VI_Secretion(self):
        ko_list = [self.bn+'_K11903', self.bn+'_K11904',
                   self.bn+'_K11906', self.bn+'_K11907',
                   self.bn+'_K11891', self.bn+'_K11892',
                   self.bn+'_K11912', self.bn+'_K11913',
                   self.bn+'_K11915']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Type VI Secretion'] = (
            self.abundance[self.bn+'_K11904'] +
            self.abundance[self.bn+'_K11903'] +
            self.abundance[self.bn+'_K11906'] +
            self.abundance[self.bn+'_K11891'] +
            self.abundance[self.bn+'_K11892'] +
            self.abundance[self.bn+'_K11907'] +
            self.abundance[self.bn+'_K11912'] +
            self.abundance[self.bn+'_K11913'] +
            self.abundance[self.bn+'_K11915'])/9

    def Sec_SRP(self):
        ko_list = [self.bn+'_K03072', self.bn+'_K03074', self.bn+'_K12257',
                   self.bn+'_K03073', self.bn+'_K03075', self.bn+'_K03076',
                   self.bn+'_K03210', self.bn+'_K03217', self.bn+'_K03070',
                   self.bn+'_K13301', self.bn+'_K03110', self.bn+'_K03071',
                   self.bn+'_K03106']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Sec-SRP'] = (
            self.abundance[self.bn+'_K03072'] +
            self.abundance[self.bn+'_K03074'] +
            self.abundance[self.bn+'_K12257'] +
            self.abundance[self.bn+'_K03073'] +
            self.abundance[self.bn+'_K03075'] +
            self.abundance[self.bn+'_K03076'] +
            self.abundance[self.bn+'_K03210'] +
            self.abundance[self.bn+'_K03217'] +
            self.abundance[self.bn+'_K03070'] +
            self.abundance[self.bn+'_K13301'] +
            self.abundance[self.bn+'_K03110'] +
            self.abundance[self.bn+'_K03071'] +
            self.abundance[self.bn+'_K03106'])/13

    def Twin_arginine_targeting(self):
        ko_list = [self.bn+'_K03116', self.bn+'_K03117',
                   self.bn+'_K03118', self.bn+'_K03425']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Twin arginine targeting'] = (
            self.abundance[self.bn+'_K03116'] +
            self.abundance[self.bn+'_K03117'] +
            self.abundance[self.bn+'_K03118'] +
            self.abundance[self.bn+'_K03425'])/4

    def Type_Vabc_secretion(self):
        ko_list = [self.bn+'_K11016', self.bn+'_K11017',
                   self.bn+'_K11028', self.bn+'_K12341',
                   self.bn+'_K12342']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Type Vabc secretion'] = (
            self.abundance[self.bn+'_K11028'] +
            (self.abundance[self.bn+'_K11017'] +
             self.abundance[self.bn+'_K11016'])/2 +
            (self.abundance[self.bn+'_K12341'] +
             self.abundance[self.bn+'_K12342'])/2)

    def Bacterial_chemotaxis(self):
        ko_list = [self.bn+'_K03406', self.bn+'_K05874', self.bn+'_K05875',
                   self.bn+'_K05876', self.bn+'_K05877', self.bn+'_K03776',
                   self.bn+'_K10108', self.bn+'_K10439', self.bn+'_K10540',
                   self.bn+'_K12368', self.bn+'_K03407', self.bn+'_K03408',
                   self.bn+'_K03413', self.bn+'_K03410', self.bn+'_K03414',
                   self.bn+'_K03409', self.bn+'_K03412', self.bn+'_K13924',
                   self.bn+'_K03415', self.bn+'_K03411', self.bn+'_K00575',
                   self.bn+'_K02410', self.bn+'_K02416', self.bn+'_K02417',
                   self.bn+'_K02556', self.bn+'_K02557']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Bacterial chemotaxis'] = (
          self.abundance[self.bn+'_K03406'] +
          self.abundance[self.bn+'_K05874'] +
          self.abundance[self.bn+'_K05875'] +
          self.abundance[self.bn+'_K05876'] +
          self.abundance[self.bn+'_K05877'] +
          self.abundance[self.bn+'_K03776'] +
          self.abundance[self.bn+'_K10108'] +
          self.abundance[self.bn+'_K10439'] +
          self.abundance[self.bn+'_K10540'] +
          self.abundance[self.bn+'_K12368'] +
          self.abundance[self.bn+'_K03407'] +
          self.abundance[self.bn+'_K03408'] +
          self.abundance[self.bn+'_K03413'] +
          self.abundance[self.bn+'_K03410'] +
          self.abundance[self.bn+'_K03414'] +
          self.abundance[self.bn+'_K03409'] +
          self.abundance[self.bn+'_K03412'] +
          self.abundance[self.bn+'_K13924'] +
          self.abundance[self.bn+'_K03415'] +
          self.abundance[self.bn+'_K03411'] +
          self.abundance[self.bn+'_K00575'] +
          self.abundance[self.bn+'_K02410'] +
          self.abundance[self.bn+'_K02416'] +
          self.abundance[self.bn+'_K02417'] +
          self.abundance[self.bn+'_K02556'] +
          self.abundance[self.bn+'_K02557'])/26

    def Flagellum_assembly(self):
        ko_list = [self.bn+'_K02402', self.bn+'_K02403', self.bn+'_K02398',
                   self.bn+'_K02405', self.bn+'_K02406', self.bn+'_K02407',
                   self.bn+'_K02397', self.bn+'_K02396', self.bn+'_K02414',
                   self.bn+'_K02389', self.bn+'_K02390', self.bn+'_K02391',
                   self.bn+'_K02392', self.bn+'_K02393', self.bn+'_K02394',
                   self.bn+'_K02387', self.bn+'_K02388', self.bn+'_K02408',
                   self.bn+'_K02409', self.bn+'_K02410', self.bn+'_K02416',
                   self.bn+'_K02417', self.bn+'_K02400', self.bn+'_K02401',
                   self.bn+'_K02411', self.bn+'_K02412', self.bn+'_K02418',
                   self.bn+'_K02419', self.bn+'_K02420', self.bn+'_K02421',
                   self.bn+'_K13820', self.bn+'_K02556', self.bn+'_K02557',
                   self.bn+'_K21217', self.bn+'_K21218', self.bn+'_K02399',
                   self.bn+'_K02413', self.bn+'_K02422', self.bn+'_K02423',
                   self.bn+'_K02386']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Flagellum assembly'] = (
          self.abundance[self.bn+'_K02402'] +
          self.abundance[self.bn+'_K02403'] +
          self.abundance[self.bn+'_K02398'] +
          self.abundance[self.bn+'_K02405'] +
          self.abundance[self.bn+'_K02406'] +
          self.abundance[self.bn+'_K02407'] +
          self.abundance[self.bn+'_K02397'] +
          self.abundance[self.bn+'_K02396'] +
          self.abundance[self.bn+'_K02414'] +
          self.abundance[self.bn+'_K02389'] +
          self.abundance[self.bn+'_K02390'] +
          self.abundance[self.bn+'_K02391'] +
          self.abundance[self.bn+'_K02392'] +
          self.abundance[self.bn+'_K02393'] +
          self.abundance[self.bn+'_K02394'] +
          self.abundance[self.bn+'_K02387'] +
          self.abundance[self.bn+'_K02388'] +
          self.abundance[self.bn+'_K02408'] +
          self.abundance[self.bn+'_K02409'] +
          self.abundance[self.bn+'_K02410'] +
          self.abundance[self.bn+'_K02416'] +
          self.abundance[self.bn+'_K02417'] +
          self.abundance[self.bn+'_K02400'] +
          self.abundance[self.bn+'_K02401'] +
          self.abundance[self.bn+'_K02411'] +
          self.abundance[self.bn+'_K02412'] +
          self.abundance[self.bn+'_K02418'] +
          self.abundance[self.bn+'_K02419'] +
          self.abundance[self.bn+'_K02420'] +
          self.abundance[self.bn+'_K02421'] +
          self.abundance[self.bn+'_K13820'] +
          self.abundance[self.bn+'_K02556'] +
          self.abundance[self.bn+'_K02557'] +
          self.abundance[self.bn+'_K21217'] +
          self.abundance[self.bn+'_K21218'] +
          self.abundance[self.bn+'_K02399'] +
          self.abundance[self.bn+'_K02413'] +
          self.abundance[self.bn+'_K02422'] +
          self.abundance[self.bn+'_K02423'] +
          self.abundance[self.bn+'_K02386'])/40

    def Dissimilatory_arsenic_reduction(self):
        ko_list = [self.bn+'_K00537', self.bn+'_K03741',
                   self.bn+'_K18701', self.bn+'_K03325',
                   self.bn+'_K03893', self.bn+'_K03892',
                   self.bn+'_K01551']
        for ko in ko_list:
            if ko not in self.abundance:
                self.abundance[ko] = 0
        self.out_data['Dissimilatory arsenic reduction'] = (
          self.abundance[self.bn+'_K00537'] +
          self.abundance[self.bn+'_K03741'] +
          self.abundance[self.bn+'_K18701'] +
          self.abundance[self.bn+'_K03325'] +
          self.abundance[self.bn+'_K03893'] +
          self.abundance[self.bn+'_K03892'] +
          self.abundance[self.bn+'_K01551'])/4

    def solve_pathway(self):
        self.Photosystem_II()
        self.Photosystem_I()
        self.Cytochrome_b6_f_complex()
        self.anoxygenic_photosystem_II_pufML()
        self.anoxygenic_photosystem_I_pscABCD()
        self.RuBisCo()
        self.CBB_Cycle()
        self.rTCA_Cycle()
        self.Wood_Ljungdahl()
        self.three_Hydroxypropionate_Bicycle()
        #self.Dicarboxylate_hydroxybutyrate_cycle()
        #self.pectinesterase()
        #self.diacetylchitobiose_deacetylase()
        #self.glucoamylase()
        #self.D_galacturonate_epimerase()
        #self.exo_poly_alpha_galacturonosidase()
        #self.oligogalacturonide_lyase()
        #self.cellulase()
        #self.exopolygalacturonase()
        #self.chitinase()
        #self.basic_endochitinase_B()
        #self.bifunctional_chitinase_or_lysozyme()
        #self.beta_N_acetylhexosaminidase()
        #self.D_galacturonate_isomerase()
        #self.alpha_amylase()
        #self.beta_glucosidase()
        #self.pullulanase()
        self.glycolysis()
        self.Entner_Doudoroff_Pathway()
        self.gluconeogenesis()
        self.tca_cycle()
        self.Methanogenesis()
        self.Methanogenesis_via_methanol()
        #self.Methanogenesis_via_methylamine()
        #self.Methanogenesis_via_dimethylamine()
        #self.Methanogenesis_via_trimethylamine()
        self.Methanogenesis_via_amines()
        self.Methanogenesis_via_acetate()
        self.Methanogenesis_CO2_methane()
        self.Methane_oxidation_methane_methanol()
        self.Methane_oxidation_methanol_Formaldehyde()
        self.Mixed_acid_lactate()
        self.Mixed_acid_formate()
        self.Mixed_acid_Formate_to_CO2_H2()
        self.Mixed_acid_acetate()
        self.Mixed_acid_pyruvate_to_acetate_include_via_acetylP()
        self.Mixed_acid_acetyl_CoA_to_acetate_include_via_acetylP()
        self.Mixed_acid_lactate_to_acetate()
        self.Mixed_acid_Ethanol_Acetate_to_Acetylaldehyde()
        self.Mixed_acid_Ethanol_Acetyl_CoA_to_Acetylaldehyde()
        self.Mixed_acid_Ethanol_Acetylaldehyde_to_Ethanol()
        self.Mixed_acid_succinate()
        self.Glyoxylate_shunt()
        self.Anaplerotic_genes()
        self.Dissimilatory_nitrate_reduction_to_nitrite()
        self.Dissimilatory_nitrite_reduction_to_ammonia()
        self.DNRA()
        self.Assimilatory_nitrate_reduction_to_nitrite()
        self.Assimilatory_nitrite_reduction_to_ammonia()
        self.Assimilatory_nitrate_reduction_to_ammonia()
        self.Denitrification_NO2_NO()
        self.Denitrification_NO_N2O()
        self.Denitrification_N2O_N2()
        self.Nitrogen_fixation()
        self.Nitrification_ammonia_to_hydroxylamine()
        self.Nitrification_hydroxylamine_to_nitrite()
        self.Nitrification_nitrite_to_nitrate()
        self.Nitrification()
        self.Anammox()
        self.Anammox_of_ammonia_to_hydrazine()
        self.Anammox_of_hydrazine_to_nitrogen()
        self.Assimilatory_sulfate_reduction_to_sulfite()
        self.Assimilatory_sulfite_reduction_to_sulfide()
        self.Dissimilatory_sulfate_reduction_to_sulfite()
        self.Dissimilatory_sulfite_reduction_to_sulfide()
        self.Thiosulfate_oxidation_by_SOX_complex_thiosulfate_sulfate()
        self.Alternative_thiosulfate_oxidation_doxAD()
        self.Alternative_thiosulfate_oxidation_tsdA()
        self.Thiosulfate_oxidation_total()
        self.sulfur_reduction_sulfur_sulfide_sreABC()
        self.thiosulfate_disproportionation_thiosulfate_sulfide_sulfite_phsABC()
        self.sulfhydrogenase()
        self.sulfur_disproportionation_sulfur_sulfide_sulfite()
        self.sulfur_dioxygenase()
        self.sulfite_oxidation_sulfite_sulfate_sor_SUOX_soeABC()
        self.sulfide_oxidation_sulfide_sulfur_fccAB()
        self.DMSP_biosynthesis_LMet_to_DMSP()
        self.DMSP_demethylation_DMSP_to_MMPA()
        self.DMSP_demethylation_MMPA_to_MeSH()
        self.DMSP_cleavage()
        self.DMS_oxidation_DMS_to_MeSH()
        self.DMS_oxidation_DMS_to_DMSO()
        self.DMSO_reduction_DMSO_to_DMS()
        self.MddA_pathway_MeSH_to_DMS()
        self.MeSH_oxidation_MeSH_to_Formaldehyde()
        self.F_type_ATPase()
        self.V_type_ATPase()
        self.NADH_quinone_oxidoreductase()
        self.NADPH_quinone_oxidoreductase()
        self.succinate_dehydrogenase_ubiquinone()
        self.Cytochrome_c_oxidase_cbb3_type()
        self.Cytochrome_bd_ubiquinol_oxidase()
        self.Cytochrome_o_ubiquinol_oxidase()
        self.Cytochrome_c_oxidase_prokaryotes()
        self.Cytochrome_aa3_600_menaquinol_oxidase()
        self.cytochrome_bc1_complex()
        self.Phosphate_transporter()
        self.Phosphonate_transporter()
        self.Thiamin_transporter()
        self.Vitamin_B12_transporter()
        self.Urea_transporter()
        self.Type_I_Secretion()
        self.Type_III_Secretion()
        self.Type_II_Secretion()
        self.Type_IV_Secretion()
        self.Type_VI_Secretion()
        self.Sec_SRP()
        self.Twin_arginine_targeting()
        self.Type_Vabc_secretion()
        self.Bacterial_chemotaxis()
        self.Flagellum_assembly()
        self.Dissimilatory_arsenic_reduction()
        return self.out_data


function_order = ['Photosystem II (psbABCDEF)',
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
                  'Anaplerotic genes (pyruvate -> oxaloacetate)',
                  'Dissimilatory nitrate reduction, nitrate -> nitrite (narGHI or napAB)',
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
                  'Anammox, hydrazine -> nitrogen (hdh)',
                  'Assimilatory sulfate reduction, sulfate -> sulfite',
                  'Assimilatory sulfate reduction, sulfite -> sulfide (cysJI or sir)',
                  'Dissimilatory sulfate reduction, sulfate -> sulfite (reversible) (sat and aprAB)',
                  'Dissimilatory sulfate reduction, sulfite -> sulfide (reversible) (dsrAB)',
                  'Thiosulfate oxidation by SOX complex, thiosulfate -> sulfate',
                  'Alternative thiosulfate oxidation (doxAD)',
                  'Alternative thiosulfate oxidation (tsdA)',
                  'Thiosulfate oxidation (SOX, doxAD and tsdA)',
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
                  'DMSO reduction, DMSO -> DMS (dMSOR)',
                  'MddA pathway, MeSH -> DMS (mddA)',
                  'MeSH oxidation, MeSH -> Formaldehyde (mTO)',
                  'F-type ATPase',
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
