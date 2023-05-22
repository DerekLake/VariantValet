# VariantValet
Binning Algorithm for Viral Variant Classification

VariantValet Pipeline Overview

This repository contains a pipeline for processing and analyzing viral variant data from FASTQ files. The pipeline integrates various scripts and tools to filter sequences, bin amplicon reads by variant, and generate consensus sequences using a pretrained neural network model provided by Medaka. Pipeline was designed for SARS-CoV-2 S gene long-read Oxford Nanopore (R.10.4.1 Flow Cell) amplicons.

Overview of the Pipeline

Sequence Filtering - Filter_by_length.py: This script filters sequences from a FASTQ file based on their length. It outputs three new FASTQ files containing reads corresponding to certain lengths that are supplied by an argument. (ex: reads are filtered to 3 fastq files containing reads <4000bp, betweeen 4000-4200 bp, and over 4200 bp. It also supplies the read count within each fastq file.

Variant Binning - VariantValet.py: This Python script implements a binning algorithm to categorize viral variant-specific amplicons by haplotype from a wastewater sample containing multiple variants, using point mutations as a basis for differentiation.

Extracting FASTQs for Variant Bins - get_FASTQs_for_variant_bins.py: This script takes the output from VariantValet.py and retrieves the original FASTQ sequences corresponding to each variant bin, outputting them into separate FASTQ files.

Consensus Generation and Analysis - Medaka: After the variant bins have been identified and the corresponding sequences retrieved, the Oxford Nanopore Technologies (ONT) tool Medaka is used to generate a consensus sequence for each bin and analyze it using a pretrained neural network model. Medaka is a tool for creating consensus sequences and variant calling from nanopore sequencing data.

Getting Started

Each of the Python scripts in this pipeline uses the argparse module for command-line argument parsing. You can run any script with the -h or --help option to see a description of its expected inputs and outputs.

Before running the pipeline, make sure you have installed all necessary dependencies, including BioPython for the Python scripts and Medaka for consensus generation and analysis.

Running the Pipeline

To run the entire pipeline, you would typically execute each script in the order listed above, passing the output from one script as the input to the next. Initial input for VariantValet.py will require a SAM file and can be generated with Minimap2. Be sure to check the individual README files for each script for specific usage examples and additional details.

This repository is a work in progress, and we welcome feedback and contributions.

Contact

If you have any questions or run into any issues, please feel free to contact us at dpl65@nau.edu
