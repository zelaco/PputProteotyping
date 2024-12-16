import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def enrich_go_terms(species_file, annotations_file, output_dir):
    species_df = pd.read_excel(species_file, sheet_name='Species')
    annotations_df = pd.read_excel(annotations_file)

    for species in species_df.columns:
        species_proteins = set(species_df[species].dropna())
        species_annotations = annotations_df[annotations_df['SeqName'].isin(species_proteins)]

        go_data = []
        for _, row in species_annotations.iterrows():
            if pd.notna(row['GO']):
                for go_term, go_name in zip(row['GO'].split(';'), row['GO Names'].split(';')):
                    category = go_term[0]
                    simplified_name = go_name.strip().split(':')[-1]
                    go_data.append((species, simplified_name, category))

        plot_data = pd.DataFrame(go_data, columns=['Species', 'GO Term', 'Type'])
        top_go_terms = (
            plot_data.groupby(['Species', 'GO Term', 'Type'])
            .size()
            .reset_index(name='Count')
            .sort_values(by=['Species', 'Type', 'Count'], ascending=False)
            .groupby(['Species', 'Type'])
            .head(10)
        )

        palette = {'C': '#a84832', 'P': '#439447', 'F': '#2a62c9'}
        plt.figure(figsize=(20, 18))
        sns.barplot(x='Count', y='GO Term', hue='Type', data=top_go_terms, palette=palette)
        plt.title(f"{species}", fontstyle='italic', fontsize=20)
        plt.xlabel('Nr. of Proteins')
        plt.ylabel('GO Term')
        plt.legend(title='Category')

        plt.tight_layout()
        plt.savefig(f"{output_dir}/GOTERMS_{species}.png", dpi=300)
        print(f"GO term plot saved for {species}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform GO term enrichment analysis and generate visualizations.")
    parser.add_argument("--species-file", required=True, help="Path to the species Excel file.")
    parser.add_argument("--annotations-file", required=True, help="Path to the merged annotations file.")
    parser.add_argument("--output-dir", required=True, help="Directory to save the GO term plots.")
    args = parser.parse_args()

    enrich_go_terms(args.species_file, args.annotations_file, args.output_dir)
