import os
import pandas as pd
import polars as pl
from datetime import datetime

def replace_values_pl(df, column_name, old_value, new_value):
    """
    Replace old values with new values in a specified column of a Polars DataFrame.

    Parameters:
        df (pl.DataFrame): The input Polars DataFrame.
        column_name (str): The name of the column to perform the replacement in.
        old_value (str): The old value to be replaced in the specified column.
        new_value (str): The new value to replace the old value with.

    Returns:
        pl.DataFrame: A new Polars DataFrame with the specified replacements.
    """
    df = df.with_columns(df[column_name]
                        .str.replace(
                            old_value, 
                            new_value)
                            .alias(column_name))
    
    return df

def replace_values(df, column_name, old_value, new_value):
    """
    Replace old values with new values in a specified column of a Pandas DataFrame.

    Parameters:
        df (pd.DataFrame): The input Pandas DataFrame.
        column_name (str): The name of the column to perform the replacement in.
        old_value (str): The old value to be replaced in the specified column.
        new_value (str): The new value to replace the old value with.

    Returns:
        pd.DataFrame: A new Pandas DataFrame with the specified replacements.
    """
    df[column_name] = df[column_name].str.replace(old_value, new_value)
    
    return df

def read_csv_pl(file_path, separator = ','):
    """
    Read a CSV file into a Polars DataFrame with specified data types.

    Parameters:
        file_path (str): The path to the CSV file to be read.
        separator (str, optional): The delimiter used in the CSV file (default is ',').
        
    Returns:
        pl.DataFrame: A Polars DataFrame containing the data from the CSV file with specified data types.
    """

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

def read_csv(file_path, separator=',', encoding='ISO-8859-1'):
    """
    Read a CSV file into a Pandas DataFrame with specified data types.

    Parameters:
        file_path (str): The path to the CSV file to be read.
        separator (str, optional): The delimiter used in the CSV file (default is ',').
        encoding (str, optional): The encoding of the CSV file (default is 'utf-8').
        
    Returns:
        pd.DataFrame: A Pandas DataFrame containing the data from the CSV file with specified data types.
    """
    dtypes = {
        'NumAto': float,
        'AnguloMeiaPotenciaAntena': float,
        'PotenciaTransmissorWatts': float,
        'AlturaAntena': float,
        'GanhoAntena': str,
        'AnguloElevacao': float,
        'Azimute': float,
        'FrenteCostaAntena': float
    }

    df = pd.read_csv(file_path, dtype=dtypes, sep=separator, encoding = encoding, on_bad_lines='skip')
    return df

def strip_column_pl(df: pl.DataFrame, column_name: str) -> pl.DataFrame:
    """
    Strip whitespace from a specified column in a Polars DataFrame.

    Parameters:
    - df: Polars DataFrame
    - column_name: Name of the column to be cleaned and stripped

    Returns:
    - Stripped Polars DataFrame
    """

    s = pl.Series(
        df[column_name].map_elements(lambda x: x.strip() if isinstance(x, str) else x)
    )

    df = df.with_columns(s.alias(column_name))

    return df

def strip_column(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Strip whitespace from a specified column in a Pandas DataFrame.

    Parameters:
    - df: Pandas DataFrame
    - column_name: Name of the column to be cleaned and stripped

    Returns:
    - Stripped Pandas DataFrame
    """
    df[column_name] = df[column_name].apply(lambda x: x.strip() if isinstance(x, str) else x)
    return df

def concatenate_columns(row, first_column, second_column):
    """
    Concatenates values from two columns of a DataFrame row, handling null values.

    Parameters:
    - row (pandas.Series): A row from a DataFrame.
    - first_column (str): Name of the first column to concatenate.
    - second_column (str): Name of the second column to concatenate.

    Returns:
    str or None: Concatenated string based on the values of the specified columns.
    """
    first_value = str(row[first_column]) if pd.notna(row[first_column]) else None
    second_value = str(row[second_column]) if pd.notna(row[second_column]) else None

    if first_value and second_value:
        return first_value + '_' + second_value
    elif first_value:
        return first_value
    elif second_value:
        return second_value
    else:
        return None

def filter_columns(df):
    """
    Filter and select a subset of columns from the given DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing the columns.

    Returns:
    pd.DataFrame: A new DataFrame containing only the selected columns
    """

    df = df[[
    'SiglaUf',
    'CodMunicipio',
    'DesignacaoEmissao',
    'Tecnologia', 
    'tipoTecnologia',
    'FreqTxMHz',
    'FreqRxMHz',
    'CodTipoClasseEstacao',
    'ClassInfraFisica',
    'CompartilhamentoInfraFisica',
    'CodTipoAntena',
    'GanhoAntena',
    'FrenteCostaAntena',
    'AnguloMeiaPotenciaAntena',
    'AnguloElevacao',
    'Polarizacao',
    'AlturaAntena',
    'CodEquipamentoTransmissor',
    'PotenciaTransmissorWatts',
    'CodDebitoTFI',
    'DataLicenciamento',
    'DataPrimeiroLicenciamento',
    'DataValidade']]

    return df
 
def process_designacao_emissao(row):
    """
    Process the 'DesignacaoEmissao' column in a DataFrame row.

    Parameters:
    - row (pd.Series): A row of a DataFrame.

    Returns:
    pd.Series: A Series containing two columns:
        - 'LarguraFaixaNecessaria': Set of the first 4 characters of each string separated by whitespaces.
        - 'CaracteristicasBasicas': List of the three characters after the first 4 in each string.

    If the 'DesignacaoEmissao' value is None, both new columns will be set to None.
    """

    if pd.isnull(row['DesignacaoEmissao']):
        return pd.Series({'LarguraFaixaNecessaria': None, 'CaracteristicasBasicas': None})

    parts = row['DesignacaoEmissao'].split()

    largura_faixa_necessaria = set(part[:4] for part in parts)

    caracteristicas_basicas = [part[4:7] for part in parts]

    return pd.Series({'LarguraFaixaNecessaria': largura_faixa_necessaria, 'CaracteristicasBasicas': caracteristicas_basicas})

def process_data(row, date_column):
    """
    Process a DataFrame row to calculate the age since a specified date.

    Parameters:
    - row (pandas.Series): A row of a DataFrame.
    - date_column (str): The name of the column containing date information.

    Returns:
    - int or None: The age in days since the specified date if available, else None.
    """

    date_value = pd.to_datetime(row[date_column], errors='coerce')
    
    DiasDesde = (pd.to_datetime('today') - date_value).days if pd.notna(date_value) else None
    
    return DiasDesde

def extract_first_two_characters(directory_path):
    """
    Extracts the first two characters of each file name in the specified directory.

    Parameters:
    - directory_path (str): The path to the directory containing the files.

    Returns:
    - list of str: A list containing the first two characters of each file name.
    """
    
    files = os.listdir(directory_path)
    
    first_two_characters = [file[:2] for file in files]
    
    return first_two_characters