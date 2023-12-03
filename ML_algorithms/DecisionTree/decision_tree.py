import pandas as pd
import os

script_directory = os.path.dirname(os.path.realpath(__file__)) # directory of this script
script_directory_parent2 = os.path.dirname(os.path.dirname(script_directory)) # parent of the directory of the script
anatel_file_path = os.path.join(script_directory_parent2, 'data', 'labeled_csv_files', 'Anatel_labeled.csv')

anatel = pd.read_csv(anatel_file_path)

