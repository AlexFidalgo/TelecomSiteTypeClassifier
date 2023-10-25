import polars as pl

def read_csv(file_path, separator = ','):

    dtypes = {
        'NumAto': float,
        'AnguloMeiaPotenciaAntena': float,
        'PotenciaTransmissorWatts': float,
        'AlturaAntena': float,
        'GanhoAntena': str,
        'AnguloElevacao': float,
        'Azimute':float,
        'FrenteCostaAntena': float
        }

    df = pl.read_csv(file_path, ignore_errors = True, dtypes = dtypes, separator = separator)
    return df

if __name__ == '__main__':
    
    merged_file_path = './data/merged_data.csv'
    
    df = read_csv(merged_file_path, separator=';')

    x = 1