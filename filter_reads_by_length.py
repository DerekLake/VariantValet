#!/usr/bin/env python3

import argparse
from Bio import SeqIO

# Set up command line arguments
parser = argparse.ArgumentParser(description='Filter reads by length')
parser.add_argument('-i', '--input', type=str, required=True,
                    help='Input FASTQ file')
parser.add_argument('-s', '--short', type=int, default=4000,
                    help='Threshold for short sequences')
parser.add_argument('-l', '--long', type=int, default=4200,
                    help='Threshold for long sequences')
args = parser.parse_args()

# Check if the --long argument is greater than the --short argument
if args.long <= args.short:
    raise ValueError('The --long threshold must be greater than the --short threshold.')

# Initialize lists to store sequences
short_sequences = []
medium_sequences = []
long_sequences = []

# Try to parse the input file and classify sequences
try:
    for record in SeqIO.parse(args.input, "fastq"):
        if len(record.seq) < args.short:
            short_sequences.append(record)
        elif args.short <= len(record.seq) <= args.long:
            medium_sequences.append(record)
        elif len(record.seq) > args.long:
            long_sequences.append(record)
except FileNotFoundError:
    print(f"The file {args.input} does not exist.")
    exit(1)
except Exception as e:
    print(f"An error occurred while parsing the file: {e}")
    exit(1)

# Write sequences to output files and provide feedback
print("Writing sequences to output files...")
SeqIO.write(short_sequences, f"{args.input}_<{args.short}.fastq", "fastq")
SeqIO.write(medium_sequences, f"{args.input}_{args.short}to{args.long}.fastq", "fastq")
SeqIO.write(long_sequences, f"{args.input}_{args.long}<.fastq", "fastq")
print("Writing complete!")

# Print the number of reads in each bin
print(f"Number of reads with length under {args.short}: ", len(short_sequences))
print(f"Number of reads with length between {args.short} and {args.long}: ", len(medium_sequences))
print(f"Number of reads with length above {args.long}: ", len(long_sequences))

