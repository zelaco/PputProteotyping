import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set global font size
plt.rcParams.update({'font.size': 20})

# Load annotations
annotations_file_path = 'Data/merged_putida_annotations.xlsx'
annotations_df = pd.read_excel(annotations_file_path)

# Function to count and rank GO terms by category
def count_go_terms(df, species_name):
    go_data = []
    for _, row in df.iterrows():
        if pd.notna(row['GO']):
            go_terms = str(row['GO']).split(';')
            go_names = str(row['GO Names']).split(';')
            for go_term, go_name in zip(go_terms, go_names):
                category = go_term[0]  # First letter indicates category (C, P, F)
                simplified_name = go_name.strip().split(':')[-1]  # Simplify GO name
                go_data.append((species_name, simplified_name, category))
    return pd.DataFrame(go_data, columns=['Species', 'GO Term', 'Type'])

# Prepare data for each species
species_file_path = 'Data/PutidaP.xlsx'
species_df = pd.read_excel(species_file_path, sheet_name='Species')

# Create a combined DataFrame for all species
plot_data = pd.DataFrame()
for species in species_df.columns:
    species_proteins = set(species_df[species].dropna())
    species_annotations = annotations_df[annotations_df['SeqName'].isin(species_proteins)]
    species_go_data = count_go_terms(species_annotations, species)
    plot_data = pd.concat([plot_data, species_go_data])

# Filter out invalid or missing 'Type' values
plot_data = plot_data[plot_data['Type'].isin(['C', 'P', 'F'])]

# Calculate top 10 GO terms for each species and type
top_go_terms = (
    plot_data.groupby(['Species', 'GO Term', 'Type'])
    .size()
    .reset_index(name='Count')
    .sort_values(by=['Species', 'Type', 'Count'], ascending=False)
    .groupby(['Species', 'Type'])
    .head(10)
)

# Define color palette for full category names
palette = {'C': '#a84832', 'P': '#439447', 'F': '#2a62c9'}

# Full names for the legend
legend_labels = {
    'C': 'Cellular Component',
    'P': 'Biological Process',
    'F': 'Molecular Function'
}

# Plot top GO terms for each species
for species in species_df.columns:
    species_data = top_go_terms[top_go_terms['Species'] == species]
    
    # Ensure only valid data is plotted
    species_data = species_data[species_data['Type'].isin(['C', 'P', 'F'])]
    
    plt.figure(figsize=(20, 18))
    barplot = sns.barplot(
        x='Count',
        y='GO Term',
        hue='Type',
        data=species_data,
        palette=palette
    )
    plt.title(f"{species}", fontstyle='italic', fontsize=20)
    plt.xlabel('Nr. of Proteins', fontsize=20)
    plt.ylabel('GO Term', fontsize=20)

    # Adjust the legend with full names
    handles, labels = barplot.get_legend_handles_labels()
    full_labels = [legend_labels[label] for label in labels]
    plt.legend(handles, full_labels, title='Category', loc='best', fontsize=20)

    plt.tight_layout()
    plt.savefig(f'Outputs/GOTERMS_{species}.png', dpi=300)

