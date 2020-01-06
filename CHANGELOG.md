# Changelog
All notable changes to Diting will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

- Allow users to provide sam files
- Add support for conda deployment
- Add `--continue` option for users
- Add DMSP synthesis/degradation pathways

## [0.5] - 2020-01-06

### Added
- added visualization of carbon, nitrogen and sulfur cycle.
- added support for downloading and initializing kofam_database automatically
- readded heatmap output
- A more helpful manual
- added a table of the relative abundance of k_number among samples output 

### fixed
- minor bugs

## [0.4] - 2019-11-04

### Changed
- reframed the code, splitting functions into several modules
- modified pathways calculation to object-oriented programming. Greatly simplified the code.

### fixed
- minor bugs

### Removed
- removed heatmap output temporarily

## [0.3] - 2019-10-21

### Added

- added the file "Pathway_formulas.txt" containing the formulas of pathways

### Changed

- revised the file "accessory-scripts/KEGG-decoder_meta.py"

### Removed

- KOALA_definition.txt

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

