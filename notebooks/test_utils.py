import unittest
import polars as pl
import pandas as pd
from utils import *

class TestUtils(unittest.TestCase):

    def test_replace_values(self):

        data = {
            'Column1': ['apple', 'banana', 'orange', 'apple', 'orange'],
            'Column2': [1, 2, 3, 4, 5]
        }
        df = pd.DataFrame(data)

        df_modified = replace_values(df, 'Column1', 'apple', 'fruit')

        expected_df = pd.DataFrame({
            'Column1': ['fruit', 'banana', 'orange', 'fruit', 'orange'],
            'Column2': [1, 2, 3, 4, 5]
        })

        self.assertTrue(df.equals(expected_df))

    def test_strip_columns_pl(self):

        data = {
            'col1': ['   apple  ', 'banana  ', '   cherry', None, 123],
            'col2': ['   dog', 'elephant', '   tiger  ', None, 'lion   '],
            'col3': [1, 2, 3, 4, 5]
        }
        df = pl.DataFrame(data)

        df = strip_column_pl(df, 'col1')

        expected_df = pl.DataFrame(
            data = {
                'col1': ['apple', 'banana', 'cherry', None, 123],
                'col2': ['   dog', 'elephant', '   tiger  ', None, 'lion   '],
                'col3': [1, 2, 3, 4, 5]
            }
        )

        df_arrow = df.to_arrow()
        expected_arrow = expected_df.to_arrow()
        self.assertTrue(df_arrow.equals(expected_arrow))

    def test_strip_column(self):
        data = {
            'col1': ['   apple  ', 'banana  ', '   cherry', None, 123],
            'col2': ['   dog', 'elephant', '   tiger  ', None, 'lion   '],
            'col3': [1, 2, 3, 4, 5]
        }
        df = pd.DataFrame(data)

        df = strip_column(df, 'col1')

        expected_df = pd.DataFrame(
            data={
                'col1': ['apple', 'banana', 'cherry', None, 123],
                'col2': ['   dog', 'elephant', '   tiger  ', None, 'lion   '],
                'col3': [1, 2, 3, 4, 5]
            }
        )

        self.assertTrue(df.equals(expected_df))

    def test_concatenate_columns(self):
        data = {
            'Tecnologia': ['apple', 'banana', 'cherry', None, '123', 'ab', None],
            'tipoTecnologia': ['dog', 'elephant', 'tiger', None, 'lion', None, 'bc'],
        }
        df = pd.DataFrame(data)

        df['tech'] = df.apply(lambda row: concatenate_columns(row, 'Tecnologia', 'tipoTecnologia'), axis=1)

        expected_df = pd.DataFrame(
            data={
                'Tecnologia': ['apple', 'banana', 'cherry', None, '123', 'ab', None],
                'tipoTecnologia': ['dog', 'elephant', 'tiger', None, 'lion', None, 'bc'],
                'tech': ['apple_dog', 'banana_elephant', 'cherry_tiger', None, '123_lion', 'ab', 'bc']
            }
        )
        # print(f"df = {df}")
        # print(f"expected_df = {expected_df}")

        self.assertTrue(df.equals(expected_df))

    def test_process_designacao_emissao(self):

        data = {'DesignacaoEmissao': ['8K30F1D', '7K60F1E 7K60F1W', '7K60F1E 7K61F1W', None]}
        pdf = pd.DataFrame(data)

        result = pdf.apply(process_designacao_emissao, axis=1)

        expected_output = pd.DataFrame({
            'LarguraFaixaNecessaria': [{'8K30'}, {'7K60'}, {'7K60', '7K61'}, None],
            'CaracteristicasBasicas': [['F1D'], ['F1E', 'F1W'], ['F1E', 'F1W'], None]
        })

        pd.testing.assert_frame_equal(result, expected_output)

if __name__ == "__main__":
    unittest.main()
