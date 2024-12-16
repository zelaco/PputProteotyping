import pandas as pd
import argparse

def merge_annotations(eggnog_file, interpro_file, output_file):
    eggnog_df = pd.read_excel(eggnog_file)
    interpro_df = pd.read_excel(interpro_file)

    # Merge and clean data
    merged_df = pd.merge(
        eggnog_df,
        interpro_df,
        left_on='Query ID',
        right_on='SeqName',
        how='outer',
        suffixes=('_EggNOG', '_InterPro')
    )
    merged_df.fillna('', inplace=True)

    # Deduplicate GO terms
    merged_df['GO'] = merged_df.apply(
        lambda row: '; '.join(sorted(set(row['GOs'].split(';') + row['GO IDs'].split(';')))),
        axis=1
    )
    merged_df['#GO'] = merged_df['GO'].apply(lambda x: len(x.split(';')))

    merged_df.drop(columns=['GOs', 'GO IDs'], inplace=True)
    merged_df.to_excel(output_file, index=False)
    print(f"Merged annotations saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge EggNOG and InterPro annotations.")
    parser.add_argument("--eggnog-file", required=True, help="Path to the filtered EggNOG file.")
    parser.add_argument("--interpro-file", required=True, help="Path to the filtered InterPro file.")
    parser.add_argument("--output-file", required=True, help="Path to save the merged annotations.")
    args = parser.parse_args()

    merge_annotations(args.eggnog_file, args.interpro_file, args.output_file)
