import pandas as pd

# File paths
putida_p_file = 'Data/PutidaP.xlsx'
putida_eggnog_file = 'Data/putida_eggnog.xlsx'
putida_interpro_file = 'Data/putida_interpro.xlsx'

# Load data
putida_p_df = pd.read_excel(putida_p_file)  # Load PutidaP.xlsx
putida_eggnog_df = pd.read_excel(putida_eggnog_file)  # Load eggnog file
putida_interpro_df = pd.read_excel(putida_interpro_file)  # Load interpro file

# Extract the Accession column
accessions = putida_p_df['Accession'].tolist()

# Filter putida_eggnog based on Query ID
filtered_eggnog = putida_eggnog_df[putida_eggnog_df['Query ID'].isin(accessions)]

# Filter putida_interpro based on SeqName
filtered_interpro = putida_interpro_df[putida_interpro_df['SeqName'].isin(accessions)]

# Save the filtered data to new Excel files
filtered_eggnog.to_excel('filtered_putida_eggnog.xlsx', index=False)
filtered_interpro.to_excel('filtered_putida_interpro.xlsx', index=False)

print("Filtered files saved: filtered_putida_eggnog.xlsx and filtered_putida_interpro.xlsx")
