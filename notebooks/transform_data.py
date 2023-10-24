import polars as pl

def read_csv(file_path):

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

    df = pl.read_csv(file_path, ignore_errors = True, dtypes = dtypes)
    return df