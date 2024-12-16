import pandas as pd
from Bio import SeqIO
import argparse

def retrieve_sequences(accession_file, proteome_file, output_file):
    # Read the Excel file and get accession numbers
    df = pd.read_excel(accession_file)
    accession_numbers = df.iloc[:, 3].tolist()

    # Extract sequences from the .faa file
    seq_dict = SeqIO.to_dict(SeqIO.parse(proteome_file, "fasta"))
    output_sequences = [seq_dict[acc] for acc in accession_numbers if acc in seq_dict]

    # Save extracted sequences
    with open(output_file, 'w') as output_handle:
        SeqIO.write(output_sequences, output_handle, "fasta")
    print(f"Sequences saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve sequences based on accession numbers.")
    parser.add_argument("--accession-file", required=True, help="Path to the Excel file with accession numbers.")
    parser.add_argument("--proteome-file", required=True, help="Path to the .faa proteome file.")
    parser.add_argument("--output-file", required=True, help="Path to save the retrieved sequences.")
    args = parser.parse_args()

    retrieve_sequences(args.accession_file, args.proteome_file, args.output_file)
