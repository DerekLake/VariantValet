# Viral Variant Pipeline Overview

This repository contains a pipeline for processing and analyzing viral variant data from FASTQ files. The pipeline integrates various scripts and tools to filter sequences, bin variants, and generate consensus sequences using a pretrained neural network model provided by Medaka.

## Overview of the Pipeline

1. **Sequence Filtering - `Filter_by_length.py`**: This script filters sequences from a FASTQ file based on their length. It outputs a new FASTQ file containing only the sequences that meet the specified length criteria.

2. **Variant Binning - `VariantValet.py`**: This Python script implements a binning algorithm to categorize viral variant-specific amplicons by haplotype from a wastewater sample containing multiple variants, using point mutations as a basis for differentiation.

3. **Extracting FASTQs for Variant Bins - `get_FASTQs_for_variant_bins.py`**: This script takes the output from `VariantValet.py` and retrieves the original FASTQ sequences corresponding to each variant bin, outputting them into separate FASTQ files.

4. **Consensus Generation and Analysis - Medaka**: After the variant bins have been identified and the corresponding sequences retrieved, the Oxford Nanopore Technologies (ONT) tool Medaka is used to generate a consensus sequence for each bin and analyze it using a pretrained neural network model. Medaka is a tool for creating consensus sequences and variant calling from nanopore sequencing data. 

## Getting Started

Each of the Python scripts in this pipeline uses the argparse module for command-line argument parsing. You can run any script with the `-h` or `--help` option to see a description of its expected inputs and outputs.

Before running the pipeline, make sure you have installed all necessary dependencies, including BioPython for the Python scripts and Medaka for consensus generation and analysis.

## Running the Pipeline

To run the entire pipeline, you would typically execute each script in the order listed above, passing the output from one script as the input to the next. Be sure to check the individual README files for each script for specific usage examples and additional details.

This repository is a work in progress, and we welcome feedback and contributions.

## Contact

If you have any questions or run into any issues, please feel free to contact us.


