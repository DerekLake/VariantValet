# VariantValet
 Binning Algorithm for Viral Variant Classification
README.md for VariantValet.py

VariantValet is a Python script designed to provide .txt files containing all SARS-CoV-2 amplicon sequencing read names for specific point mutations. It also produces variant-specific txt files containing all read names that contain all of the mutations specific to each variant supplied in the TSV file input.

However, VariantValet could putatively be used with any reference genome/organism as long as you can supply a TSV file containing new mutations and variants, a FASTA reference sequence, and a SAM file created with Minimap2 (use your FASTQ reads and your reference fasta to create the SAM file).

This could be very helpful when trying to track a pathogen or virus as it spreads and rapidly evolves. The script requires a SAM input in which Minimap2 was used. Txt files could be used to extract the FASTQ reads from initial FASTQ input used for SAM generation using get_seqs_fastq_gz.py

Requirements:
- Python 3.9.15 (Tested with 3.9.15 but could work with Python 3.x)
- Pysam
-*Minimap2 for SAM generation

Usage:

python VariantValet.py -r <reference.fasta> -i <input.sam> -t <mutations.tsv> -o <output_directory>

Arguments:
-r, --reference : Path to the reference genome (FASTA format).
-i, --input     : Path to the input SAM file.
-t, --tsv       : Path to the input TSV file with mutations.
-o, --output    : Path to the output directory.

Input TSV Format:
The input TSV file should contain a header line and rows with two columns: variant and mutation. The variant is a string identifier for the set of mutations, and the mutation is a single mutation in the format "REF_BASEPOSALT_BASE" (e.g., "A123T").

Example:

Variant  Mutation
A        A12345T
A        G67891A
B        T23456C
C        G78912A

Output:
The script will create two sets of text files in the output directory:
- mutation_*.txt: Files containing read names for each mutation (e.g., mutation_A123T.txt).
- variant_*.txt: Files containing read names for each variant (e.g., variant_A.txt).

