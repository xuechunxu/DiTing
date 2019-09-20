DiTing
================================================================
### Name ###
**DiTing** is a chinese mythical creature who knows everything when he puts ears on the earth's surface. Parallelly, this software could recognise biogeochemical cycle on Earth.  
**谛听(DiTing)** 若伏在地下，一霎时，便可将四大部洲山川社稷、洞天福地之间，
蠃虫、鳞虫、毛虫、羽虫、昆虫，天仙、地仙、神仙、人仙、鬼仙，顾鉴善恶，察听贤愚。

### Introduction ###
DiTing v0.1
This software was designed to determine the relative abundance of metabolic and biogeochemical
functional pathways in a set of given metagenomic reads simultaneously. The output is just a folder
which containing  a group of paired-end clean reads. These reads will be assemblied, KEGG annotated,
and parsed for producing a table of relative abundance of elemental/biogeochemical cycling pathways (e.g. Nitrogen, Carbon, Sulfur) in each sample.
* **Notably, our `Accessory_scripts/KEGG-decoder_meta.py` was rewrote according to Graham's [KEGG-Decoder](https://github.com/bjtully/BioData/tree/master/KEGGDecoder). The ` KOALA_definitons.txt` was provided by Graham.** 

### Procedure ###
![image](https://github.com/xuechunxu/DiTing/blob/master/Flow_chart.png)

### Copyright ###
Xue Chunxu, xuechunxu@outlook.com  
Heyu Lin, heyu.lin@student.unimelb.edu.au  
Xiao-Hua Zhang, xhzhang@ouc.edu.cn  
Lab of Microbial Oceanography  
College of Marine Life Sciences, Ocean University of China, Qingdao 266003, China  

### Dependencies ###
* [Megahit](https://github.com/voutcn/megahit)
* [Prokka](https://github.com/tseemann/prokka)
* [bwa](https://github.com/lh3/bwa)
* [BBMap](https://github.com/BioInfoTools/BBMap)(Pileup is needed)
* [HMMER](http://hmmer.org/)

* [python3](https://www.python.org/downloads/)
    Module:  
    * [Pandas](http://pandas.pydata.org/pandas-docs/stable/install.html)
    * [matplotlib](http://matplotlib.org/users/installing.html)

* [KofamKOALA hmm database](ftp://ftp.genome.jp/pub/db/kofam/)
    * [ko_list.gz](ftp://ftp.genome.jp/pub/db/kofam/ko_list.gz)
    * [profiles.tar.gz](ftp://ftp.genome.jp/pub/db/kofam/profiles.tar.gz)

### Installation ###
1. Download this script  
`git clone https://github.com/xuechunxu/DiTing.git`  
or go to where you want the program to be and clone the github repository or click the green buttom "download ZIP" folder, and unzip.  
2. DiTing requires the `KofamKOALA hmm database`. [KofamKOALA website](https://www.genome.jp/tools/kofamkoala/). This database should be kept in the same directory with the `DiTing_v0.1.py` scripts. Go to the folder of this software:  
`mkdir kofam_database`  
`cd kofam_database`  
`wget -c ftp://ftp.genome.jp/pub/db/kofam/ko_list.gz`  
`wget -c ftp://ftp.genome.jp/pub/db/kofam/profiles.tar.gz`  
`gzip -d ko_list.gz`  
`tar xzf profiles.tar.gz`  
3. DiTing requires the following programs to be added to your system path:  
* [Megahit](https://github.com/voutcn/megahit)
* [Prokka](https://github.com/tseemann/prokka)
* [bwa](https://github.com/lh3/bwa)
* [BBMap](https://github.com/BioInfoTools/BBMap)(Pileup is needed)
* [HMMER](http://hmmer.org/)

### Running ###
1. One step running  
`python DiTing_v0.1.py -r <Clean_reads_Dir>`  
* The input is the `<Clean_reads_Dir>` folder that containing a group of paired-end metagenomic clean reads, looks like:  
`sample_one_1.fastq`  
`sample_one_2.fastq`  
`sample_two_1.fastq`  
`sample_two_2.fastq`  
`sample_three_1.fastq`  
`sample_three_2.fastq`  
The paired-end metagenomic clean reads should be ended with `.fastq`  
2. output  
The final result is the `Pathways_relative_abundance_each_sample.tab` with the relative abundance of pathways in each sample. This table is in the folder `Final_result` directory.  

### Version ###  
DiTing_v0.1 -- Sep 19, 2019 --  
The Birthday!  
