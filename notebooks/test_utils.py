import unittest
import polars as pl
import utils
import pandas as pd

class TestStripColumn(unittest.TestCase):

    def test_strip_columns(self):

        data = {
            'col1': ['   apple  ', 'banana  ', '   cherry', None, 123],
            'col2': ['   dog', 'elephant', '   tiger  ', None, 'lion   '],
            'col3': [1, 2, 3, 4, 5]
        }
        df = pl.DataFrame(data)

        df = utils.strip_column(df, 'col1')

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

    def test_concatenate_columns(self):
        data = {
            'Tecnologia': ['apple', 'banana', 'cherry', None, '123', 'ab', None],
            'tipoTecnologia': ['dog', 'elephant', 'tiger', None, 'lion', None, 'bc'],
        }
        df = pd.DataFrame(data)

        df['tech'] = df.apply(lambda row: utils.concatenate_columns(row, 'Tecnologia', 'tipoTecnologia'), axis=1)

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

if __name__ == "__main__":
    unittest.main()
