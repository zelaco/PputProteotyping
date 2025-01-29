# *Pseudomonas putida* group Proteotyping

## Code supplement

This repository provides Python scripts for analyzing genomic and proteomic data of the *Pseudomonas putida* group, inserted in chapter IV of my doctoral thesis. It includes scripts for filtering, merging annotations, generating visualizations, and identifying biomarker candidates.

## Script explanation
### `genome_metrics.py`:
* Parses multiple FASTA files in a directory.
* Calculates genome statistics including:
    - Genome size
    - GC content
    - Number of contigs
    - N50
    - Longest and shortest contig lengths
    - Average contig length
* Saves results to a CSV file.

### `clustermap.py`:
* Requires similarity matrix of genome-based identification data (ANI)
* Creates clustermaps for similarity matrices (ANI)

### `venn_diagram.py`:
* Generate a Venn diagram for species comparisons, based on the number of peptides found.

### `expression_heatmap.py`:
* Create expression heatmaps from proteomic data.

### `sequence_retrieval.py`:
* Extract protein sequences from a `.faa` file based on accession numbers.
* Remove duplicate sequences.

### `filter_annotations.py`:
* Filter EggNOG and InterPro annotation files based on accessions.

### `merge_annotations.py`:
* Merge filtered annotations outputs from previous script, deduplicating Gene Ontology (GO) terms.

### `top_goterms.py`:
* Analyze and visualize the top GO terms by species, based on the file with the merged annotations.

### `biomarker_candidates.py`:
* Identify species-specific unique proteins.

## Contact

If you have any questions or need further information, feel free to reach out:

    Email: [j.serpa@uib.es]
    GitHub: [github.com/zelaco]
