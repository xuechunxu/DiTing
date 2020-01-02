<img src="./DiTing_logo.jpg" width="250" height="250">

DiTing  
================================  
### Etymon
**DiTing** is a chinese mythical creature who knows everything when he puts ears on the earth's surface. Parallelly, this software could recognise biogeochemical cycle on Earth when just put metagenomic Clean Reads as input.  

### Introduction
#### DiTing
This software was designed to determine the relative abundance of metabolic and biogeochemical
functional pathways in a set of given metagenomic reads simultaneously. The input is just a folder
which containing a group of paired-end clean reads. These reads will be assemblied, KEGG annotated,
and parsed for producing a table of relative abundance of elemental/biogeochemical cycling pathways (e.g. Nitrogen, Carbon, Sulfur) in each sample. According to the relative abundances, sketch maps and heatmaps will be produced for comparing biogeochemical functions visually.


### Procedure
![image](./Flow_chart.png)

### Copyright
Xue Chunxu, xuechunxu@outlook.com  
Heyu Lin, heyu.lin@student.unimelb.edu.au  
Xiaoyu Zhu, xiaoyuzhu321@126.com  
Xiao-Hua Zhang, xhzhang@ouc.edu.cn   
Lab of Microbial Oceanography  
College of Marine Life Sciences, Ocean University of China, Qingdao 266003, China  

### Dependencies
* [Megahit](https://github.com/voutcn/megahit)
* [Prodigal](https://github.com/hyattpd/Prodigal)
* [bwa](https://github.com/lh3/bwa)
* [BBMap](https://github.com/BioInfoTools/BBMap)(Pileup is needed)
* [HMMER](http://hmmer.org/)
* [python3](https://www.python.org/downloads/)
    Module:  
    * [Pandas](http://pandas.pydata.org/pandas-docs/stable/install.html)
    * [matplotlib](http://matplotlib.org/users/installing.html)
    * [opencv](https://pypi.org/project/opencv-python/)
    * [Pillow](https://pypi.org/project/Pillow/)
    * [shutil](https://docs.python.org/3/library/shutil.html)
    * [seaborn](https://seaborn.pydata.org/index.html)

* KofamKOALA hmm database (ftp://ftp.genome.jp/pub/db/kofam/)
    * [ko_list.gz](ftp://ftp.genome.jp/pub/db/kofam/ko_list.gz)
    * [profiles.tar.gz](ftp://ftp.genome.jp/pub/db/kofam/profiles.tar.gz)

### Installation
#### 1. Download this script
`git clone https://github.com/xuechunxu/DiTing.git`  
or go to where you want the program to be and clone the github repository or click the green buttom "download ZIP" folder, and unzip.  
#### 2. DiTing requires the `KofamKOALA hmm database`. [KofamKOALA website](https://www.genome.jp/tools/kofamkoala/). This database will be downloaded and unzipped automatically when you run this software for the first time. 
Or you can download the database manually. This database should be kept in the same directory with the `dingting.py` scripts. Go to the folder of this software:
```bash
mkdir kofam_database
cd kofam_database
wget -c ftp://ftp.genome.jp/pub/db/kofam/ko_list.gz 
wget -c ftp://ftp.genome.jp/pub/db/kofam/profiles.tar.gz 
gzip -d ko_list.gz
tar zxvf profiles.tar.gz 
```
#### 3. DiTing requires the following programs to be added to your system path:
* [Megahit](https://github.com/voutcn/megahit)
* [Prodigal](https://github.com/hyattpd/Prodigal)
* [bwa](https://github.com/lh3/bwa)
* [BBMap](https://github.com/BioInfoTools/BBMap)(Pileup is needed)
* [HMMER](http://hmmer.org/)

### Running
#### 1. One step running
```bash
python diting.py -r <Clean_reads_Dir> -o <Output_Dir>
```
* The input is the `<Clean_reads_Dir>` folder that containing a group of paired-end metagenomic clean reads, looks like: 
```
sample_one_1.fastq
sample_one_2.fastq
sample_two_1.fastq
sample_two_2.fastq
sample_three_1.fastq
sample_three_2.fastq
```
The paired-end metagenomic clean reads should be ended with `.fq`, `.fq.gz`, `.fastq`, or `.fastq.gz` 
#### 2. Optional parameter
**2.1 -a metagenomic_assembly, --assembly metagenomic_assembly**  
folder containing metagenomic assemblies corresponding to provided reads should be provided, which should have the same base name as the reads. The reads will not be assemblied when you use `-a` or `--assembly` parameter.  
```bash
python diting.py -r <Clean_reads_Dir> -a <Metagenomic_assembly> -o <Output_Dir>
```
* The `<Metagenomic_assembly>` folder looks like: 
```
sample_one.fa
sample_two.fa
sample_three.fa
```
**2.2 -n threads, --threads threads**  
threads that will be used.  
```bash
python diting.py -r <Clean_reads_Dir> -a <Metagenomic_assembly> -o <Output_Dir> -n 20
```
**2.3 --noclean [no_cleaning]**  
The sam files would be retained if this flag was used.  
```bash
python diting.py -r <Clean_reads_Dir> -a <Metagenomic_assembly> -o <Output_Dir> -n --noclean
```
#### 3. Output
**The final result is the `pathways_relative_abundance.tab` with the relative abundance of pathways in each sample.**  
**A table `ko_abundance_among_samples.tab` with the relativa abundance of each `k_number` of KEGG annotation is produced in `KEGG_annotation/` folder.**  
**There are also three sketch maps about carbon, nitrogen and sulfur cycle named `carbon_cycle_sketch.png`, `nitrogen_cycle_sketch.png` and `sulfur_cycle_sketch.png`, respectively.**  
**There are also four heatmaps about carbon, nitrogen, sulfur cycle and other pathways named `carbon_cycle_heatmap.pdf`, `nitrogen_cycle_heatmap.pdf`, `sulfur_cycle_heatmap.pdf` and `other_cycle_heatmap.pdf`, respectively.**  
<img src="https://github.com/xuechunxu/DiTing/blob/master/example/diting.out/carbon_cycle.png" width="792" height="657.7">  
<img src="https://github.com/xuechunxu/DiTing/blob/master/example/diting.out/nitrogen_cycle.png" width="792" height="771.4">  
<img src="https://github.com/xuechunxu/DiTing/blob/master/example/diting.out/sulfur_cycle.png" width="792" height="726.9">  
