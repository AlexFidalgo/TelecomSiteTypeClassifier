# Script to merge the csv files from different states into a single file

import os
from tqdm import tqdm
import polars as pl
from transform_data import read_csv


def merge_files(csv_files_dir, output_file):
   
    merged_data = None

    for file in tqdm(os.listdir(csv_files_dir)):
        if file.endswith(".csv"):
            file_path = os.path.join(csv_files_dir, file)

            df = read_csv(file_path)

            if merged_data is None:
                merged_data = df
            else:
                merged_data = pl.concat([merged_data, df])

    merged_data.write_csv(output_file, separator = ';')

if __name__ == '__main__':
    csv_files_dir = './data/csv_files'
    output_file = './data/csv_files/merged_data.csv'

    merge_files(csv_files_dir, output_file)
