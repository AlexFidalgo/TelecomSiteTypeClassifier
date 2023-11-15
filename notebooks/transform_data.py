import os
import polars as pl
from utils import *

# for state in states
csv_files_dir = '../data/csv_files'
file = 'AC.csv'
file_path = os.path.join(csv_files_dir, file)
df = read_csv(file_path, separator = ',')

# removing whitespaces from edges of ClassInfraFisica
df = strip_column(df, 'ClassInfraFisica')

pdf = df.to_pandas()
pdf['Technology'] = pdf.apply(lambda row: concatenate_columns(row, 'Tecnologia', 'tipoTecnologia'), axis=1)




