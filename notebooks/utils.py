import os
import re
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
    'NumEstacao',
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
    'PotenciaTransmissorWatts',
    'CodDebitoTFI',
    'DataLicenciamento',
    'DataPrimeiroLicenciamento',
    'DataValidade']]

    return df

def convert_bandwidth(value):
    """
    Convert bandwidth values from a specific format to numeric values.

    Parameters:
    - value (str): The input string representing bandwidth in a specific format.

    Returns:
    - int or None: The converted numeric bandwidth value or None if the input format is invalid.

    The input string should follow the format where the numeric part represents
    the three most significant digits of the bandwidth, and a letter represents the
    unit of bandwidth (H for Hertz, K for Kilohertz, M for Megahertz, G for Gigahertz).
    The optional decimal part is also supported.

    Examples:
    - convert_bandwidth('16K0') returns 16000
    - convert_bandwidth('5M00') returns 5000000
    - convert_bandwidth('40M0') returns 40000000
    - convert_bandwidth('2M14') returns 2140000
    - convert_bandwidth('27M5') returns 27500000
    - convert_bandwidth('2M50') returns 2500000
    - convert_bandwidth('invalid_format') returns None
    """
    match = re.match(r'(\d+)([HKMG])?(\d+)?', value)
    if match:
        number_part = int(match.group(1))
        unit_part = match.group(2)
        decimal_part = match.group(3)

        if unit_part == 'H':
            multiplier = 1
        elif unit_part == 'K':
            multiplier = 1e3
        elif unit_part == 'M':
            multiplier = 1e6
        elif unit_part == 'G':
            multiplier = 1e9
        else:
            multiplier = 1

        if decimal_part is not None:
            number_part = float(f"{number_part}.{decimal_part}")

        return int(number_part * multiplier)
    else:
        return None
 
def process_designacao_emissao(row):
    """
    Process the 'DesignacaoEmissao' column in a DataFrame row.

    Parameters:
    - row (pd.Series): A row of a DataFrame.

    Returns:
    pd.Series: A Series containing two columns:
        - 'LarguraFaixaNecessaria': The 4 characters after the first comma if the value is a set; otherwise, the first 4 characters of the first string separated by whitespaces.
        - 'CaracteristicasBasicas': The three characters after the first 4 in the first string if the value is a set; otherwise, the three characters after the first 4 in the first string.

    If the 'DesignacaoEmissao' value is None, both new columns will be set to None.
    """

    if pd.isnull(row['DesignacaoEmissao']):
        return pd.Series({'LarguraFaixaNecessaria': None, 'CaracteristicasBasicas': None})

    parts = row['DesignacaoEmissao'].split()

    if len(parts) > 1 and row['DesignacaoEmissao'].startswith('{') and row['DesignacaoEmissao'].endswith('}'):
        value_inside_set =parts[0][2:-2]
    else:
        value_inside_set = parts[0]

    largura_faixa_necessaria = value_inside_set[:4]

    caracteristicas_basicas = value_inside_set[4:7]

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

def extract_first_two_characters(direc_name1, direc_name2):
    """
    Extracts the first two characters of each file name in the specified directory.

    Parameters:
    - directory_path (str): The path to the directory containing the files.

    Returns:
    - list of str: A list containing the first two characters of each file name.
    """

    directory_path = os.path.join(os.path.dirname(__file__), os.pardir, direc_name1, direc_name2)
    
    files = os.listdir(directory_path)
    
    first_two_characters = [file[:2] for file in files]
    
    return first_two_characters

def set_aggregation(x):
    """
    Aggregate a pandas Series or DataFrame column by either returning the
    single unique element if all values are the same, or a set of unique
    elements if there are multiple distinct values.

    Parameters:
    - x: pandas Series or DataFrame column
        The input data to be aggregated.

    Returns:
    - Aggregated value:
        If all values are the same, returns the single unique element.
        If there are multiple distinct values, returns a set of unique elements.
    """

    if len(set(x)) == 1:
        return x.iloc[0]  
    else:
        return set(x)

def create_column_from_existing_column(df, new_column_name, eval_column_name, value):
    """
    Create a new Boolean column in a DataFrame based on the values of an existing column.

    Parameters:
    - df (pandas.DataFrame): The DataFrame to modify.
    - new_column_name (str): The name of the new Boolean column to create.
    - eval_column_name (str): The name of the column to evaluate for the condition.
    - value (str): The name of the column whose values will be used for evaluation.

    Returns:
    None: The function modifies the input DataFrame in place by adding a new Boolean column.

    """
    df[new_column_name] = False
    df.loc[df[eval_column_name] == value, new_column_name] = True

def agg_non_none(series):
    """
    Aggregate a pandas Series by returning the first non-None value.

    Parameters:
    - series (pd.Series): The input pandas Series.

    Returns:
    - The first non-None value in the Series, or None if all values are None.
    """
    non_none_values = series.dropna().values
    return non_none_values[0] if non_none_values.size > 0 else None

