import os
import polars as pl
from utils import *

# for state in states
csv_files_dir = '../data/csv_files'
file = 'AC.csv'
file_path = os.path.join(csv_files_dir, file)
df = read_csv(file_path, separator = ',')