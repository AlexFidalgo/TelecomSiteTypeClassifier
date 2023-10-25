import subprocess
from extract_data import *
from merge_data import *
from transform_data import *


if __name__ == '__main__':

    script_path = './src/download.ps1'
    # with open(script_path, 'r') as script_file:
    #     script_content = script_file.read()
    #     print(script_content)
    subprocess.run(['powershell', script_path])

    zip_files_dir = './data/zip_files' 
    csv_files_dir = './data/csv_files'
    unzip_files(zip_files_dir, csv_files_dir)

    zip_files_dir = './data/zip_files'
    clear(zip_files_dir)
