import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

def generate_heatmap(input_file, output_file, accession_column, heatmap_columns):
    data = pd.read_excel(input_file)
    heatmap_data = data[[accession_column] + heatmap_columns].set_index(accession_column)
    heatmap_data = heatmap_data[(heatmap_data != 0).all(axis=1)].dropna()

    sns.clustermap(
        heatmap_data,
        cmap='magma_r',
        metric='euclidean',
        method='average',
        figsize=(10, 12),
        yticklabels=False,
        row_cluster=False,
        dendrogram_ratio=(.1, .1),
        cbar_pos=(0, .2, .03, .4)
    )

    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Heatmap saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an expression heatmap.")
    parser.add_argument("--input-file", required=True, help="Path to the input Excel file.")
    parser.add_argument("--output-file", required=True, help="Path to save the heatmap.")
    parser.add_argument("--accession-column", default="Accession", help="Name of the accession column.")
    parser.add_argument("--heatmap-columns", nargs='+', required=True, help="List of columns to include in the heatmap.")
 
