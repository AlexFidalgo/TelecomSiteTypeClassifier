import os
import pandas as pd
from utils import *

# for state in states
csv_files_dir = '../data/csv_files'
file = 'AC.csv'
file_path = os.path.join(csv_files_dir, file)
df = read_csv(file_path, separator = ',')

# CodMunicipio
df['CodMunicipio'] = df['CodMunicipio'].fillna(0).astype(int)

# DesignacaoEmissao
df[['LarguraFaixaNecessaria', 'CaracteristicasBasicas']] = df.apply(process_designacao_emissao, axis=1)
df.drop(columns=['DesignacaoEmissao'], inplace=True)

# Tecnologia, tipoTecnologia
df['Tecnologia_e_Tipo'] = df.apply(lambda row: concatenate_columns(row, 'Tecnologia', 'tipoTecnologia'), axis=1)
df.drop(columns=['Tecnologia', 'tipoTecnologia'], inplace=True)

# ClassInfraFisica 
df = strip_column(df, 'ClassInfraFisica')
df['ClassInfraFisica'] = df['ClassInfraFisica'].str.upper()
df = replace_values(df, 'ClassInfraFisica', 'GREENFILD', 'GREENFIELD')

# CodTipoAntena
df['CodTipoAntena'] = df['CodTipoAntena'].fillna(0).astype(int)
df['CodTipoAntena'] = df['CodTipoAntena'].astype(str)

# GanhoAntena
df['GanhoAntena'] = pd.to_numeric(df['GanhoAntena'], errors='coerce')

# FrenteCostaAntena
df['FrenteCostaAntena'] = pd.to_numeric(df['FrenteCostaAntena'], errors='coerce')

# AnguloMeiaPotenciaAntena
df['AnguloMeiaPotenciaAntena'] = pd.to_numeric(df['AnguloMeiaPotenciaAntena'], errors='coerce')

# AnguloElevacao
df['AnguloElevacao'] = pd.to_numeric(df['AnguloElevacao'], errors='coerce')

# Polarizacao
df['Polarizacao'] = df['Polarizacao'].str.upper()

# AlturaAntena
df['AlturaAntena'] = pd.to_numeric(df['AlturaAntena'], errors='coerce')

# DataLicenciamento
df['IdadeLicenciamento'] = df.apply(process_data, date_column='DataLicenciamento', axis=1)
df.drop(columns=['DataLicenciamento'], inplace=True)

#DataPrimeiroLicenciamento
df['IdadePrimeiroLicenciamento'] = df.apply(process_data, date_column='DataPrimeiroLicenciamento', axis=1)
df.drop(columns=['DataLicenciamento'], inplace=True)