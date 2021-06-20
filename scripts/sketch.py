"""
visualization of carbon, nitrogen and sulfur cycle
"""
import os
import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
from PIL import Image
import sys
import re
import shutil
import cv2
from .logformatter import *
    
__author__ = "Xue Chunxu"
__contact__ = "xuechunxu@outlook.com"
__version__ = "0.7"
    
    
def sketch(abundance_table):
    logging.info('Visualize abundance table')
    os.mkdir('Figure_tmp')
    dict_table = {}
    # make pie charts of each pathway
    head = ''
    total_abun_pathway_dir = {}
    with open(abundance_table) as table:
        for line in table:
            line = line.strip('\n')
            if line.startswith('#'):
                head = line
            else:
                pathway1 = line.split('\t')[0]
                pathway2 = re.sub('/', ' or ', pathway1)
                pathway3 = re.sub('->', 'to', pathway2)
                pathway4 = re.sub(' ', '_', pathway3)
                pathway5 = re.sub('"', '', pathway4)
                pathway6 = re.sub(',', '', pathway5)
                pathway7 = re.sub('\\(', '', pathway6)
                pathway8 = re.sub('\\)', '', pathway7)
                pathway = re.sub('&_', '', pathway8)
                #print(pathway)
                abundance = line.split('\t')
                del abundance[0]
                total = 0
                for i in abundance:
                    total += float(i)
                # dir of total abundance of pathways
                total_abun_pathway_dir[pathway] = total
                abundance_nor = []
                if total == float(0):
                    continue
                else:
                    for i in abundance:
                        abundance_nor.append(float(i)/float(total))
                    #print(abundance_nor)
                    colors = ['#FF0000', '#FF7F00', '#FFD400', '#FFFF00', '#BFFF00',
                              '#6AFF00', '#00EAFF', '#0095FF', '#0040FF', '#AA00FF', 
                              '#FF00AA', '#EDB9B9', '#E7E9B9', '#B9EDE0', '#B9D7ED', 
                              '#DCB9ED', '#8F2323', '#8F6A23', '#4F8F23', '#23628F']
                    plt.axes(aspect='equal')
                    plt.pie(abundance_nor, colors=colors, startangle=90)
                    plt.savefig("Figure_tmp/" + pathway + ".png",
                                format='png', bbox_inches='tight', transparent=True)
    
    
    # background dir pathway
    self_script_pathway = sys.path[0]
    #print(self_script_pathway)
    background_image_pathway = self_script_pathway + "/figure"
    
    # load nitrogen_cycle.png image
    nitrogen_cycle_background_fig = background_image_pathway + "/nitrogen_cycle.png"
    shutil.copy(nitrogen_cycle_background_fig, './Figure_tmp/')
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    #print("background_image_size:", nitrogen_cycle_image.size)
    nitrogen_cycle = ['Nitrogen_fixation_nitrogen_to_ammonia_nifKDH',
                      'Nitrification_ammonia_to_hydroxylamine_amoABC',
                      'Nitrification_hydroxylamine_to_nitrite_hao',
                      'Nitrification_nitrite_to_nitrate_nxrAB',
                      'Assimilatory_nitrate_reduction_nitrate_to_nitrite_narB_or_NR_or_nasAB',
                      'Assimilatory_nitrate_reduction_nitrite_to_ammonia_NIT-6_or_nirA',
                      'Dissimilatory_nitrate_reduction_nitrate_to_nitrite_narGHI_or_napAB',
                      'Dissimilatory_nitrate_reduction_nitrite_to_ammonia_nirBD_or_nrfAH',
                      'Denitrification_nitrite_to_nitric_oxide_nirK_or_nirS',
                      'Denitrification_nitric_oxide_to_nitrous_oxide_norBC',
                      'Denitrification_nitrous_oxide_to_nitrogen_nosZ',
                      'Anammox_nitric_oxide_+_ammonia_to_hydrazine_hzs',
                      'Anammox_hydrazine_to_nitrogen_hdh']
    
    nitrogen_cycle_dir = {}
    for i in nitrogen_cycle:
        nitrogen_cycle_dir[i] = total_abun_pathway_dir[i]
    
    # get the most abundance of nitrogen cycle pathways
    top_abun_nitro = int(0)
    for key in nitrogen_cycle_dir:
        if nitrogen_cycle_dir[key] > top_abun_nitro:
            top_abun_nitro = nitrogen_cycle_dir[key]
    three_quarter_nitro = 3/4 * top_abun_nitro
    two_quarter_nitro = 1/2 * top_abun_nitro
    one_quarter_nitro = 1/4 * top_abun_nitro

    #for write total abundance of each pathway in sketch
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color_font = (0, 0, 0)
    thickness = 4
    
    try:
        pathway_fig = Image.open("Figure_tmp/Nitrogen_fixation_nitrogen_to_ammonia_nifKDH.png")
        position = ()
        #total_abundance_of_each_pathway = '%.2e' % nitrogen_cycle_dir['Nitrogen_fixation_nitrogen_to_ammonia_nifKDH']
        #position_abundance = ()
        if nitrogen_cycle_dir['Nitrogen_fixation_nitrogen_to_ammonia_nifKDH'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1264, 460, 1744, 940)
            #position_abundance = (1264, 940)
        elif nitrogen_cycle_dir['Nitrogen_fixation_nitrogen_to_ammonia_nifKDH'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1384, 426, 1784, 826)
            #position_abundance = (1384, 826)
        elif nitrogen_cycle_dir['Nitrogen_fixation_nitrogen_to_ammonia_nifKDH'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (1434, 426, 1754, 746)
            #position_abundance = (1434, 746)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (1430, 444, 1670, 684)
            #position_abundance = (1430, 684)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
        #nitrogen_cycle_image_cv2 = cv2.imread("Figure_tmp/nitrogen_cycle.png")
        #cv2.putText(nitrogen_cycle_image_cv2, total_abundance_of_each_pathway,
                #position_abundance, font, fontScale, color_font, thickness)
        #cv2.imwrite('Figure_tmp/nitrogen_cycle.png', nitrogen_cycle_image_cv2)
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Nitrification_ammonia_to_hydroxylamine_amoABC.png")
        position = ()
        #total_abundance_of_each_pathway = '%.2e' % nitrogen_cycle_dir['Nitrification_ammonia_to_hydroxylamine_amoABC']
        #position_abundance = ()
        if nitrogen_cycle_dir['Nitrification_ammonia_to_hydroxylamine_amoABC'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (486, 1240, 966, 1720)
            #position_abundance = (486, 1720)
        elif nitrogen_cycle_dir['Nitrification_ammonia_to_hydroxylamine_amoABC'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (532, 1196, 932, 1596)
            #position_abundance = (532, 1596)
        elif nitrogen_cycle_dir['Nitrification_ammonia_to_hydroxylamine_amoABC'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (540, 1244, 860, 1564)
            #position_abundance = (540, 1564)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (544, 1274, 784, 1514)
            #position_abundance = (544, 1514)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
        #cv2.putText(nitrogen_cycle_image_cv2, total_abundance_of_each_pathway,
                #position_abundance, font, fontScale, color_font, thickness)
        #cv2.imwrite('Figure_tmp/nitrogen_cycle.png', nitrogen_cycle_image_cv2)
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Nitrification_hydroxylamine_to_nitrite_hao.png")
        position = ()
        if nitrogen_cycle_dir['Nitrification_hydroxylamine_to_nitrite_hao'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (476, 2370, 956, 2850)
        elif nitrogen_cycle_dir['Nitrification_hydroxylamine_to_nitrite_hao'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (482, 2440, 882, 2840)
        elif nitrogen_cycle_dir['Nitrification_hydroxylamine_to_nitrite_hao'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (488, 2456, 808, 2776)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (494, 2500, 734, 2740)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Nitrification_nitrite_to_nitrate_nxrAB.png")
        position = ()
        if nitrogen_cycle_dir['Nitrification_nitrite_to_nitrate_nxrAB'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1222, 3166, 1702, 3646)
        elif nitrogen_cycle_dir['Nitrification_nitrite_to_nitrate_nxrAB'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1266, 3254, 1666, 3654)
        elif nitrogen_cycle_dir['Nitrification_nitrite_to_nitrate_nxrAB'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (1276, 3326, 1596, 3646)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (1308, 3394, 1548, 3634)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Assimilatory_nitrate_reduction_nitrate_to_nitrite_narB_or_NR_or_nasAB.png")
        position = ()
        if nitrogen_cycle_dir['Assimilatory_nitrate_reduction_nitrate_to_nitrite_narB_or_NR_or_nasAB'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2442, 3128, 2922, 3608)
        elif nitrogen_cycle_dir['Assimilatory_nitrate_reduction_nitrate_to_nitrite_narB_or_NR_or_nasAB'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2502, 3192, 2902, 3592)
        elif nitrogen_cycle_dir['Assimilatory_nitrate_reduction_nitrate_to_nitrite_narB_or_NR_or_nasAB'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2532, 3278, 2852, 3598)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2582, 3348, 2822, 3588)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Assimilatory_nitrate_reduction_nitrite_to_ammonia_NIT-6_or_nirA.png")
        position = ()
        if nitrogen_cycle_dir['Assimilatory_nitrate_reduction_nitrite_to_ammonia_NIT-6_or_nirA'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1744, 2100, 2224, 2580)
        elif nitrogen_cycle_dir['Assimilatory_nitrate_reduction_nitrite_to_ammonia_NIT-6_or_nirA'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2004, 2276, 2404, 2676)
        elif nitrogen_cycle_dir['Assimilatory_nitrate_reduction_nitrite_to_ammonia_NIT-6_or_nirA'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2066, 2288, 2386, 2608)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2252, 2402, 2492, 2642)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Dissimilatory_nitrate_reduction_nitrate_to_nitrite_narGHI_or_napAB.png")
        position = ()
        if nitrogen_cycle_dir['Dissimilatory_nitrate_reduction_nitrate_to_nitrite_narGHI_or_napAB'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2654, 3648, 3134, 4128)
        elif nitrogen_cycle_dir['Dissimilatory_nitrate_reduction_nitrate_to_nitrite_narGHI_or_napAB'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2646, 3668, 3046, 4068)
        elif nitrogen_cycle_dir['Dissimilatory_nitrate_reduction_nitrate_to_nitrite_narGHI_or_napAB'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2702, 3682, 3022, 4002)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2764, 3700, 3004, 3940)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Dissimilatory_nitrate_reduction_nitrite_to_ammonia_nirBD_or_nrfAH.png")
        position = ()
        if nitrogen_cycle_dir['Dissimilatory_nitrate_reduction_nitrite_to_ammonia_nirBD_or_nrfAH'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2612, 2146, 3092, 2626)
        elif nitrogen_cycle_dir['Dissimilatory_nitrate_reduction_nitrite_to_ammonia_nirBD_or_nrfAH'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2578, 2118, 2978, 2518)
        elif nitrogen_cycle_dir['Dissimilatory_nitrate_reduction_nitrite_to_ammonia_nirBD_or_nrfAH'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2738, 2340, 3058, 2660)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2784, 2438, 3024, 2678)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/Denitrification_nitrite_to_nitric_oxide_nirK_or_nirS.png")
        position = ()
        if nitrogen_cycle_dir['Denitrification_nitrite_to_nitric_oxide_nirK_or_nirS'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (3226, 2448, 3706, 2928)
        elif nitrogen_cycle_dir['Denitrification_nitrite_to_nitric_oxide_nirK_or_nirS'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (3316, 2478, 3716, 2878)
        elif nitrogen_cycle_dir['Denitrification_nitrite_to_nitric_oxide_nirK_or_nirS'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3392, 2500, 3712, 2820)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3464, 2546, 3704, 2786)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/Denitrification_nitric_oxide_to_nitrous_oxide_norBC.png")
        position = ()
        if nitrogen_cycle_dir['Denitrification_nitric_oxide_to_nitrous_oxide_norBC'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (3260, 1276, 3740, 1756)
        elif nitrogen_cycle_dir['Denitrification_nitric_oxide_to_nitrous_oxide_norBC'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (3310, 1300, 3710, 1700)
        elif nitrogen_cycle_dir['Denitrification_nitric_oxide_to_nitrous_oxide_norBC'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3386, 1338, 3706, 1658)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3470, 1376, 3710, 1616)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/Denitrification_nitrous_oxide_to_nitrogen_nosZ.png")
        position = ()
        if nitrogen_cycle_dir['Denitrification_nitrous_oxide_to_nitrogen_nosZ'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2436, 452, 2916, 932)
        elif nitrogen_cycle_dir['Denitrification_nitrous_oxide_to_nitrogen_nosZ'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2506, 466, 2906, 866)
        elif nitrogen_cycle_dir['Denitrification_nitrous_oxide_to_nitrogen_nosZ'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2540, 462, 2860, 782)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2596, 476, 2836, 716)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/Anammox_nitric_oxide_+_ammonia_to_hydrazine_hzs.png")
        position = ()
        if nitrogen_cycle_dir['Anammox_nitric_oxide_+_ammonia_to_hydrazine_hzs'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2522, 1158, 3002, 1638)
        elif nitrogen_cycle_dir['Anammox_nitric_oxide_+_ammonia_to_hydrazine_hzs'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2654, 1276, 3054, 1676)
        elif nitrogen_cycle_dir['Anammox_nitric_oxide_+_ammonia_to_hydrazine_hzs'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2680, 1224, 3000, 1644)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2740, 1416, 2980, 1656)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    nitrogen_cycle_image = Image.open("Figure_tmp/nitrogen_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/Anammox_hydrazine_to_nitrogen_hdh.png")
        position = ()
        if nitrogen_cycle_dir['Anammox_hydrazine_to_nitrogen_hdh'] >= three_quarter_nitro:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1746, 434, 2226, 914)
        elif nitrogen_cycle_dir['Anammox_hydrazine_to_nitrogen_hdh'] >= two_quarter_nitro:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1830, 454, 2230, 854)
        elif nitrogen_cycle_dir['Anammox_hydrazine_to_nitrogen_hdh'] >= one_quarter_nitro:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (1916, 518, 2236, 838)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (1982, 574, 2222, 814)
        nitrogen_cycle_image_copy = nitrogen_cycle_image.copy()
        nitrogen_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        nitrogen_cycle_image_copy.save("Figure_tmp/nitrogen_cycle.png", 'png')
    except:
        pass
    
    # draw figure legend of samples
    # translate RGB to BGR; 170,0,255 -> 255,0,170
    color1 = (0, 0, 255)
    color2 = (0,127,255)
    color3 = (0,212,255)
    color4 = (0,255,255)
    color5 = (0,255,191)
    color6 = (0,255,106)
    color7 = (255,234,0)
    color8 = (255,149,0)
    color9 = (255,64,0)
    color10 = (255,0,170)
    color11 = (170,0,255)
    color12 = (185,185,237)
    color13 = (185,233,231)
    color14 = (224,237,185)
    color15 = (237,215,185)
    color16 = (237,185,220)
    color17 = (35,35,143)
    color18 = (35,106,143)
    color19 = (35,143,79)
    color20 = (143,98,35)
    colors = [color1, color2, color3, color4, color5,
              color6, color7, color8, color9, color10,
              color11, color12, color13, color14, color15,
              color16, color17, color18, color19, color20]
    samples = head.split('\t')
    Count_samples = len(samples)
    for i in range(1, Count_samples):
        nitrogen_cycle_image_cv2 = cv2.imread("Figure_tmp/nitrogen_cycle.png")
        color = colors[i-1]
        #print(str(color))
        (xmin, ymin) = (4010, 132+120*(int(i)-1))
        # (1901,66),(1941,106)
        (xmax, ymax) = (4090, 212+120*(int(i)-1))
        #(1901, 126) (1941, 166)
        cv2.rectangle(nitrogen_cycle_image_cv2,
                      (xmin, ymin), (xmax, ymax), color, -1)
    
        # draw sample_text of figure legend
        sample = samples[i]
        org = (4110, 192+120*(int(i)-1))
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 2
        color_font = (0, 0, 0)
        thickness = 4
        cv2.putText(nitrogen_cycle_image_cv2, sample, org,
                    font, fontScale, color_font, thickness)
        cv2.imwrite('Figure_tmp/nitrogen_cycle.png', nitrogen_cycle_image_cv2)
    
    # draw figure legend of pie
    nitrogen_cycle_image_cv2 = cv2.imread("Figure_tmp/nitrogen_cycle.png")
    color_cycle = (109, 118, 248)
    cv2.circle(nitrogen_cycle_image_cv2, (4004, 3600), 184, color_cycle, -1)
    cv2.circle(nitrogen_cycle_image_cv2, (4004, 3242), 154, color_cycle, -1)
    cv2.circle(nitrogen_cycle_image_cv2, (4004, 2946), 122, color_cycle, -1)
    cv2.circle(nitrogen_cycle_image_cv2, (4004, 2712), 92, color_cycle, -1)
    
    top_abun_nitro_sci = '%.2e' % (top_abun_nitro)
    three_quarter_nitro_sci = '%.2e' % (three_quarter_nitro)
    two_quarter_nitro_sci = '%.2e' % (two_quarter_nitro)
    one_quarter_nitro_sci = '%.2e' % (one_quarter_nitro)
    text1 = '>= ' + str(three_quarter_nitro_sci) + '; ' + \
        '<' + str(top_abun_nitro_sci)
    text2 = '>= ' + str(two_quarter_nitro_sci) + '; ' + \
        '<' + str(three_quarter_nitro_sci)
    text3 = '>= ' + str(one_quarter_nitro_sci) + '; ' + \
        '<' + str(two_quarter_nitro_sci)
    text4 = '> ' + str(0) + '; ' + '<' + str(one_quarter_nitro_sci)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color_font = (0, 0, 0)
    thickness = 4
    cv2.putText(nitrogen_cycle_image_cv2, text1, (4192, 3612),
                font, fontScale, color_font, thickness)
    cv2.putText(nitrogen_cycle_image_cv2, text2, (4162, 3254),
                font, fontScale, color_font, thickness)
    cv2.putText(nitrogen_cycle_image_cv2, text3, (4130, 2958),
                font, fontScale, color_font, thickness)
    cv2.putText(nitrogen_cycle_image_cv2, text4, (4096, 2724),
                font, fontScale, color_font, thickness)
    
    legend_line1 = "Figure. Relative abundances of the pathways involved in the nitrogen cycle. The pie chart indicates"
    legend_line2 = "the relative abundance of each pathway in each metagenomic sample . The size of pie charts represent"
    legend_line3 = "the total relative abundance of each pathway. ANRA, assimilatory nitrate reduction to ammonium;"
    legend_line4 = "DNRA, Dissimilatory nitrate reduction to ammonium; Anammox, anaerobic ammonium oxidation."
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color_font = (0, 0, 0)
    thickness = 4
    cv2.putText(nitrogen_cycle_image_cv2, legend_line1,
                (400, 4304), font, fontScale, color_font, thickness)
    cv2.putText(nitrogen_cycle_image_cv2, legend_line2,
                (400, 4384), font, fontScale, color_font, thickness)
    cv2.putText(nitrogen_cycle_image_cv2, legend_line3,
                (400, 4464), font, fontScale, color_font, thickness)
    cv2.putText(nitrogen_cycle_image_cv2, legend_line4,
                (400, 4542), font, fontScale, color_font, thickness)
    
    cv2.imwrite('Figure_tmp/nitrogen_cycle.png', nitrogen_cycle_image_cv2)
    
    os.system('mv Figure_tmp/nitrogen_cycle.png ./nitrogen_cycle_sketch.png')
    
    
    # sulfur cycle
    sulfur_cycle_background_fig = background_image_pathway + "/sulfur_cycle.png"
    shutil.copy(sulfur_cycle_background_fig, './Figure_tmp/')
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    #print("background_image_size:", sulfur_cycle_image.size)
    sulfur_cycle = ['Sulfur_reduction_sulfur_to_sulfide_sreABC',
                    'Sulfide_oxidation_sulfide_to_sulfur_fccAB',
                    'Sulfur_disproportionation_sulfur_to_sulfide_sulfite',
                    'Dissimilatory_sulfate_reduction_sulfate_to_sulfite_reversible_sat_and_aprAB',
                    'Dissimilatory_sulfate_reduction_sulfite_to_sulfide_reversible_dsrAB',
                    'Assimilatory_sulfate_reduction_sulfate_to_sulfite',
                    'Assimilatory_sulfate_reduction_sulfite_to_sulfide_cysJI_or_sir',
                    'Sulfite_oxidation_sulfite_to_sulfate_sorB_SUOX_soeABC',
                    'Thiosulfate_disproportionation_thiosulfate_to_sulfide_sulfite_phsABC',
                    'Thiosulfate_oxidation_SOX_doxAD_and_tsdA',
                    ]
    
    sulfur_cycle_dir = {}
    for i in sulfur_cycle:
        sulfur_cycle_dir[i] = total_abun_pathway_dir[i]
    
    # get the most abundance of sulfur cycle pathways
    top_abun_sulfur = int(0)
    for key in sulfur_cycle_dir:
        if sulfur_cycle_dir[key] > top_abun_sulfur:
            top_abun_sulfur = sulfur_cycle_dir[key]
    three_quarter_sulfur = 3/4 * top_abun_sulfur
    two_quarter_sulfur = 1/2 * top_abun_sulfur
    one_quarter_sulfur = 1/4 * top_abun_sulfur
    #print(top_abun_sulfur)
    
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Sulfur_reduction_sulfur_to_sulfide_sreABC.png")
        position = ()
        if sulfur_cycle_dir['Sulfur_reduction_sulfur_to_sulfide_sreABC'] >= three_quarter_sulfur:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (3183, 50, 3663, 530)
        elif sulfur_cycle_dir['Sulfur_reduction_sulfur_to_sulfide_sreABC'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (3194, 112, 3594, 512)
        elif sulfur_cycle_dir['Sulfur_reduction_sulfur_to_sulfide_sreABC'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3237, 189, 3557, 509)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3242, 251, 3482, 491)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Sulfide_oxidation_sulfide_to_sulfur_fccAB.png")
        position = ()
        if sulfur_cycle_dir['Sulfide_oxidation_sulfide_to_sulfur_fccAB'] >= three_quarter_sulfur:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2796, 454, 3276, 934)
        elif sulfur_cycle_dir['Sulfide_oxidation_sulfide_to_sulfur_fccAB'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2839, 471, 3239, 871)
        elif sulfur_cycle_dir['Sulfide_oxidation_sulfide_to_sulfur_fccAB'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2915, 499, 3235, 819)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2952, 505, 3192, 745)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Sulfur_disproportionation_sulfur_to_sulfide_sulfite.png")
        position = ()
        if sulfur_cycle_dir['Sulfur_disproportionation_sulfur_to_sulfide_sulfite'] >= three_quarter_sulfur:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2862, 1327, 3342, 1807)
        elif sulfur_cycle_dir['Sulfur_disproportionation_sulfur_to_sulfide_sulfite'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2943, 1342, 3343, 1742)
        elif sulfur_cycle_dir['Sulfur_disproportionation_sulfur_to_sulfide_sulfite'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3022, 1342, 3342, 1662)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3111, 1341, 3351, 1581)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Dissimilatory_sulfate_reduction_sulfate_to_sulfite_reversible_sat_and_aprAB.png")
        position = ()
        if sulfur_cycle_dir['Dissimilatory_sulfate_reduction_sulfate_to_sulfite_reversible_sat_and_aprAB'] >= three_quarter_sulfur:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (828, 2864, 1308, 3344)
        elif sulfur_cycle_dir['Dissimilatory_sulfate_reduction_sulfate_to_sulfite_reversible_sat_and_aprAB'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (914, 2992, 1314, 3392)
        elif sulfur_cycle_dir['Dissimilatory_sulfate_reduction_sulfate_to_sulfite_reversible_sat_and_aprAB'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (909, 3033, 1229, 3353)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (900, 3057, 1140, 3297)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Dissimilatory_sulfate_reduction_sulfite_to_sulfide_reversible_dsrAB.png")
        position = ()
        if sulfur_cycle_dir['Dissimilatory_sulfate_reduction_sulfite_to_sulfide_reversible_dsrAB'] >= three_quarter_sulfur:
            #print('test!')
            pathway_fig = pathway_fig.resize((480, 480))
            position = (804, 804, 1284, 1284)
        elif sulfur_cycle_dir['Dissimilatory_sulfate_reduction_sulfite_to_sulfide_reversible_dsrAB'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (861, 766, 1261, 1166)
        elif sulfur_cycle_dir['Dissimilatory_sulfate_reduction_sulfite_to_sulfide_reversible_dsrAB'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (890, 788, 1210, 1108)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (865, 845, 1105, 1085)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Assimilatory_sulfate_reduction_sulfate_to_sulfite.png")
        position = ()
        if sulfur_cycle_dir['Assimilatory_sulfate_reduction_sulfate_to_sulfite'] >= three_quarter_sulfur:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (417, 3235, 897, 3715)
        elif sulfur_cycle_dir['Assimilatory_sulfate_reduction_sulfate_to_sulfite'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (478, 3250, 878, 3650)
        elif sulfur_cycle_dir['Assimilatory_sulfate_reduction_sulfate_to_sulfite'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (567, 3308, 887, 3628)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (634, 3334, 874, 3574)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Assimilatory_sulfate_reduction_sulfite_to_sulfide_cysJI_or_sir.png")
        position = ()
        if sulfur_cycle_dir['Assimilatory_sulfate_reduction_sulfite_to_sulfide_cysJI_or_sir'] >= three_quarter_sulfur:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (252, 559, 732, 1039)
        elif sulfur_cycle_dir['Assimilatory_sulfate_reduction_sulfite_to_sulfide_cysJI_or_sir'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (379, 586, 779, 986)
        elif sulfur_cycle_dir['Assimilatory_sulfate_reduction_sulfite_to_sulfide_cysJI_or_sir'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (526, 531, 846, 851)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (649, 546, 889, 786)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Sulfite_oxidation_sulfite_to_sulfate_sorB_SUOX_soeABC.png")
        position = ()
        if sulfur_cycle_dir['Sulfite_oxidation_sulfite_to_sulfate_sorB_SUOX_soeABC'] >= three_quarter_sulfur:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2902, 3237, 3382, 3717)
        elif sulfur_cycle_dir['Sulfite_oxidation_sulfite_to_sulfate_sorB_SUOX_soeABC'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2947, 3306, 3347, 3706)
        elif sulfur_cycle_dir['Sulfite_oxidation_sulfite_to_sulfate_sorB_SUOX_soeABC'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3017, 3364, 3337, 3684)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3074, 3428, 3314, 3668)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Thiosulfate_disproportionation_thiosulfate_to_sulfide_sulfite_phsABC.png")
        position = ()
        if sulfur_cycle_dir['Thiosulfate_disproportionation_thiosulfate_to_sulfide_sulfite_phsABC'] >= three_quarter_sulfur:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2201, 1367, 2681, 1847)
        elif sulfur_cycle_dir['Thiosulfate_disproportionation_thiosulfate_to_sulfide_sulfite_phsABC'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2196, 1433, 2596, 1833)
        elif sulfur_cycle_dir['Thiosulfate_disproportionation_thiosulfate_to_sulfide_sulfite_phsABC'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2180, 1504, 2500, 1824)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2171, 1573, 2411, 1813)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    sulfur_cycle_image = Image.open("Figure_tmp/sulfur_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Thiosulfate_oxidation_SOX_doxAD_and_tsdA.png")
        position = ()
        if sulfur_cycle_dir['Thiosulfate_oxidation_SOX_doxAD_and_tsdA'] >= three_quarter_sulfur:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1660, 2890, 2140, 3370)
        elif sulfur_cycle_dir['Thiosulfate_oxidation_SOX_doxAD_and_tsdA'] >= two_quarter_sulfur:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1666, 2953, 2066, 3353)
        elif sulfur_cycle_dir['Thiosulfate_oxidation_SOX_doxAD_and_tsdA'] >= one_quarter_sulfur:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (1677, 3010, 1997, 3330)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (1668, 3012, 1908, 3252)
        sulfur_cycle_image_copy = sulfur_cycle_image.copy()
        sulfur_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        sulfur_cycle_image_copy.save("Figure_tmp/sulfur_cycle.png", 'png')
    except:
        pass
    
    # draw figure legend of samples
    color1 = (0, 0, 255)
    color2 = (0,127,255)
    color3 = (0,212,255)
    color4 = (0,255,255)
    color5 = (0,255,191)
    color6 = (0,255,106)
    color7 = (255,234,0)
    color8 = (255,149,0)
    color9 = (255,64,0)
    color10 = (255,0,170)
    color11 = (170,0,255)
    color12 = (185,185,237)
    color13 = (185,233,231)
    color14 = (224,237,185)
    color15 = (237,215,185)
    color16 = (237,185,220)
    color17 = (35,35,143)
    color18 = (35,106,143)
    color19 = (35,143,79)
    color20 = (143,98,35)
    colors = [color1, color2, color3, color4, color5,
              color6, color7, color8, color9, color10,
              color11, color12, color13, color14, color15,
              color16, color17, color18, color19, color20]
    samples = head.split('\t')
    Count_samples = len(samples)
    for i in range(1, Count_samples):
        sulfur_cycle_image_cv2 = cv2.imread("Figure_tmp/sulfur_cycle.png")
        color = colors[i-1]
        #print(str(color))
        (xmin, ymin) = (4274, 132+120*(int(i)-1))
        # (1901,66),(1941,106)
        (xmax, ymax) = (4354, 212+120*(int(i)-1))
        #(1901, 126) (1941, 166)
        cv2.rectangle(sulfur_cycle_image_cv2, (xmin, ymin),
                      (xmax, ymax), color, -1)
    
        # draw sample_text of figure legend
        sample = samples[i]
        org = (4374, 192+120*(int(i)-1))
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 2
        color_font = (0, 0, 0)
        thickness = 4
        cv2.putText(sulfur_cycle_image_cv2, sample, org,
                    font, fontScale, color_font, thickness)
        cv2.imwrite('Figure_tmp/sulfur_cycle.png', sulfur_cycle_image_cv2)
    
    # draw figure legend of pie
    sulfur_cycle_image_cv2 = cv2.imread("Figure_tmp/sulfur_cycle.png")
    color_cycle = (109, 118, 248)
    cv2.circle(sulfur_cycle_image_cv2, (4314, 3828), 184, color_cycle, -1)
    cv2.circle(sulfur_cycle_image_cv2, (4314, 3470), 154, color_cycle, -1)
    cv2.circle(sulfur_cycle_image_cv2, (4314, 3174), 122, color_cycle, -1)
    cv2.circle(sulfur_cycle_image_cv2, (4314, 2940), 92, color_cycle, -1)
    
    top_abun_sulfur_sci = '%.2e' % (top_abun_sulfur)
    three_quarter_sulfur_sci = '%.2e' % (three_quarter_sulfur)
    two_quarter_sulfur_sci = '%.2e' % (two_quarter_sulfur)
    one_quarter_sulfur_sci = '%.2e' % (one_quarter_sulfur)
    text1 = '>= ' + str(three_quarter_sulfur_sci) + '; ' + \
        '<' + str(top_abun_sulfur_sci)
    text2 = '>= ' + str(two_quarter_sulfur_sci) + '; ' + \
        '<' + str(three_quarter_sulfur_sci)
    text3 = '>= ' + str(one_quarter_sulfur_sci) + '; ' + \
        '<' + str(two_quarter_sulfur_sci)
    text4 = '> ' + str(0) + '; ' + '<' + str(one_quarter_sulfur_sci)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color_font = (0, 0, 0)
    thickness = 4
    cv2.putText(sulfur_cycle_image_cv2, text1, (4518, 3840),
                font, fontScale, color_font, thickness)
    cv2.putText(sulfur_cycle_image_cv2, text2, (4488, 3482),
                font, fontScale, color_font, thickness)
    cv2.putText(sulfur_cycle_image_cv2, text3, (4456, 3186),
                font, fontScale, color_font, thickness)
    cv2.putText(sulfur_cycle_image_cv2, text4, (4426, 2952),
                font, fontScale, color_font, thickness)
    
    legend_line1 = "Figure. Relative abundances of the pathways involved in the sulfur cycle. The pie chart indicates"
    legend_line2 = "the relative abundance of each pathway in each metagenomic sample . The size of pie charts represent"
    legend_line3 = "the total relative abundance of each pathway. ASR, assimilatory sulfate reduction; DSR, dissimilatory"
    legend_line4 = "sulfate reduction."
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color_font = (0, 0, 0)
    thickness = 4
    cv2.putText(sulfur_cycle_image_cv2, legend_line1, (420, 4182),
                font, fontScale, color_font, thickness)
    cv2.putText(sulfur_cycle_image_cv2, legend_line2, (420, 4262),
                font, fontScale, color_font, thickness)
    cv2.putText(sulfur_cycle_image_cv2, legend_line3, (420, 4342),
                font, fontScale, color_font, thickness)
    cv2.putText(sulfur_cycle_image_cv2, legend_line4, (420, 4422),
                font, fontScale, color_font, thickness)
    
    cv2.imwrite('Figure_tmp/sulfur_cycle.png', sulfur_cycle_image_cv2)
    
    os.system('mv Figure_tmp/sulfur_cycle.png ./sulfur_cycle_sketch.png')
    


    #DMSP cycle
    DMSP_cycle_background_fig = background_image_pathway + "/DMSP_cycle.png"
    shutil.copy(DMSP_cycle_background_fig, './Figure_tmp/')
    DMSP_cycle_image = Image.open("Figure_tmp/DMSP_cycle.png")
    #print("background_image_size:", carbon_cycle_image.size)
    DMSP_cycle = ['DMSP_biosynthesis_L-Met_to_DMSP_DSYB_or_dsyB_or_mmtN',
                  'DMSP_demethylation_DMSP_to_MMPA_dmdA',
                  'DMSP_demethylation_MMPA_to_MeSH_dmdBCD_or_acuH',
                  'DMSP_cleavage_DMSP_to_DMS_ddds_or_alma1',
                  'DMS_oxidation_DMS_to_MeSH_dmoA',
                  'DMS_oxidation_DMS_to_DMSO_ddhABC_or_tmm',
                  'DMSO_reduction_DMSO_to_DMS_dms_or_dorA',
                  'MddA_pathway_MeSH_to_DMS_mddA',
                  'MeSH_oxidation_MeSH_to_Formaldehyde_MTO'
                 ]
    
    DMSP_cycle_dir = {}
    for i in DMSP_cycle:
        DMSP_cycle_dir[i] = total_abun_pathway_dir[i]
    
    # get the most abundance of DMSP cycle pathways
    top_abun_DMSP = int(0)
    for key in DMSP_cycle_dir:
        if DMSP_cycle_dir[key] > top_abun_DMSP:
            top_abun_DMSP = DMSP_cycle_dir[key]
    three_quarter_DMSP = 3/4 * top_abun_DMSP
    two_quarter_DMSP = 1/2 * top_abun_DMSP
    one_quarter_DMSP = 1/4 * top_abun_DMSP

    try:
        pathway_fig = Image.open("Figure_tmp/DMSP_biosynthesis_L-Met_to_DMSP_DSYB_or_dsyB_or_mmtN.png")
        position = ()
        if DMSP_cycle_dir['DMSP_biosynthesis_L-Met_to_DMSP_DSYB_or_dsyB_or_mmtN'] >= three_quarter_DMSP:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (544, 2523, 1024, 732)
        elif DMSP_cycle_dir['DMSP_biosynthesis_L-Met_to_DMSP_DSYB_or_dsyB_or_mmtN'] >= two_quarter_DMSP:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (555, 2574, 955, 2974)
        elif DMSP_cycle_dir['DMSP_biosynthesis_L-Met_to_DMSP_DSYB_or_dsyB_or_mmtN'] >= one_quarter_DMSP:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (514, 2587, 834, 2907)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (518, 2630, 758, 2870)
        DMSP_cycle_image_copy = DMSP_cycle_image.copy()
        DMSP_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        DMSP_cycle_image_copy.save("Figure_tmp/DMSP_cycle.png", 'png')
    except:
        pass

    DMSP_cycle_image = Image.open("Figure_tmp/DMSP_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/DMSP_demethylation_DMSP_to_MMPA_dmdA.png")
        position = ()
        if DMSP_cycle_dir['DMSP_demethylation_DMSP_to_MMPA_dmdA'] >= three_quarter_DMSP:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1185, 2331, 1665, 2811)
        elif DMSP_cycle_dir['DMSP_demethylation_DMSP_to_MMPA_dmdA'] >= two_quarter_DMSP:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1189, 2335, 1589, 2735)
        elif DMSP_cycle_dir['DMSP_demethylation_DMSP_to_MMPA_dmdA'] >= one_quarter_DMSP:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (1200, 2398, 1520, 2718)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (1240, 2509, 1480, 2749)
        DMSP_cycle_image_copy = DMSP_cycle_image.copy()
        DMSP_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        DMSP_cycle_image_copy.save("Figure_tmp/DMSP_cycle.png", 'png')
    except:
        pass

    DMSP_cycle_image = Image.open("Figure_tmp/DMSP_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/DMSP_demethylation_MMPA_to_MeSH_dmdBCD_or_acuH.png")
        position = ()
        if DMSP_cycle_dir['DMSP_demethylation_MMPA_to_MeSH_dmdBCD_or_acuH'] >= three_quarter_DMSP:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1213, 630, 1693, 1110)
        elif DMSP_cycle_dir['DMSP_demethylation_MMPA_to_MeSH_dmdBCD_or_acuH'] >= two_quarter_DMSP:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1173, 761, 1573, 1161)
        elif DMSP_cycle_dir['DMSP_demethylation_MMPA_to_MeSH_dmdBCD_or_acuH'] >= one_quarter_DMSP:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (1160, 796, 1480, 1116)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (1160, 884, 1400, 1124)
        DMSP_cycle_image_copy = DMSP_cycle_image.copy()
        DMSP_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        DMSP_cycle_image_copy.save("Figure_tmp/DMSP_cycle.png", 'png')
    except:
        pass

    DMSP_cycle_image = Image.open("Figure_tmp/DMSP_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/DMSP_cleavage_DMSP_to_DMS_ddds_or_alma1.png")
        position = ()
        if DMSP_cycle_dir['DMSP_cleavage_DMSP_to_DMS_ddds_or_alma1'] >= three_quarter_DMSP:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2736, 2513, 3216, 2993)
        elif DMSP_cycle_dir['DMSP_cleavage_DMSP_to_DMS_ddds_or_alma1'] >= two_quarter_DMSP:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2811, 2545, 3211, 2945)
        elif DMSP_cycle_dir['DMSP_cleavage_DMSP_to_DMS_ddds_or_alma1'] >= one_quarter_DMSP:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2894, 2573, 3214, 2893)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2965, 2636, 3205, 2876)
        DMSP_cycle_image_copy = DMSP_cycle_image.copy()
        DMSP_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        DMSP_cycle_image_copy.save("Figure_tmp/DMSP_cycle.png", 'png')
    except:
        pass

    DMSP_cycle_image = Image.open("Figure_tmp/DMSP_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/DMS_oxidation_DMS_to_MeSH_dmoA.png")
        position = ()
        if DMSP_cycle_dir['DMS_oxidation_DMS_to_MeSH_dmoA'] >= three_quarter_DMSP:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (3116, 266, 3596, 746)
        elif DMSP_cycle_dir['DMS_oxidation_DMS_to_MeSH_dmoA'] >= two_quarter_DMSP:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (3131, 314, 3531, 714)
        elif DMSP_cycle_dir['DMS_oxidation_DMS_to_MeSH_dmoA'] >= one_quarter_DMSP:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3195, 432, 3515, 752)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3207, 487, 3447, 727)
        DMSP_cycle_image_copy = DMSP_cycle_image.copy()
        DMSP_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        DMSP_cycle_image_copy.save("Figure_tmp/DMSP_cycle.png", 'png')
    except:
        pass

    DMSP_cycle_image = Image.open("Figure_tmp/DMSP_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/DMS_oxidation_DMS_to_DMSO_ddhABC_or_tmm.png")
        position = ()
        if DMSP_cycle_dir['DMS_oxidation_DMS_to_DMSO_ddhABC_or_tmm'] >= three_quarter_DMSP:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2290, 1795, 2770, 2275)
        elif DMSP_cycle_dir['DMS_oxidation_DMS_to_DMSO_ddhABC_or_tmm'] >= two_quarter_DMSP:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2306, 1805, 2706, 2205)
        elif DMSP_cycle_dir['DMS_oxidation_DMS_to_DMSO_ddhABC_or_tmm'] >= one_quarter_DMSP:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2367, 1806, 2687, 2126)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2470, 1811, 2710, 2051)
        DMSP_cycle_image_copy = DMSP_cycle_image.copy()
        DMSP_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        DMSP_cycle_image_copy.save("Figure_tmp/DMSP_cycle.png", 'png')
    except:
        pass

    DMSP_cycle_image = Image.open("Figure_tmp/DMSP_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/DMSO_reduction_DMSO_to_DMS_dms_or_dorA.png")
        position = ()
        if DMSP_cycle_dir['DMSO_reduction_DMSO_to_DMS_dms_or_dorA'] >= three_quarter_DMSP:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2531, 1270, 3011, 1750)
        elif DMSP_cycle_dir['DMSO_reduction_DMSO_to_DMS_dms_or_dorA'] >= two_quarter_DMSP:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2563, 1355, 2963, 1755)
        elif DMSP_cycle_dir['DMSO_reduction_DMSO_to_DMS_dms_or_dorA'] >= one_quarter_DMSP:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2591, 1410, 2911, 1730)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2608, 1487, 2848, 1727)
        DMSP_cycle_image_copy = DMSP_cycle_image.copy()
        DMSP_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        DMSP_cycle_image_copy.save("Figure_tmp/DMSP_cycle.png", 'png')
    except:
        pass

    DMSP_cycle_image = Image.open("Figure_tmp/DMSP_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/MddA_pathway_MeSH_to_DMS_mddA.png")
        position = ()
        if DMSP_cycle_dir['MddA_pathway_MeSH_to_DMS_mddA'] >= three_quarter_DMSP:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2714, 591, 3194, 1071)
        elif DMSP_cycle_dir['MddA_pathway_MeSH_to_DMS_mddA'] >= two_quarter_DMSP:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2796, 640, 3196, 1040)
        elif DMSP_cycle_dir['MddA_pathway_MeSH_to_DMS_mddA'] >= one_quarter_DMSP:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2845, 640, 3165, 960)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2936, 689, 3176, 929)
        DMSP_cycle_image_copy = DMSP_cycle_image.copy()
        DMSP_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        DMSP_cycle_image_copy.save("Figure_tmp/DMSP_cycle.png", 'png')
    except:
        pass

    DMSP_cycle_image = Image.open("Figure_tmp/DMSP_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/MeSH_oxidation_MeSH_to_Formaldehyde_MTO.png")
        position = ()
        if DMSP_cycle_dir['MeSH_oxidation_MeSH_to_Formaldehyde_MTO'] >= three_quarter_DMSP:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (602, 420, 1082, 900)
        elif DMSP_cycle_dir['MeSH_oxidation_MeSH_to_Formaldehyde_MTO'] >= two_quarter_DMSP:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (648, 403, 1048, 803)
        elif DMSP_cycle_dir['MeSH_oxidation_MeSH_to_Formaldehyde_MTO'] >= one_quarter_DMSP:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (722, 379, 1042, 699)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (785, 358, 1025, 598)
        DMSP_cycle_image_copy = DMSP_cycle_image.copy()
        DMSP_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        DMSP_cycle_image_copy.save("Figure_tmp/DMSP_cycle.png", 'png')
    except:
        pass

    # draw figure legend of samples
    color1 = (0, 0, 255)
    color2 = (0,127,255)
    color3 = (0,212,255)
    color4 = (0,255,255)
    color5 = (0,255,191)
    color6 = (0,255,106)
    color7 = (255,234,0)
    color8 = (255,149,0)
    color9 = (255,64,0)
    color10 = (255,0,170)
    color11 = (170,0,255)
    color12 = (185,185,237)
    color13 = (185,233,231)
    color14 = (224,237,185)
    color15 = (237,215,185)
    color16 = (237,185,220)
    color17 = (35,35,143)
    color18 = (35,106,143)
    color19 = (35,143,79)
    color20 = (143,98,35)
    colors = [color1, color2, color3, color4, color5,
              color6, color7, color8, color9, color10,
              color11, color12, color13, color14, color15,
              color16, color17, color18, color19, color20]
    samples = head.split('\t')
    Count_samples = len(samples)
    for i in range(1, Count_samples):
        DMSP_cycle_image_cv2 = cv2.imread("Figure_tmp/DMSP_cycle.png")
        color = colors[i-1]
        #print(str(color))
        (xmin, ymin) = (4274, 132+120*(int(i)-1))
        # (1901,66),(1941,106)
        (xmax, ymax) = (4354, 212+120*(int(i)-1))
        #(1901, 126) (1941, 166)
        cv2.rectangle(DMSP_cycle_image_cv2, (xmin, ymin),
                      (xmax, ymax), color, -1)
    
        # draw sample_text of figure legend
        sample = samples[i]
        org = (4374, 192+120*(int(i)-1))
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 2
        color_font = (0, 0, 0)
        thickness = 4
        cv2.putText(DMSP_cycle_image_cv2, sample, org,
                    font, fontScale, color_font, thickness)
        cv2.imwrite('Figure_tmp/DMSP_cycle.png', DMSP_cycle_image_cv2)
    
    # draw figure legend of pie
    DMSP_cycle_image_cv2 = cv2.imread("Figure_tmp/DMSP_cycle.png")
    color_cycle = (109, 118, 248)
    cv2.circle(DMSP_cycle_image_cv2, (4314, 3828), 184, color_cycle, -1)
    cv2.circle(DMSP_cycle_image_cv2, (4314, 3470), 154, color_cycle, -1)
    cv2.circle(DMSP_cycle_image_cv2, (4314, 3174), 122, color_cycle, -1)
    cv2.circle(DMSP_cycle_image_cv2, (4314, 2940), 92, color_cycle, -1)
    
    top_abun_DMSP_sci = '%.2e' % (top_abun_DMSP)
    three_quarter_DMSP_sci = '%.2e' % (three_quarter_DMSP)
    two_quarter_DMSP_sci = '%.2e' % (two_quarter_DMSP)
    one_quarter_DMSP_sci = '%.2e' % (one_quarter_DMSP)
    text1 = '>= ' + str(three_quarter_DMSP_sci) + '; ' + \
        '<' + str(top_abun_DMSP_sci)
    text2 = '>= ' + str(two_quarter_DMSP_sci) + '; ' + \
        '<' + str(three_quarter_DMSP_sci)
    text3 = '>= ' + str(one_quarter_DMSP_sci) + '; ' + \
        '<' + str(two_quarter_DMSP_sci)
    text4 = '> ' + str(0) + '; ' + '<' + str(one_quarter_DMSP_sci)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color_font = (0, 0, 0)
    thickness = 4
    cv2.putText(DMSP_cycle_image_cv2, text1, (4518, 3840),
                font, fontScale, color_font, thickness)
    cv2.putText(DMSP_cycle_image_cv2, text2, (4488, 3482),
                font, fontScale, color_font, thickness)
    cv2.putText(DMSP_cycle_image_cv2, text3, (4456, 3186),
                font, fontScale, color_font, thickness)
    cv2.putText(DMSP_cycle_image_cv2, text4, (4426, 2952),
                font, fontScale, color_font, thickness)
    
    legend_line1 = "Figure. Relative abundances of the pathways involved in the DMSP cycle. The pie chart indicates"
    legend_line2 = "the relative abundance of each pathway in each metagenomic sample. The size of pie charts represent"
    legend_line3 = "the total relative abundance of each pathway."
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color_font = (0, 0, 0)
    thickness = 4
    cv2.putText(DMSP_cycle_image_cv2, legend_line1, (420, 4182),
                font, fontScale, color_font, thickness)
    cv2.putText(DMSP_cycle_image_cv2, legend_line2, (420, 4262),
                font, fontScale, color_font, thickness)
    cv2.putText(DMSP_cycle_image_cv2, legend_line3, (420, 4342),
                font, fontScale, color_font, thickness)
    
    cv2.imwrite('Figure_tmp/DMSP_cycle.png', DMSP_cycle_image_cv2)
    
    os.system('mv Figure_tmp/DMSP_cycle.png ./DMSP_cycle_sketch.png')




    # carbon cycle
    carbon_cycle_background_fig = background_image_pathway + "/carbon_cycle.png"
    shutil.copy(carbon_cycle_background_fig, './Figure_tmp/')
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    #print("background_image_size:", carbon_cycle_image.size)
    carbon_cycle = ['CBB_cycle_prkB',
                    'rTCA_cycle_aclAB_ccsAB_ccl',
                    'Wood-Ljungdahl_pathway_acsABCDE',
                    '3-Hydroxypropionate_Bicycle',
                    #'Dicarboxylate-hydroxybutyrate_cycle',
                    'Glycolysis_glk_pfk_pyk',
                    'Entner-Doudoroff_pathway_glucose-6P_to_glyceraldehyde-3P_+_pyruvate',
                    'TCA_cycle',
                    'Methanogenesis_CO2_to_methane',
                    'Methanogenesis_acetate_to_methane_cdhCDE',
                    'Methanogenesis_methanol_to_methane_mtaABC',
                    'Methane_oxidation_methane_to_methanol_mmoBCDXYZ_amoABC',
                    'Methane_oxidation_methanol_to_formaldehyde_mxaFI_xoxF',
                    'Fermentation_to_acetate_pyruvate_to_acetate_poxB_poxL_acyP',
                    'Fermentation_to_acetate_acetyl-CoA_to_acetate_ach1_eutD_pta_acyP',
                    'Fermentation_to_acetate_lactate_to_acetate_EC:1.13.12.4',
                    'Fermentation_to_lactate_pyruvate_to_lactate_LDH',
                    'Fermentation_to_formate_pyruvate_to_formate_pf1D',
                    'Fermentation_to_formate_to_CO2_H2_fdh',
                    'Fermentation_to_ethanol_acetate_to_acetylaldehyde_ald',
                    'Fermentation_to_ethanol_acetyl-CoA_to_acetylaldehyde_reversible',
                    'Fermentation_to_ethanol_acetylaldehyde_to_ethanol_adh_mdh'
                    ]
    
    carbon_cycle_dir = {}
    for i in carbon_cycle:
        carbon_cycle_dir[i] = total_abun_pathway_dir[i]
    
    # get the most abundance of DMSP cycle pathways
    top_abun_carbon = int(0)
    for key in carbon_cycle_dir:
        if carbon_cycle_dir[key] > top_abun_carbon:
            top_abun_carbon = carbon_cycle_dir[key]
    three_quarter_carbon = 3/4 * top_abun_carbon
    two_quarter_carbon = 1/2 * top_abun_carbon
    one_quarter_carbon = 1/4 * top_abun_carbon
    
    try:
        pathway_fig = Image.open("Figure_tmp/CBB_cycle_prkB.png")
        position = ()
        if carbon_cycle_dir['CBB_cycle_prkB'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2343, 432, 2823, 912)
        elif carbon_cycle_dir['CBB_cycle_prkB'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2391, 500, 2791, 900)
        elif carbon_cycle_dir['CBB_cycle_prkB'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2429, 580, 2749, 900)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2471, 645, 2711, 885)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/rTCA_cycle_aclAB_ccsAB_ccl.png")
        position = ()
        if carbon_cycle_dir['rTCA_cycle_aclAB_ccsAB_ccl'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (3244, 420, 3724, 900)
        elif carbon_cycle_dir['rTCA_cycle_aclAB_ccsAB_ccl'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (3277, 500, 3677, 900)
        elif carbon_cycle_dir['rTCA_cycle_aclAB_ccsAB_ccl'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3318, 580, 3638, 900)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3363, 660, 3603, 900)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/Wood-Ljungdahl_pathway_acsABCDE.png")
        position = ()
        if carbon_cycle_dir['Wood-Ljungdahl_pathway_acsABCDE'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (3722, 1049, 4202, 1529)
        elif carbon_cycle_dir['Wood-Ljungdahl_pathway_acsABCDE'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (3761, 1050, 4161, 1450)
        elif carbon_cycle_dir['Wood-Ljungdahl_pathway_acsABCDE'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3803, 1082, 4123, 1402)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3842, 1085, 4082, 1325)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/3-Hydroxypropionate_Bicycle.png")
        position = ()
        if carbon_cycle_dir['3-Hydroxypropionate_Bicycle'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2783, 1042, 3263, 1522)
        elif carbon_cycle_dir['3-Hydroxypropionate_Bicycle'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2838, 1059, 3238, 1459)
        elif carbon_cycle_dir['3-Hydroxypropionate_Bicycle'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2871, 1065, 3191, 1385)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2910, 1082, 3150, 1322)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    #carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    #try:
        #pathway_fig = Image.open(
            #"Figure_tmp/Dicarboxylate-hydroxybutyrate_cycle.png")
        #position = ()
        #if carbon_cycle_dir['Dicarboxylate-hydroxybutyrate_cycle'] >= three_quarter_carbon:
            #pathway_fig = pathway_fig.resize((480, 480))
            #position = (3722, 1049, 4202, 1529)
        #elif carbon_cycle_dir['Dicarboxylate-hydroxybutyrate_cycle'] >= two_quarter_carbon:
            #pathway_fig = pathway_fig.resize((400, 400))
            #position = (3761, 1050, 4161, 1450)
        #elif carbon_cycle_dir['Dicarboxylate-hydroxybutyrate_cycle'] >= one_quarter_carbon:
            #pathway_fig = pathway_fig.resize((320, 320))
            #position = (3803, 1082, 4123, 1402)
        #else:
            #pathway_fig = pathway_fig.resize((240, 240))
            #position = (3842, 1085, 4082, 1325)
        #carbon_cycle_image_copy = carbon_cycle_image.copy()
        #carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        #carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    #except:
        #pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/Glycolysis_glk_pfk_pyk.png")
        position = ()
        if carbon_cycle_dir['Glycolysis_glk_pfk_pyk'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1076, 1934, 1556, 2414)
        elif carbon_cycle_dir['Glycolysis_glk_pfk_pyk'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1076, 1939, 1476, 2339)
        elif carbon_cycle_dir['Glycolysis_glk_pfk_pyk'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (1086, 1943, 1406, 2263)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (1100, 1948, 1340, 2188)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Entner-Doudoroff_pathway_glucose-6P_to_glyceraldehyde-3P_+_pyruvate.png")
        position = ()
        if carbon_cycle_dir['Entner-Doudoroff_pathway_glucose-6P_to_glyceraldehyde-3P_+_pyruvate'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (494, 1934, 974, 2414)
        elif carbon_cycle_dir['Entner-Doudoroff_pathway_glucose-6P_to_glyceraldehyde-3P_+_pyruvate'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (566, 1939, 966, 2339)
        elif carbon_cycle_dir['Entner-Doudoroff_pathway_glucose-6P_to_glyceraldehyde-3P_+_pyruvate'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (642, 1943, 962, 2263)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (712, 1948, 952, 2188)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/TCA_cycle.png")
        position = ()
        if carbon_cycle_dir['TCA_cycle'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2713, 4645, 3193, 5125)
        elif carbon_cycle_dir['TCA_cycle'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2792, 4669, 3192, 5069)
        elif carbon_cycle_dir['TCA_cycle'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2865, 4704, 3185, 5024)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2935, 4732, 3175, 4972)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/Methanogenesis_CO2_to_methane.png")
        position = ()
        if carbon_cycle_dir['Methanogenesis_CO2_to_methane'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (5404, 841, 5884, 1321)
        elif carbon_cycle_dir['Methanogenesis_CO2_to_methane'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (5427, 905, 5827, 1305)
        elif carbon_cycle_dir['Methanogenesis_CO2_to_methane'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (5441, 952, 5761, 1272)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (5437, 998, 5677, 1238)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Methanogenesis_acetate_to_methane_cdhCDE.png")
        position = ()
        if carbon_cycle_dir['Methanogenesis_acetate_to_methane_cdhCDE'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (5611, 2213, 6091, 2693)
        elif carbon_cycle_dir['Methanogenesis_acetate_to_methane_cdhCDE'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (5620, 2268, 6020, 2668)
        elif carbon_cycle_dir['Methanogenesis_acetate_to_methane_cdhCDE'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (5629, 2298, 5949, 2618)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (5636, 2353, 5876, 2593)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Methanogenesis_methanol_to_methane_mtaABC.png")
        position = ()
        if carbon_cycle_dir['Methanogenesis_methanol_to_methane_mtaABC'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (4562, 1753, 5042, 2233)
        elif carbon_cycle_dir['Methanogenesis_methanol_to_methane_mtaABC'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (4596, 1757, 4996, 2157)
        elif carbon_cycle_dir['Methanogenesis_methanol_to_methane_mtaABC'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (4640, 1772, 4960, 2092)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (4678, 1779, 4918, 2019)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Methane_oxidation_methane_to_methanol_mmoBCDXYZ_amoABC.png")
        position = ()
        if carbon_cycle_dir['Methane_oxidation_methane_to_methanol_mmoBCDXYZ_amoABC'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (4648, 1227, 5128, 1707)
        elif carbon_cycle_dir['Methane_oxidation_methane_to_methanol_mmoBCDXYZ_amoABC'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (4704, 1290, 5104, 1690)
        elif carbon_cycle_dir['Methane_oxidation_methane_to_methanol_mmoBCDXYZ_amoABC'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (4707, 1369, 5027, 1689)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (4756, 1447, 4996, 1687)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Methane_oxidation_methanol_to_formaldehyde_mxaFI_xoxF.png")
        position = ()
        if carbon_cycle_dir['Methane_oxidation_methanol_to_formaldehyde_mxaFI_xoxF'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (2883, 1272, 3363, 1752)
        elif carbon_cycle_dir['Methane_oxidation_methanol_to_formaldehyde_mxaFI_xoxF'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (2947, 1343, 3347, 1743)
        elif carbon_cycle_dir['Methane_oxidation_methanol_to_formaldehyde_mxaFI_xoxF'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2991, 1413, 3311, 1733)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3032, 1488, 3272, 1728)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Fermentation_to_acetate_pyruvate_to_acetate_poxB_poxL_acyP.png")
        position = ()
        if carbon_cycle_dir['Fermentation_to_acetate_pyruvate_to_acetate_poxB_poxL_acyP'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (3147, 2681, 3627, 3161)
        elif carbon_cycle_dir['Fermentation_to_acetate_pyruvate_to_acetate_poxB_poxL_acyP'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (3205, 2753, 3605, 3153)
        elif carbon_cycle_dir['Fermentation_to_acetate_pyruvate_to_acetate_poxB_poxL_acyP'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3246, 2830, 3566, 3150)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3192, 2898, 3432, 3138)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Fermentation_to_acetate_acetyl-CoA_to_acetate_ach1_eutD_pta_acyP.png")
        position = ()
        if carbon_cycle_dir['Fermentation_to_acetate_acetyl-CoA_to_acetate_ach1_eutD_pta_acyP'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (3585, 3787, 4065, 4267)
        elif carbon_cycle_dir['Fermentation_to_acetate_acetyl-CoA_to_acetate_ach1_eutD_pta_acyP'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (3600, 3797, 4000, 4197)
        elif carbon_cycle_dir['Fermentation_to_acetate_acetyl-CoA_to_acetate_ach1_eutD_pta_acyP'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (3614, 3827, 3934, 4147)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (3634, 3846, 3874, 4086)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Fermentation_to_acetate_lactate_to_acetate_EC:1.13.12.4.png")
        position = ()
        if carbon_cycle_dir['Fermentation_to_acetate_lactate_to_acetate_EC:1.13.12.4'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (4684, 2513, 5164, 2993)
        elif carbon_cycle_dir['Fermentation_to_acetate_lactate_to_acetate_EC:1.13.12.4'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (4745, 2533, 5145, 2933)
        elif carbon_cycle_dir['Fermentation_to_acetate_lactate_to_acetate_EC:1.13.12.4'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (4846, 2577, 5166, 2897)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (4920, 2603, 5160, 2843)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Fermentation_to_lactate_pyruvate_to_lactate_LDH.png")
        position = ()
        if carbon_cycle_dir['Fermentation_to_lactate_pyruvate_to_lactate_LDH'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1533, 2488, 2013, 2968)
        elif carbon_cycle_dir['Fermentation_to_lactate_pyruvate_to_lactate_LDH'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1551, 2510, 1951, 2910)
        elif carbon_cycle_dir['Fermentation_to_lactate_pyruvate_to_lactate_LDH'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (1574, 2518, 1894, 2838)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (1604, 2529, 1844, 2769)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Fermentation_to_formate_pyruvate_to_formate_pf1D.png")
        position = ()
        if carbon_cycle_dir['Fermentation_to_formate_pyruvate_to_formate_pf1D'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1518, 3305, 1998, 3785)
        elif carbon_cycle_dir['Fermentation_to_formate_pyruvate_to_formate_pf1D'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1518, 3361, 1918, 3761)
        elif carbon_cycle_dir['Fermentation_to_formate_pyruvate_to_formate_pf1D'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (1522, 3387, 1842, 3707)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (1533, 3465, 1773, 3705)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open("Figure_tmp/Fermentation_to_formate_to_CO2_H2_fdh.png")
        position = ()
        if carbon_cycle_dir['Fermentation_to_formate_to_CO2_H2_fdh'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (1898, 3570, 2378, 4050)
        elif carbon_cycle_dir['Fermentation_to_formate_to_CO2_H2_fdh'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (1951, 3633, 2351, 4033)
        elif carbon_cycle_dir['Fermentation_to_formate_to_CO2_H2_fdh'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (2000, 3711, 2320, 4031)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (2018, 3770, 2258, 4010)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Fermentation_to_ethanol_acetate_to_acetylaldehyde_ald.png")
        position = ()
        if carbon_cycle_dir['Fermentation_to_ethanol_acetate_to_acetylaldehyde_ald'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (5613, 3660, 6093, 4140)
        elif carbon_cycle_dir['Fermentation_to_ethanol_acetate_to_acetylaldehyde_ald'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (5626, 3639, 6026, 4039)
        elif carbon_cycle_dir['Fermentation_to_ethanol_acetate_to_acetylaldehyde_ald'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (5626, 3700, 5946, 4020)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (5638, 3770, 5878, 4010)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Fermentation_to_ethanol_acetyl-CoA_to_acetylaldehyde_reversible.png")
        position = ()
        if carbon_cycle_dir['Fermentation_to_ethanol_acetyl-CoA_to_acetylaldehyde_reversible'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (4440, 4915, 4920, 5395)
        elif carbon_cycle_dir['Fermentation_to_ethanol_acetyl-CoA_to_acetylaldehyde_reversible'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (4563, 4989, 4963, 5389)
        elif carbon_cycle_dir['Fermentation_to_ethanol_acetyl-CoA_to_acetylaldehyde_reversible'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (4616, 5058, 4936, 5378)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (4637, 5132, 4877, 5372)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    carbon_cycle_image = Image.open("Figure_tmp/carbon_cycle.png")
    try:
        pathway_fig = Image.open(
            "Figure_tmp/Fermentation_to_ethanol_acetylaldehyde_to_ethanol_adh_mdh.png")
        position = ()
        if carbon_cycle_dir['Fermentation_to_ethanol_acetylaldehyde_to_ethanol_adh_mdh'] >= three_quarter_carbon:
            pathway_fig = pathway_fig.resize((480, 480))
            position = (4678, 4250, 5158, 4730)
        elif carbon_cycle_dir['Fermentation_to_ethanol_acetylaldehyde_to_ethanol_adh_mdh'] >= two_quarter_carbon:
            pathway_fig = pathway_fig.resize((400, 400))
            position = (4710, 4316, 5110, 4716)
        elif carbon_cycle_dir['Fermentation_to_ethanol_acetylaldehyde_to_ethanol_adh_mdh'] >= one_quarter_carbon:
            pathway_fig = pathway_fig.resize((320, 320))
            position = (4756, 4390, 5076, 4710)
        else:
            pathway_fig = pathway_fig.resize((240, 240))
            position = (4793, 4443, 5033, 4683)
        carbon_cycle_image_copy = carbon_cycle_image.copy()
        carbon_cycle_image_copy.paste(pathway_fig, position, pathway_fig)
        carbon_cycle_image_copy.save("Figure_tmp/carbon_cycle.png", 'png')
    except:
        pass
    
    # draw figure legend of samples
    color1 = (0, 0, 255)
    color2 = (0,127,255)
    color3 = (0,212,255)
    color4 = (0,255,255)
    color5 = (0,255,191)
    color6 = (0,255,106)
    color7 = (255,234,0)
    color8 = (255,149,0)
    color9 = (255,64,0)
    color10 = (255,0,170)
    color11 = (170,0,255)
    color12 = (185,185,237)
    color13 = (185,233,231)
    color14 = (224,237,185)
    color15 = (237,215,185)
    color16 = (237,185,220)
    color17 = (35,35,143)
    color18 = (35,106,143)
    color19 = (35,143,79)
    color20 = (143,98,35)
    colors = [color1, color2, color3, color4, color5,
              color6, color7, color8, color9, color10,
              color11, color12, color13, color14, color15,
              color16, color17, color18, color19, color20]
    samples = head.split('\t')
    Count_samples = len(samples)
    for i in range(1, Count_samples):
        carbon_cycle_image_cv2 = cv2.imread("Figure_tmp/carbon_cycle.png")
        color = colors[i-1]
        #print(str(color))
        (xmin, ymin) = (6325, 641+120*(int(i)-1))
        # (1901,66),(1941,106)
        (xmax, ymax) = (6405, 721+120*(int(i)-1))
        #(1901, 126) (1941, 166)
        cv2.rectangle(carbon_cycle_image_cv2, (xmin, ymin),
                      (xmax, ymax), color, -1)
    
        # draw sample_text of figure legend
        sample = samples[i]
        org = (6415, 701+120*(int(i)-1))
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 2
        color_font = (0, 0, 0)
        thickness = 4
        cv2.putText(carbon_cycle_image_cv2, sample, org,
                    font, fontScale, color_font, thickness)
        cv2.imwrite('Figure_tmp/carbon_cycle.png', carbon_cycle_image_cv2)
    
    # draw figure legend of pie
    carbon_cycle_image_cv2 = cv2.imread("Figure_tmp/carbon_cycle.png")
    color_cycle = (109, 118, 248)
    cv2.circle(carbon_cycle_image_cv2, (6325, 5188), 184, color_cycle, -1)
    cv2.circle(carbon_cycle_image_cv2, (6325, 4830), 154, color_cycle, -1)
    cv2.circle(carbon_cycle_image_cv2, (6325, 4534), 122, color_cycle, -1)
    cv2.circle(carbon_cycle_image_cv2, (6325, 4300), 92, color_cycle, -1)
    
    top_abun_carbon_sci = '%.2e' % (top_abun_carbon)
    three_quarter_carbon_sci = '%.2e' % (three_quarter_carbon)
    two_quarter_carbon_sci = '%.2e' % (two_quarter_carbon)
    one_quarter_carbon_sci = '%.2e' % (one_quarter_carbon)
    text1 = '>= ' + str(three_quarter_carbon_sci) + '; ' + \
        '<' + str(top_abun_carbon_sci)
    text2 = '>= ' + str(two_quarter_carbon_sci) + '; ' + \
        '<' + str(three_quarter_carbon_sci)
    text3 = '>= ' + str(one_quarter_carbon_sci) + '; ' + \
        '<' + str(two_quarter_carbon_sci)
    text4 = '> ' + str(0) + '; ' + '<' + str(one_quarter_carbon_sci)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color_font = (0, 0, 0)
    thickness = 4
    cv2.putText(carbon_cycle_image_cv2, text1, (6519, 5188),
                font, fontScale, color_font, thickness)
    cv2.putText(carbon_cycle_image_cv2, text2, (6489, 4830),
                font, fontScale, color_font, thickness)
    cv2.putText(carbon_cycle_image_cv2, text3, (6457, 4554),
                font, fontScale, color_font, thickness)
    cv2.putText(carbon_cycle_image_cv2, text4, (6427, 4320),
                font, fontScale, color_font, thickness)
    
    legend_line1 = "Figure. Relative abundances of the pathways involved in the carbon cycle. The pie chart indicates"
    legend_line2 = "the relative abundance of each pathway in each metagenomic sample . The size of pie charts represent"
    legend_line3 = "the total relative abundance of each pathway. CBB, Calvin-Benson-Bassham cycle; rTCA, reductive citric"
    legend_line4 = "acid cycle; WL, Wood-Ljungdahl pathway; 3HB, 3-hydroxypropionate bicycle; DHC, dicarboxylate-hydroxybutyrate cycle."
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 2
    color_font = (0, 0, 0)
    thickness = 4
    cv2.putText(carbon_cycle_image_cv2, legend_line1, (912, 5704),
                font, fontScale, color_font, thickness)
    cv2.putText(carbon_cycle_image_cv2, legend_line2, (912, 5824),
                font, fontScale, color_font, thickness)
    cv2.putText(carbon_cycle_image_cv2, legend_line3, (912, 5944),
                font, fontScale, color_font, thickness)
    cv2.putText(carbon_cycle_image_cv2, legend_line4, (912, 6064),
                font, fontScale, color_font, thickness)
    
    cv2.imwrite('Figure_tmp/carbon_cycle.png', carbon_cycle_image_cv2)
    
    os.system('mv Figure_tmp/carbon_cycle.png ./carbon_cycle_sketch.png')
