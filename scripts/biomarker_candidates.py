import pandas as pd

# Load the Excel file with species data and merged annotations
species_file_path = 'Data/PutidaP.xlsx'
annotations_file_path = 'Data/merged_putida_annotations.xlsx'

# Load species sheet and annotations
species_df = pd.read_excel(species_file_path, sheet_name='Species')
annotations_df = pd.read_excel(annotations_file_path)

# Define species names
species_names = species_df.columns  # Each column in 'Species' corresponds to a species

# Calculate unique proteins for each species
unique_proteins = {}
for species in species_names:
    # Get proteins for the current species
    current_species_proteins = set(species_df[species].dropna())

    # Get proteins for all other species
    other_species_proteins = set(species_df.loc[:, species_df.columns != species].stack().dropna())

    # Unique proteins are those in the current species but not in others
    unique_proteins[species] = current_species_proteins - other_species_proteins

# Write the unique proteins for each species to an Excel file
with pd.ExcelWriter('biomarker_candidates_all.xlsx', engine='openpyxl') as writer:
    for species, proteins in unique_proteins.items():
        # Filter annotations to include only unique proteins for this species
        filtered_data = annotations_df[annotations_df['SeqName'].isin(proteins)]

        # Ensure all relevant columns are present and replace missing data with empty strings
        filtered_data = filtered_data.reindex(columns=['SeqName', 'GO', 'GO Names', 'KEGG KO', 'KEGG Pathway', 'Description'])
        filtered_data.fillna('', inplace=True)

        # Save the data to an Excel sheet named after the species
        filtered_data.to_excel(writer, sheet_name=species, index=False)

        # Debug print for progress
        print(f"Processed {species}: {len(filtered_data)} unique biomarker candidates")
