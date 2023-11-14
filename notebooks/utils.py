import polars as pl
import pandas as pd

def replace_values(df, column_name, old_value, new_value):
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

def read_csv(file_path, separator = ','):
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

def strip_column(df: pl.DataFrame, column_name: str) -> pl.DataFrame:
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

