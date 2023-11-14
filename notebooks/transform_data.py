import os
import polars as pl
from utils import *

# for state in states
csv_files_dir = '../data/csv_files'
file = 'AC.csv'
file_path = os.path.join(csv_files_dir, file)
df = read_csv(file_path, separator = ',')

# removing whitespaces from edges of ClassInfraFisica
df = (
    df.select(
        pl.col('ClassInfraFisica')
        .map_elements(lambda x: x.strip() if isinstance(x, str) else x)
        .alias('ClassInfraFisica')
    )
)

