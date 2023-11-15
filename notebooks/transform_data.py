import os
import pandas as pd
from utils import *

# for state in states
csv_files_dir = '../data/csv_files'
file = 'AC.csv'
file_path = os.path.join(csv_files_dir, file)
df = read_csv(file_path, separator = ',')

# NomeEntidade -> operator


# ClassInfraFisica 
df = strip_column(df, 'ClassInfraFisica')
df = replace_values(df, 'ClassInfraFisica', 'Greenfild', 'Greenfield')

# Tecnologia, tipoTecnologia
pdf['Technology'] = pdf.apply(lambda row: concatenate_columns(row, 'Tecnologia', 'tipoTecnologia'), axis=1)

