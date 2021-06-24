import unittest
from numpy import dtype
import pandas as pd
from E3_2021ss_India import example
# TODO: Import your module with the logic (implementation)

import requests


class example1(unittest.TestCase):

    # Fetch and read should return the same, so if the dataset of fetch
    # is equal to read, we've done everything right!

    def test_read(self):
        obj = example()
        obj.get_head
        fetched = obj.fetch(
            "https://github.com/hka-mmv/dscb230-exercise/blob/main/e1/lecturer/NYPD_Complaint_Map__Year_to_Date.csv")
        readed = obj.read(
            "e3/india/NYPD_Complaint_Map__Year_to_Date.csv")
        self.assertEqual(fetched, readed)

    def test_get_position(self):  # get specific value of index
        pass

    # Testing Dataframes is complicated, because our dataset is large.
    # Therefor we'll going to test our methods with a smaller dataset!
    # Our data variable is not that hard secured, so we can reset the
    # value of it --> easy testing.

    def test_get_head(self):  # test the head method
        obj = example()
        obj.data = pd.util.testing.makeDataFrame()
        self.assertEqual(obj.data[:10], obj.get_head(10))

    def test_get_tail(self):  # test the tail method
        obj = example()
        obj.data = pd.util.testing.makeDataFrame()
        self.assertEqual(obj.data[-10:], obj.get_tail(10))

    # Straight forward, watch test_get_head()
    def test_get_type(self):  # test the dtypes method
        obj = example()
        obj.data = pd.util.testing.makeDataFrame()
        self.assertEqual(obj.data.dtypes, obj.get_type())

    # Straight forward, watch test_get_head()
    def test_get_info(self):  # describe / info
        obj = example()
        obj.data = pd.util.testing.makeDataFrame()
        self.assertEqual(obj.data.info(), obj.get_info())

    # Straight forward, watch test_get_head()
    def test_get_null(self):  # test the drop null method
        obj = example()
        obj.data = pd.util.testing.makeDataFrame()
        self.assertEqual(obj.data.isnull(), obj.get_null())

    # We can determine the size and test that, easy testing.
    def test_get_shape(self):  # test the col and row method
        obj = example()
        obj.fetch(
            "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv")
        self.assertEqual(obj.get_shape(), (126313, 23))


if __name__ == '__main__':
    unittest.main()
