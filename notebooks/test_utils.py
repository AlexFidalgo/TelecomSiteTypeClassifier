import unittest
import polars as pl
import utils

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

if __name__ == "__main__":
    unittest.main()
