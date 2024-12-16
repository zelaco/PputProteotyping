import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import argparse

def generate_venn(file_path, output_file):
    species_df = pd.read_excel(file_path, sheet_name='Species')
    species_names = species_df.columns.tolist()

    if len(species_names) != 3:
        raise ValueError("This script supports exactly 3 species for Venn diagrams.")

    species_sets = {
        species: set(species_df[species].dropna())
        for species in species_names
    }

    plt.figure(figsize=(10, 6))
    venn = venn3(
        [species_sets[species] for species in species_names],
        set_labels=species_names
    )

    for text in venn.set_labels:
        if text:
            text.set_fontsize(16)
            text.set_style('italic')

    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Venn diagram saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Venn diagram for three species.")
    parser.add_argument("--file-path", required=True, help="Path to the Excel file containing species data.")
    parser.add_argument("--output-file", required=True, help="Path to save the Venn diagram.")
    args = parser.parse_args()

    generate_venn(args.file_path, args.output_file)
