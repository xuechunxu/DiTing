KEGG-Decoder_meta
================================================================
### Description ###
Designed to parse through a KEGG-Koala outputs (including blastKOALA, ghostKOALA, KOFAMSCAN) to determine the relative abundance of various metabolic pathways in metagenomes.

* **Notably, our `KEGG-decoder_meta.py` was rewrote according to Graham's [KEGG-Decoder](https://github.com/bjtully/BioData/tree/master/KEGGDecoder). The ` KOALA_definitons.txt` was provided by Graham.** 
* This module was constructed using manually curated "canonical" pathways described as part of KEGG Pathway Maps. For information regarding which KOs are used to predict a metabolic pathway see the KOALA_definitions.txt. 


### Dependencies ###

* [Pandas](http://pandas.pydata.org/pandas-docs/stable/install.html)

* [matplotlib](http://matplotlib.org/users/installing.html)


## Procedure ##
* Start with metagenome protein FASTA file (INPUT_PROTEIN.fasta).
* Process protein sequences through KEGG-KOALA ([GhostKoala](https://www.kegg.jp/ghostkoala/), [BlastKoala](https://www.kegg.jp/blastkoala/), or [KOFAMSCAN](https://www.genome.jp/tools/kofamkoala/)) and download the tab-delimited KO assignment text file (KOALA_OUTPUT.txt)
* The Input (Input.tab) of KEGG-decoder_meta.py is `The KOALA output` text file add the relative abundance of each gene (or KO number):
```
F0_2016 K00001  0.0007370232000 
F0_2016 K00002  0.0000017390000 
F0_2016 K00003  0.0005440555000 
F0_2016 K00004  0.0000183414000
F0_2017 K00008  0.0001107390000
F0_2017 K00006  0.0000000000000
F0_2017 K00017  0.0000050780000
F0_2017 K00008  0.0000781000000
F20_2017 K00036  0.000003594000
F20_2017 K00010  0.000150967400

```

* Run KEGG-decoder_meta
```
python KEGG-decoder_meta.py <Input.tab> <Output.tab>
```
