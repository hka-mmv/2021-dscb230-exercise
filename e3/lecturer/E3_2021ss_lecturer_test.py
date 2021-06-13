import unittest
import pandas as pd
# TODO import your path to the main python file (with logic, ...)
import E3_2021ss_lecturer
import requests


class example(unittest.TestCase):

    # fetch and read should return the same, so if the dataframe of fetch
    # is equal to read, we've done everything right!

    def test_read(self):
        obj = example()
        fetched = obj.fetch(
            "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv")
        readed = obj.read("../../e1/lecturer/nbaallelo.csv")
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

    # straight forward, watch test_get_head()
    def test_get_type(self):  # test the dtypes method
        pass

    # straight forward, watch test_get_head()
    def test_get_info(self):  # describe / info
        pass

    # straight forward, watch test_get_head()
    def test_get_null(self):  # test the drop null method
        pass

    # We can determine the size and test that, easy testing.
    def test_get_size(self):  # test the col and row method
        obj = example()
        obj.fetch(
            "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv")
        self.assertEqual(obj.get_size(), (126313, 23))


if __name__ == '__main__':
    unittest.main()
