import os
import pandas as pd
from utils import *
from tqdm import tqdm

states = extract_first_two_characters('data', 'csv_files')

script_path = os.path.realpath(__file__) # path to the current script
script_directory = os.path.dirname(script_path) # directory of the script
script_directory_parent = os.path.dirname(script_directory) # parent of the directory of the script

output_directory_path = os.path.join(script_directory_parent, 'data')

cons = pd.DataFrame()

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
        'GanhoAntena': agg_non_none,
        'FrenteCostaAntena': 'max',
        'AnguloMeiaPotenciaAntena': 'max',
        'AnguloElevacao': 'min',
        'Polarizacao': 'max',
        'AlturaAntena': 'max',
        'PotenciaTransmissorWatts': 'max',
        'CodDebitoTFI': 'max',
        'LarguraFaixaNecessaria': 'max',
        'CaracteristicasBasicas': agg_non_none,
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
    g.columns = [f"{col[0]}_{col[1]}" if isinstance(col, tuple) else col for col in g.columns]

    cons = pd.concat([cons, g])

cons.to_csv(os.path.join(output_directory_path, 'Anatel.csv'), index=False)

lab = cons[cons['ClassInfraFisica_agg_non_none'].notna()]

get_rid_of_problematic_columns(lab)

rename_anatel_cols(lab)

lab = lab.dropna() # Treatment of Null values

# Station as the index
lab['Station'] = lab['Station'].astype(int)
lab.set_index('Station', inplace=True)

labeled_directory_path = os.path.join(script_directory_parent, 'data', 'labeled_csv_files')
if not os.path.exists(labeled_directory_path):
    os.makedirs(labeled_directory_path)

lab.to_csv(os.path.join(labeled_directory_path, 'Anatel_labeled.csv'), index=False)