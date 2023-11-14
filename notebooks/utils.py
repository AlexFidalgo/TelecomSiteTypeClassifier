import polars as pl

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
