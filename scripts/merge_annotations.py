import pandas as pd

# Load the filtered EggNOG and InterProScan files
filtered_eggnog_file = 'paer_eggnog.xlsx'
filtered_interpro_file = 'paer_interpro.xlsx'

eggnog_df = pd.read_excel(filtered_eggnog_file)
interpro_df = pd.read_excel(filtered_interpro_file)

# Merge the two tables using an outer join
merged_df = pd.merge(
    eggnog_df,
    interpro_df,
    left_on='Query ID',  # Column in EggNOG
    right_on='SeqName',  # Column in InterProScan
    how='outer',         # Include all rows from both tables
    suffixes=('_EggNOG', '_InterPro')
)

# Fill missing values with empty strings to handle missing data
merged_df.fillna('', inplace=True)

# Debug: Print merged DataFrame columns
print("Merged DataFrame columns:", merged_df.columns)

# Function to merge and deduplicate GO terms
def merge_go_terms(row):
    eggnog_go = str(row['GOs']).split(';') if row['GOs'] else []
    interpro_go = str(row['GO IDs']).split(';') if row['GO IDs'] else []
    combined_go = set(eggnog_go + interpro_go)  # Combine and deduplicate
    return '; '.join(sorted(filter(None, combined_go)))  # Join with semicolon, sort for consistency

# Function to merge and deduplicate GO names
def merge_go_names(row):
    eggnog_names = str(row['GO Names_EggNOG']).split(';') if row['GO Names_EggNOG'] else []
    interpro_names = str(row['GO Names_InterPro']).split(';') if row['GO Names_InterPro'] else []
    combined_names = set(eggnog_names + interpro_names)  # Combine and deduplicate
    return '; '.join(sorted(filter(None, combined_names)))  # Join with semicolon, sort for consistency

# Apply merging functions
merged_df['GO'] = merged_df.apply(merge_go_terms, axis=1)
merged_df['GO Names'] = merged_df.apply(merge_go_names, axis=1)

# Update #GO column to count the number of unique GO terms
merged_df['#GO'] = merged_df['GO'].apply(lambda x: len(x.split(';')) if x else 0)

# Remove unnecessary GO-related columns from individual sources
columns_to_drop = ['GOs', 'GO Names_EggNOG', 'GO IDs', 'GO Names_InterPro']
merged_df = merged_df.drop(columns=[col for col in columns_to_drop if col in merged_df.columns])

# Save the merged and cleaned DataFrame to an Excel file
merged_df.to_excel('Data/merged_annotations.xlsx', index=False)



