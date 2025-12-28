"""Tests for the data functions"""

import unittest
import pandas as pd
from {{cookiecutter.package_name}}.data import preprocess_data


class TestData(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(
            {
                "col-1": ["data-col-1"] * 3,
                "col-2": ["data-col-2"] * 3,
            }
        )

    def tearDown(self):
        self.df = None

    def test_preprocess_data(self):
        """Tests the `preprocess_data` function"""
        col_name = "fancy-col"
        df = preprocess_data(self.df, col_name)
        self.assertIn(col_name, df.columns)
