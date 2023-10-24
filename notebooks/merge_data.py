# Script to merge the csv files from different states into a single file

import os
from tqdm import tqdm
import polars as pl
from transform_data import read_csv


def merge_files(csv_files_dir, output_file):
   
    separator = ';'

    with open(output_file, mode="a") as f:

        for file in tqdm(os.listdir(csv_files_dir)):
            if file.endswith(".csv"):
                file_path = os.path.join(csv_files_dir, file)

                df = read_csv(file_path)

                df.write_csv(f, separator=separator)

def clear(csv_files_dir):

    files = os.listdir(csv_files_dir)

    for file in files:
        file_path = os.path.join(csv_files_dir, file)

        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")

if __name__ == '__main__':
    csv_files_dir = './data/csv_files'
    output_file = './data/merged_data.csv'
    zip_files_dir = './data/zip_files'

    merge_files(csv_files_dir, output_file)

    clear(csv_files_dir)

    clear(zip_files_dir)
