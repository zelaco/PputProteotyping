import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Load the Excel file with accession numbers
file_path = 'Data/PutidaP.xlsx' 

# Read the 'Species' sheet into a DataFrame
species_df = pd.read_excel(file_path, sheet_name='Species')

# Get the species names from the columns
species_names = species_df.columns.tolist()

# Build sets of proteins for each species
species_sets = {}
for species in species_names:
    # Get the list of proteins for this species, dropping any NaNs
    proteins = species_df[species].dropna().tolist()
    species_sets[species] = set(proteins)

# Assign species names to variables for clarity
species1, species2, species3 = species_names

# Plot the Venn diagram
plt.figure(figsize=(10, 6))
venn = venn3(
    [species_sets[species1], species_sets[species2], species_sets[species3]],
    set_labels=(species1, species2, species3)
)

# Customize the Venn diagram labels
for text in venn.set_labels:
    if text:
        text.set_fontsize(16)
        text.set_style('italic')

# Save and display the Venn diagram
plt.savefig('Outputs/VennDiagram.png', dpi=300, bbox_inches='tight')