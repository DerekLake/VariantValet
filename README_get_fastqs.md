# FastQ Filter Script

This Python script filters a FastQ file based on header ID and minimum average PHRED quality score. It utilizes the BioPython library to parse and write FastQ files.

## Dependencies

- Python 3
- BioPython

## Usage

To use the script, you must provide the input FastQ file, a headers file, the output FastQ file, and a minimum PHRED score as arguments. The script is invoked from the command line as follows:

```bash
python fastq_filter.py -i input.fastq -d headers.txt -o output.fastq -p 30

Arguments
-i or --input_fastq: Path to the input FastQ file.
-d or --headers: Path to a text file containing header IDs to be retained.
-o or --output_fastq: Path to the output FastQ file.
-p or --min_phred: Minimum average PHRED score for a read to be written to the output FastQ file.
Input

The input FastQ file (-i or --input_fastq) is a standard FastQ file.

The headers file (-d or --headers) should be a text file, with one header ID per line. These are the IDs of the reads to be retained.

Output

The output (-o or --output_fastq) is a standard FastQ file, containing only the reads specified in the headers file and with a minimum average PHRED score as specified by -p or --min_phred.

Contact

For any issues or further questions, please contact the author at dpl65@nau.edu
