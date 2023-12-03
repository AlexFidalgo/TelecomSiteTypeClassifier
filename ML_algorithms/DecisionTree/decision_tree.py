import pandas as pd
import os
from clean_data_for_decision_tree import *

# Find anatel file path
script_directory = os.path.dirname(os.path.realpath(__file__)) # directory of this script
script_directory_parent2 = os.path.dirname(os.path.dirname(script_directory)) # parent of the directory of the script
anatel_file_path = os.path.join(script_directory_parent2, 'data', 'labeled_csv_files', 'Anatel_labeled.csv')

anatel = pd.read_csv(anatel_file_path)

get_rid_of_problematic_columns(anatel)

# One-Hot Encoding
anatel = pd.get_dummies(anatel, columns=['Polarizacao_max'], prefix='Polarizacao')
anatel = pd.get_dummies(anatel, columns=['CaracteristicasBasicas_agg_non_none'], prefix='CaracteristicasBasicas')

anatel.set_index('NumEstacao', inplace=True)
