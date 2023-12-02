# Cleans csv_files, filtering and processing columns to create cleaned_csv_files

import os
import pandas as pd
from utils import *
from tqdm import tqdm

states = extract_first_two_characters('data', 'csv_files')

script_path = os.path.realpath(__file__) # path to the current script
script_directory = os.path.dirname(script_path) # directory of the script
script_directory_parent = os.path.dirname(script_directory) # parent of the directory of the script

cleaned_directory_path = os.path.join(script_directory_parent, 'data', 'cleaned_csv_files')
if not os.path.exists(cleaned_directory_path):
    os.makedirs(cleaned_directory_path)

for state in tqdm(states):
    print(f"\n{state}")

    file = f'{state}.csv'
    file_path = os.path.join(script_directory_parent, 'data', 'csv_files', file)
    polars_df = read_csv_pl(file_path, separator = ',')
    df = polars_df.to_pandas()

    # filters only relevant coluns
    df = filter_columns(df)

    # CodMunicipio
    df['CodMunicipio'] = df['CodMunicipio'].fillna(0).astype(int)

    # DesignacaoEmissao
    df[['LarguraFaixaNecessaria', 'CaracteristicasBasicas']] = df.apply(process_designacao_emissao, axis=1)
    df['LarguraFaixaNecessaria'] = df['LarguraFaixaNecessaria'].apply(convert_bandwidth)
    df.drop(columns=['DesignacaoEmissao'], inplace=True)

    # Tecnologia, tipoTecnologia
    df['Tecnologia_e_Tipo'] = df.apply(lambda row: concatenate_columns(row, 'Tecnologia', 'tipoTecnologia'), axis=1)
    df.drop(columns=['Tecnologia', 'tipoTecnologia'], inplace=True)
    df['Tecnologia_e_Tipo'] = df['Tecnologia_e_Tipo'].astype(str)
    df['Tecnologia_e_Tipo'] = df['Tecnologia_e_Tipo'].replace('None', None)
    df = replace_values(df, 'Tecnologia_e_Tipo', 'NSA', 'NR_NSA')
    df = replace_values(df, 'Tecnologia_e_Tipo', 'NR', 'NR_SA-NSA')
    create_column_from_existing_column(df, 'LTE', 'Tecnologia_e_Tipo', 'LTE')
    create_column_from_existing_column(df, 'WCDMA', 'Tecnologia_e_Tipo', 'WCDMA')
    create_column_from_existing_column(df, 'GSM', 'Tecnologia_e_Tipo', 'GSM')
    create_column_from_existing_column(df, 'WCDMA', 'Tecnologia_e_Tipo', 'WCDMA')
    create_column_from_existing_column(df, 'NR_NSA', 'Tecnologia_e_Tipo', 'NR_NSA')
    create_column_from_existing_column(df, 'NR_SA-NSA', 'Tecnologia_e_Tipo', 'NR_SA-NSA')
    create_column_from_existing_column(df, 'DMR', 'Tecnologia_e_Tipo', 'DMR')
    create_column_from_existing_column(df, 'Digital', 'Tecnologia_e_Tipo', 'digital')
    df.drop(columns=['Tecnologia_e_Tipo'], inplace = True)

    # ClassInfraFisica 
    df = strip_column(df, 'ClassInfraFisica')
    df['ClassInfraFisica'] = df['ClassInfraFisica'].str.upper()
    df = replace_values(df, 'ClassInfraFisica', 'GREENFILD', 'GREENFIELD')

    # CompartilhamentoInfraFisica
    df['CompartilhamentoInfraFisica'] = df['CompartilhamentoInfraFisica'].str.upper()

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
    df.drop(columns=['DataValidade'], inplace=True)

    # Converting object type to appropriate type
    df['SiglaUf'] = df['SiglaUf'].astype(str)
    df['CodTipoClasseEstacao'] = df['CodTipoClasseEstacao'].astype(str)
    df['GanhoAntena'] = df['GanhoAntena'].astype(float)
    df['Polarizacao'] = df['Polarizacao'].astype(str)
    df['CodDebitoTFI'] = df['CodDebitoTFI'].astype(str)

    # NaN treatment
    df['FreqTxMHz'] = df['FreqTxMHz'].astype(float)
    df['FreqRxMHz'] = df['FreqRxMHz'].astype(float)

    df.to_csv(os.path.join(cleaned_directory_path, f'{state}.csv'), index=False)

