import polars as pl
from utils import strip_column

def test_strip_column():

    data = {
        'col1': ['   apple  ', 'banana  ', '   cherry', None, 123],
        'col2': ['   dog', 'elephant', '   tiger  ', None, 'lion   '],
        'col3': [1, 2, 3, 4, 5]
    }
    df = pl.DataFrame(data)

    cleaned_df_col1 = strip_column(df, 'col1')
    expected_data_col1 = {'col1': ['apple', 'banana', 'cherry', None, 123]}
    expected_df_col1 = pl.DataFrame(expected_data_col1)
    assert cleaned_df_col1 == expected_df_col1

    # Test stripping whitespace from 'col2'
    cleaned_df_col2 = strip_column(df, 'col2')
    expected_data_col2 = {'col2': ['dog', 'elephant', 'tiger', None, 'lion']}
    expected_df_col2 = pl.DataFrame(expected_data_col2)
    assert cleaned_df_col2 == expected_df_col2

    # Test stripping whitespace from 'col3'
    cleaned_df_col3 = strip_column(df, 'col3')  # Should not modify non-string column
    assert cleaned_df_col3 == df

    # Test stripping whitespace from all columns
    cleaned_df_all = strip_column(df, 'col1')
    cleaned_df_all = strip_column(cleaned_df_all, 'col2')
    cleaned_df_all = strip_column(cleaned_df_all, 'col3')  # Should not modify non-string column
    assert cleaned_df_all == pl.DataFrame({'col1': ['apple', 'banana', 'cherry', None, 123],
                                            'col2': ['dog', 'elephant', 'tiger', None, 'lion'],
                                            'col3': [1, 2, 3, 4, 5]})
