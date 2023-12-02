import os
import pandas as pd
from utils import *
from tqdm import tqdm

states = extract_first_two_characters('data', 'csv_files')

script_path = os.path.realpath(__file__) # path to the current script
script_directory = os.path.dirname(script_path) # directory of the script
script_directory_parent = os.path.dirname(script_directory) # parent of the directory of the script

output_directory_path = os.path.join(script_directory_parent, 'data')


df = pd.DataFrame()

for state in tqdm(states):
    print(f"\n{state}")

    file = f'{state}.csv'
    file_path = os.path.join(script_directory_parent, 'data', 'cleaned_csv_files', file)
    polars_df = read_csv_pl(file_path, separator = ',')
    df = polars_df.to_pandas()

    # Aggregation
    aggregation_dict = {
        'SiglaUf': 'max',
        'CodMunicipio': 'max',
        'FreqTxMHz': ['min', 'max'],
        'FreqRxMHz': ['min', 'max'],
        'CodTipoClasseEstacao': 'max',
        'ClassInfraFisica': agg_non_none,
        'CompartilhamentoInfraFisica': agg_non_none,
        'CodTipoAntena': 'max',
        'GanhoAntena': 'max',
        'FrenteCostaAntena': 'max',
        'AnguloMeiaPotenciaAntena': 'max',
        'AnguloElevacao': 'min',
        'Polarizacao': 'max',
        'AlturaAntena': 'max',
        'PotenciaTransmissorWatts': 'max',
        'CodDebitoTFI': 'max',
        'LarguraFaixaNecessaria': 'max',
        'CaracteristicasBasicas': 'max',
        'LTE': 'max',
        'WCDMA': 'max',
        'GSM': 'max',
        'NR_NSA': 'max',
        'NR_SA-NSA': 'max',
        'DMR': 'max',
        'Digital': 'max',
        'DiasDesdeLicenciamento': 'max', 
        'DiasDesdePrimeiroLicenciamento': 'max',
        'DiasAteExpirar': 'min'}

    g = df.groupby('NumEstacao').agg(aggregation_dict).reset_index()
    g.columns = [' '.join(col).strip() for col in g.columns.values] # Flattens the multi-level column index

    df = pd.concat([df, g])

df.to_csv(os.path.join(output_directory_path, f'Anatel.csv'), index=False)