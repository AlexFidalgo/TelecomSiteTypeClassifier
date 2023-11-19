# Cleans csv_files, filtering and processing columns to create cleaned_csv_files

import os
import pandas as pd
from utils import *
from tqdm import tqdm

csv_files_directory = './data/csv_files'
states = extract_first_two_characters(csv_files_directory)

script_path = os.path.realpath(__file__) # path to the current script
script_directory = os.path.dirname(script_path) # directory of the script
script_directory_parent = os.path.dirname(script_directory) # parent of the directory of the script

cleaned_directory_path = os.path.join(script_directory_parent, 'data', 'cleaned_csv_files')
if not os.path.exists(cleaned_directory_path):
    os.makedirs(cleaned_directory_path)

for state in tqdm(states):

    print(f"\n{state}")

    file = f'{state}.csv'
    file_path = os.path.join(csv_files_directory, file)
    polars_df = read_csv_pl(file_path, separator = ',')
    df = polars_df.to_pandas()

    # filters only relevant coluns
    df = filter_columns(df)

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
    df['DiasDesdeLicenciamento'] = df.apply(process_data, date_column='DataLicenciamento', axis=1)
    df.drop(columns=['DataLicenciamento'], inplace=True)

    #DataPrimeiroLicenciamento
    df['DiasDesdePrimeiroLicenciamento'] = df.apply(process_data, date_column='DataPrimeiroLicenciamento', axis=1)
    df.drop(columns=['DataPrimeiroLicenciamento'], inplace=True)

    #DataValidade
    df['DiasAteExpirar'] = df.apply(process_data, date_column='DataValidade', axis=1)

    df.to_csv(os.path.join(cleaned_directory_path, f'{state}.csv'), index=False)

