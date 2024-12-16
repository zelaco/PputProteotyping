import pandas as pd
import argparse

def identify_biomarkers(species_file, annotations_file, output_file):
    species_df = pd.read_excel(species_file, sheet_name='Species')
    annotations_df = pd.read_excel(annotations_file)
    species_names = species_df.columns

    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for species in species_names:
            current_proteins = set(species_df[species].dropna())
            other_proteins = set(species_df.loc[:, species_df.columns != species].stack().dropna())
            unique_proteins = current_proteins - other_proteins

            filtered_data = annotations_df[annotations_df['SeqName'].isin(unique_proteins)]
            filtered_data = filtered_data.reindex(columns=['SeqName', 'GO', 'GO Names', 'KEGG KO', 'KEGG Pathway', 'Description'])
            filtered_data.fillna('', inplace=True)

            filtered_data.to_excel(writer, sheet_name=species, index=False)
            print(f"Processed {species}: {len(filtered_data)} unique biomarker candidates")

    print(f"Biomarker candidates saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Identify biomarker candidates for each species.")
    parser.add_argument("--species-file", required=True, help="Path to the species Excel file.")
    parser.add_argument("--annotations-file", required=True, help="Path to the merged annotations file.")
    parser.add_argument("--output-file", required=True, help="Path to save the biomarker candidates.")
    args = parser.parse_args()

    identify_biomarkers(args.species_file, args.annotations_file, args.output_file)
