# PputProteotyping: Proteomic and Genomic Tools for *Pseudomonas putida* Analysis

This repository provides Python scripts for analyzing genomic and proteomic data of *Pseudomonas putida*, inserted in chapter IV of my doctoral thesis. It includes scripts for filtering, merging annotations, generating visualizations, and identifying biomarker candidates.

## Features
- **Genome Metrics and ANI Clustermap**:
  - Calculate genome size, GC content, N50, and other genome metrics.
  - Create hierarchical clustermaps from ANI matrices.

- **Sequence Retrieval**:
  - Extract protein sequences from a `.faa` file based on accession numbers.
  - Remove duplicate sequences.

- **Annotation Filtering and Merging**:
  - Filter EggNOG and InterPro annotation files based on accessions.
  - Merge filtered annotations, deduplicating Gene Ontology (GO) terms.

- **Visualization Tools**:
  - Generate Venn diagrams for species comparisons.
  - Create expression heatmaps from proteomic data.

- **Biomarker Candidate Identification**:
  - Identify species-specific unique proteins.

- **Top GO Terms Analysis**:
  - Analyze and visualize the top GO terms by species.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PputProteotyping.git
   cd PputProteotyping
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Genome Metrics Calculation
Calculate genome size statistics (e.g., N50, GC content, genome size):
```bash
python scripts/genome_metrics.py --input-dir /path/to/fasta_files --output-file /path/to/genome_stats.csv
```

### 2. ANI Clustermap
Generate a hierarchical clustermap from an ANI matrix:
```bash
python scripts/clustermap.py --matrix /path/to/ANI_matrix.xlsx --output /path/to/clustermap.png
```

### 3. Sequence Retrieval
Extract sequences based on accession numbers from an `.faa` file:
```bash
python scripts/sequence_retrieval.py --accession-file /path/to/PutidaP.xlsx --proteome-file /path/to/PputidaProteome.faa --output-file /path/to/unique_proteotyping_sequences.faa
```

### 4. Annotation Filtering and Merging
#### Filter Annotations:
Filter EggNOG and InterPro annotation files based on accession numbers:
```bash
python scripts/filter_annotations.py --accession-file /path/to/PutidaP.xlsx --eggnog-file /path/to/putida_eggnog.xlsx --interpro-file /path/to/putida_interpro.xlsx --eggnog-output /path/to/filtered_putida_eggnog.xlsx --interpro-output /path/to/filtered_putida_interpro.xlsx
```

#### Merge Annotations:
Combine filtered annotations:
```bash
python scripts/merge_annotations.py --eggnog-file /path/to/filtered_putida_eggnog.xlsx --interpro-file /path/to/filtered_putida_interpro.xlsx --output-file /path/to/merged_putida_annotations.xlsx
```

### 5. Venn Diagram
Generate a Venn diagram comparing species:
```bash
python scripts/venn_diagram.py --file-path /path/to/PutidaP.xlsx --output-file /path/to/VennDiagram.png
```

### 6. Expression Heatmap
Generate a heatmap from expression data:
```bash
python scripts/expression_heatmap.py --input-file /path/to/PutidaP.xlsx --output-file /path/to/clustermap_def.png --accession-column Accession --heatmap-columns ICU_D3_79 ICU_D3_93 UCE_D3_119 UCE_D3_129 UCE_D4_115
```

### 7. Biomarker Candidate Identification
Identify species-specific biomarker candidates:
```bash
python scripts/biomarker_candidates.py --species-file /path/to/PutidaP.xlsx --annotations-file /path/to/merged_putida_annotations.xlsx --output-file /path/to/biomarker_candidates_all.xlsx
```

### 8. Top GO Terms Analysis
Analyze and visualize the top GO terms by species:
```bash
python scripts/enrichment_goterms.py --species-file /path/to/PutidaP.xlsx --annotations-file /path/to/merged_putida_annotations.xlsx --output-dir /path/to/outputs
```
