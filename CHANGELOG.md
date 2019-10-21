# Changelog
All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

- Add support for downloading and initializing kofam_database automatically
- Add a function to check the availability of database before hmmsearch
- Move the functions in diting.py into other scripts and import them as modules
- Allow users to provide sam files
- Add support for conda deployment
- Add more comment of the code

## [0.3] - 2019-10-21

### Added

- add the file "Pathway_formulas.txt" containing the formulas of pathways

### Changed

- revise the file "accessory-scripts/KEGG-decoder_meta.py"

### Removed

- KOALA_definition.txt file

## [0.2] - 2019-10-03

### Added

- More options including `--outdir`, `--assembly`, `--threads`, and `--noclean` are available
- Allow the input reads ending with `.fq`, `.fq.gz`, `.fastq`, or `.fastq.gz`
- Multiprocessing for hmmsearch step (speed up the program significantly)

### Changed

- Rearrange the directories for various outputs
- Run hmmsearch in real muiltiprocessing mode

### Fixed
- other minor bugs

### Removed

- tmp files

## [0.1] - 2019-09-19

- The first release

