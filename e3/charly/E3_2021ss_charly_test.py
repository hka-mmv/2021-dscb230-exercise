import unittest
import pandas as pd
from E3_2021ss_charly import Example


class ExampleTest(unittest.TestCase):

    # Fetch and read should return the same, so if the dataset of fetch
    # is equal to read, we've done everything right!
    # dataset not available locally, therefore skipped

    def test_get_position(self):  # get specific value of index
        pass

    # Testing Dataframes is complicated, because our dataset is large.
    # Therefor we'll going to test our methods with a smaller dataset!
    # Our data variable is not that hard secured, so we can reset the
    # value of it --> easy testing.

    def test_get_head(self):  # test the head method
        obj = Example()
        obj.data = pd.util.testing.makeDataFrame()
        self.assertEqual(obj.data[:10].equals(obj.get_head(10)), True)

    def test_get_tail(self):  # test the tail method
        obj = Example()
        obj.data = pd.util.testing.makeDataFrame()
        self.assertEqual(obj.data[-10:].equals(obj.get_tail(10)), True)

    # Straight forward, watch test_get_head()
    def test_get_type(self):  # test the dtypes method
        pass

    # Straight forward, watch test_get_head()
    def test_get_info(self):  # describe / info
        pass

    # Straight forward, watch test_get_head()
    def test_get_null(self):  # test the drop null method
        pass

    # We can determine the size and test that, easy testing.
    def test_get_size(self):  # test the col and row method
        obj = Example()
        new_data = obj.fetch(
            "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv")
        self.assertEqual(new_data.shape, (126314, 23))


if __name__ == '__main__':
    unittest.main()
