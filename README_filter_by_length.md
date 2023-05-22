# Filter Reads by Length

This is a Python script to filter sequence reads from a FASTQ file into three categories based on their length:

- Short sequences
- Medium sequences
- Long sequences

The thresholds for the sequence lengths are customizable and can be passed as command-line arguments.

## Prerequisites

To run this script, you need Python 3 and BioPython installed. You can install BioPython with pip:

pip3 install biopython

## Usage

You can run this script from the command line with the following syntax:


python3 filter_reads_by_length.py -i INPUT -s SHORT -l LONG


Replace:
-"INPUT" with the name of your FASTQ file
-"SHORT" with the maximum length for short sequences
-"LONG" with the minimum length for long sequences.

Example:

python3 filter_reads_by_length.py -i input.fastq -s 4000 -l 4200


This will classify sequences in input.fastq into three categories:

- Short sequences (length < 4000)
- Medium sequences (4000 ≤ length ≤ 4200)
- Long sequences (length > 4200)

The script will output three new FASTQ files for each category and print the number of reads in each category.

## Error Handling

The script includes basic error handling. It will stop and print an error message if:

- The input file does not exist.
- There's a problem parsing the input file.
- The short sequence threshold is greater than or equal to the long sequence threshold.

## Contact

If you encounter any problems or have any suggestions, please open an issue or submit a pull request.

