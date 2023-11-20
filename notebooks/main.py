import subprocess
import os
from extract_data import *
from merge_data import *
from transform_data import *

if __name__ == '__main__':

    data_dir = './data'
    zip_files_dir = os.path.join(data_dir, 'zip_files')
    csv_files_dir = os.path.join(data_dir, 'csv_files')

    # Create 'data' and 'csv_files' directories if they don't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    if not os.path.exists(csv_files_dir):
        os.makedirs(csv_files_dir)

    script_path = './src/download.ps1'
    subprocess.run(['powershell', script_path])

    unzip_files(zip_files_dir, csv_files_dir)

    # Optionally, clear 'zip_files' directory after unzipping
    clear(zip_files_dir)

    script_path = 'transform_data.py'
    subprocess.run(['python', script_path])
