from Bio import SeqIO
import os
import csv
import numpy as np

def calculate_genome_metrics(fasta_file):
    contig_lengths = [len(record.seq) for record in SeqIO.parse(fasta_file, "fasta")]
    total_length = sum(contig_lengths)
    gc_content = sum(record.seq.count('G') + record.seq.count('C') for record in SeqIO.parse(fasta_file, "fasta")) / total_length * 100 if total_length > 0 else 0

    # Sort contig lengths in descending order and calculate cumulative lengths
    contig_lengths.sort(reverse=True)
    cumulative_lengths = np.cumsum(contig_lengths)
    half_genome_size = total_length / 2
    n50 = next(length for length, cum_len in zip(contig_lengths, cumulative_lengths) if cum_len >= half_genome_size)

    return {
        "Genome Size": total_length,
        "GC Content": gc_content,
        "Number of Contigs": len(contig_lengths),
        "N50": n50,
        "Longest Contig": contig_lengths[0] if contig_lengths else 0,
        "Shortest Contig": contig_lengths[-1] if contig_lengths else 0,
        "Average Contig Length": total_length / len(contig_lengths) if contig_lengths else 0
    }

def process_fasta_files_in_directory(directory):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith((".fasta", ".fa")):
            filepath = os.path.join(directory, filename)
            metrics = calculate_genome_metrics(filepath)
            isolate_name = os.path.splitext(filename)[0]
            results.append({"Isolate Name": isolate_name, **metrics})
    return results

def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ["Isolate Name", "Genome Size", "GC Content", "Number of Contigs", "N50", "Longest Contig", "Shortest Contig", "Average Contig Length"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

# Specify the directory containing the FASTA files and the output CSV file
directory = "Data/PutidaGenomes"
output_file = "Outputs/Pputida_genome_stats.csv"

results = process_fasta_files_in_directory(directory)
save_results_to_csv(results, output_file)

print(f"Results saved to {output_file}")
