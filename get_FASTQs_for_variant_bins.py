#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:21:34 2023
***Script should be executed on each variant txt file***
@author: Dlake
"""

from Bio import SeqIO
import argparse

# Function to test if a file can be opened
def test_file(filename):
    try:
        with open(filename):
            pass
    except IOError:
        raise IOError('File cannot be opened: ' + filename)

# Main function that reads input files, filters the sequences, and writes the output file
def main(in_fastq, headers, out_fastq, min_phred):  # Add min_phred argument here
    # Read the IDs file and store the IDs as a set
    with open(headers) as f:
        data_set = set(line.strip() for line in f)

    # Open the output FASTQ file for writing
    with open(out_fastq, "w") as output_handle:
        # Open and parse the input FASTQ file
        with open(in_fastq, "rt") as handle:
            for record in SeqIO.parse(handle, "fastq"):
                if record.id.split()[0] in data_set:
                    mean_phred_score = sum(record.letter_annotations["phred_quality"]) / len(record.letter_annotations["phred_quality"])
                    if mean_phred_score > min_phred:  # Use min_phred argument here; does not include reads with an AVERAGE PHRED lower than arg
                        SeqIO.write(record, output_handle, "fastq")

# Command-line argument parsing and script execution within main fucntion; calls test_file and main functions
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input_fastq", required=True, type=str)
    parser.add_argument("-d", "--headers", required=True, type=str)
    parser.add_argument("-o", "--output_fastq", required=True, type=str)
    parser.add_argument("-p", "--min_phred", required=True, type=int)  # Add min_phred argument (e.g. 30 = Q30 which is 99.9% accurate basecalling)

    args = parser.parse_args()

    test_file(args.input_fastq)
    test_file(args.headers)

    main(args.input_fastq, args.headers, args.output_fastq, args.min_phred)  # Add args.min_phred here
