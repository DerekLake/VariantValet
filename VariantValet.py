#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:21:08 2023

@author: Dlake
"""


import argparse
import csv
import re
import os
import sys
from collections import defaultdict
import pysam

def read_mutations_from_tsv(tsvfile):
    #Read mutation and variant data from a TSV file
    variants = defaultdict(list)
    all_mutations = set()
    with open(tsvfile, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)  # Skip the header
        for row in reader:
            variant, mutation = row[0], row[1]
            variants[variant].append(mutation)
            all_mutations.add(mutation)
    return all_mutations, variants

def write_read_names_to_txt(binned_reads, output_dir):
    #Write the read names for each mutation to a text file
    for mutation, read_names in binned_reads.items():
        with open(os.path.join(output_dir, f"mutation_{mutation}.txt"), "w") as outfile:
            for name in read_names:
                outfile.write(name + "\n")

def write_variant_reads_to_txt(variant_reads, output_dir):
    #Write the read names for each variant to a text file
    for variant, read_names in variant_reads.items():
        with open(os.path.join(output_dir, f"variant_{variant}.txt"), "w") as outfile:
            for name in read_names:
                outfile.write(name + "\n")

def bin_reads_per_mutation_and_variant(mutations, variants, samfile, ref_fasta):
    #Bin the reads per mutation and variant
    binned_reads = defaultdict(list)
    variant_reads = defaultdict(list)
    ref_seq = {}
   # Load reference sequence (or sequences, but position might be off)
    with pysam.FastaFile(ref_fasta) as ref_file:
        for ref_name in ref_file.references:
            ref_seq[ref_name] = ref_file.fetch(ref_name)

    # Iterate through the reads in the SAM file
    with pysam.AlignmentFile(samfile) as samfile:
        for read in samfile.fetch():
            ref_name = samfile.get_reference_name(read.reference_id)
            ref_aligned_seq = ref_seq[ref_name][read.reference_start:read.reference_end]
            read_aligned_seq = read.query_sequence

            read_mutations = []
            # Check for mutations in the read
            for mutation in mutations:
                # Extract the ref base, position, and alt base from supplied muts
                match = re.match(r'([ACTG])(\d+)([ACTG])', mutation)
                ref_base, pos, alt_base = match.groups()
                pos = int(pos) - 1

                try:
                    # If pos not in aligned region of read, skip this iter
                    if pos < read.reference_start or pos >= read.reference_end:
                        continue
                    # If ref base in aligned ref seq does not match expected ref base, skip this iter
                    if ref_aligned_seq[pos - read.reference_start] != ref_base:
                        continue
                    # If alt base in aligned read seq does not match expected alt base, skip this iter
                    if read_aligned_seq[read.get_reference_positions().index(pos)] != alt_base:
                        continue
                    # If any exception occurs, skip this iter (will likely change to only IndexError or ValueError soon)
                except: pass

                # If mut found, add read name to binned_reads dict and mut to read_mutations list
                binned_reads[mutation].append(read.query_name)
                read_mutations.append(mutation)
                
            #check for variants in the read
            for variant, variant_mutations in variants.items():
                # If the set of muts in read matches the set of muts for variant, add read name to variant_reads dict
                if set(read_mutations) == set(variant_mutations):
                    variant_reads[variant].append(read.query_name)

    return binned_reads, variant_reads

def main():
    #define CLI arg parser
    parser = argparse.ArgumentParser(description='Bin SARS-CoV-2 reads based on specific mutations.')
    parser.add_argument('-r', '--reference', required=True, help='Path to the reference genome (FASTA format).')
    parser.add_argument('-i', '--input', required=True, help='Path to the input SAM file.')
    parser.add_argument('-t', '--tsv', required=True, help='Path to the input TSV file with mutations.')
    parser.add_argument('-o', '--output', required=True, help='Path to the output directory.')
    #parse teh CLI args
    args = parser.parse_args()

    # Check if input files and output directory even exist/are supplied
    if not os.path.exists(args.reference):
        print("Error: Reference file not found.")
        sys.exit(1)
    if not os.path.exists(args.input):
        print("Error: Input SAM file not found.")
        sys.exit(1)
    if not os.path.exists(args.tsv):
        print("Error: Input TSV file not found.")
        sys.exit(1)

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    # Read muts from the input TSV file
    all_mutations, variants = read_mutations_from_tsv(args.tsv)

    # Bin reads per mutation and variant
    binned_reads, variant_reads = bin_reads_per_mutation_and_variant(all_mutations, variants, args.input, args.reference)

    # Write read names for each mut and variant to txt files
    write_read_names_to_txt(binned_reads, args.output)
    write_variant_reads_to_txt(variant_reads, args.output)

if __name__ == '__main__':
    main()
