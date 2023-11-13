# Script to extract the raw data obtained to a folder of csv files

import os
import zipfile
from tqdm import tqdm

def get_list_of_zip_files(zip_dir):

    file_list = os.listdir(zip_dir)
    return file_list

def unzip_files(zip_dir, csv_dir):
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)

    file_list = get_list_of_zip_files(zip_dir)

    for file_name in tqdm(file_list):
        folder_name = os.path.splitext(file_name)[0] 
        file_path = os.path.join(zip_dir, file_name)

        if zipfile.is_zipfile(file_path):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(csv_dir) 

            for root, _, files in os.walk(csv_dir):
                for file in files:
                    if file.startswith('csv_licenciamento'):
                        new_name = os.path.join(root, folder_name + ".csv")
                        os.rename(os.path.join(root, file), new_name)

if __name__ == '__main__':

    zip_files_dir = './data/zip_files' 
    csv_files_dir = './data/csv_files'

    unzip_files(zip_files_dir, csv_files_dir)