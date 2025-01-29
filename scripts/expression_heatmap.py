import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the data from your Excel file
data = pd.read_excel("Data/PutidaP.xlsx")

# Extract the Accession column and heatmap data (columns U to Y)
accession_column = 'Accession'  
heatmap_columns = ['ICU_D3_79', 'ICU_D3_93', 'UCE_D3_119', 'UCE_D3_129', 'UCE_D4_115']  

# Subset the data
heatmap_data = data[[accession_column] + heatmap_columns].set_index(accession_column)

# Remove rows where any value in heatmap_columns is zero or NaN
heatmap_data = heatmap_data[(heatmap_data != 0).all(axis=1)].dropna(subset=heatmap_columns)

# Plot the clustermap
sns.clustermap(
    heatmap_data,
    cmap='magma_r',       # Choose a colormap
    metric='euclidean',   # Distance metric for clustering
    method='average',     # Clustering method
    figsize=(10, 12),      # Adjust the size of the plot
    yticklabels=False,     # Remove y-axis labels
    row_cluster=False,    # Disable row clustering
    dendrogram_ratio=(.1, .1), # Adjust the size of the dendrogram
    cbar_pos=(0, .2, .03, .4)     # Position of the colorbar
)

# Save the plot
plt.savefig('Outputs/clustermap_def.png', dpi=300, bbox_inches='tight')