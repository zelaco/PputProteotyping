import pandas as pd
import seaborn as sns
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import squareform

# Load your ANI matrix from Excel
ani_matrix = pd.read_excel('Data/ANI_Matrix.xlsx', index_col=0)

# Make the matrix symmetrical by averaging reciprocal values
for i in range(ani_matrix.shape[0]):
    for j in range(i + 1, ani_matrix.shape[1]):
        avg_value = (ani_matrix.iloc[i, j] + ani_matrix.iloc[j, i]) / 2
        ani_matrix.iloc[i, j] = avg_value
        ani_matrix.iloc[j, i] = avg_value

# Convert the ANI values to distance values (100 - ANI)
distance_matrix = 100 - ani_matrix

# Convert the distance matrix to a condensed form (1D) for the linkage function
condensed_distance_matrix = squareform(distance_matrix)

# Perform hierarchical clustering using UPGMA (method='average')
linkage_matrix = linkage(condensed_distance_matrix, method='average')

# Create a seaborn clustermap, now only using the row_linkage
clustermap = sns.clustermap(
    ani_matrix,
    row_linkage=linkage_matrix,
    col_linkage=linkage_matrix,  # You can set this to None if you want to cluster only rows
    cmap='coolwarm',
    figsize=(20, 15),  # Increase figure size
    dendrogram_ratio=(.2, 0),  # Adjust the ratio of the dendrogram to the heatmap
    cbar_pos=(1.1, 0.3, 0.03, 0.4)  # Adjust the position of the color bar (legend)
)

# Adjust dendrogram line thickness
for line in clustermap.ax_row_dendrogram.collections:
    line.set_linewidth(2)  # Thicker row dendrogram lines

# Adjust the font size and font name of the species names (row and column labels)
# Remove the labels below (column labels)
clustermap.ax_heatmap.set_xticklabels([])
    
clustermap.ax_heatmap.set_yticklabels(
    clustermap.ax_heatmap.get_yticklabels(), fontsize=22, fontname='Arial', fontstyle='italic') 

# Adjust the font size of the color bar (legend)
clustermap.ax_cbar.set_yticklabels(clustermap.ax_cbar.get_yticklabels(), fontsize=20) 

# Rotate the labels and adjust the font size for readability
clustermap.ax_heatmap.set_xticklabels(clustermap.ax_heatmap.get_xticklabels(), rotation=90, fontsize=20)
clustermap.ax_heatmap.set_yticklabels(clustermap.ax_heatmap.get_yticklabels(), rotation=0, fontsize=20)

# Save the figure to a file instead of showing it
clustermap.savefig("Outputs/ANI_clustermap.png", dpi=300)  

# Extract the reordered indices of rows and columns from the clustermap
reordered_rows = clustermap.dendrogram_row.reordered_ind
reordered_cols = clustermap.dendrogram_col.reordered_ind

# Reorder the matrix according to the clustered heatmap order
reordered_matrix = ani_matrix.iloc[reordered_rows, reordered_cols]

# Export the reordered matrix to Excel
reordered_matrix.to_excel('Data/reordered_ANI_matrix.xlsx')