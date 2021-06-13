import pandas as pd
import matplotlib.pyplot as plt
import requests


class example:

    def __init__(self):
        self.data = self.read("e1/lecturer/AB_NYC_2019.csv")
        self.url = "https://github.com/hka-mmv/dscb230-exercise/blob/main/e1/lecturer/AB_NYC_2019.csv.zip"

    # --------------- GET THE DATA ---------------

    def fetch(self, url):
        """This Method fetches a dataset from a given url"""

        # NOTE: Fetching a HTTP request usually needs "try except"!
        # TODO
        try:
            r = requests.get(url)
            dataset = r
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            pass
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            pass
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)
        return dataset

    def read(self, filename):
        """This method reads a given file

        It can important any file extension like json, csv, etc.
        """
        data = None

        # NOTE: Use "assert" if filename contains a dot for the extension (data not okay, data.csv okay)
        # TODO
        assert "." in filename, f"{filename} is not valid filename"  # TODO
        data = pd.read_csv(filename)  # TODO
        print(data)  # TODO
        return data

    # --------------- DATA UNDERSTANDING ---------------

    # This section contains methods for searching the dataset for specific characteristics.
    # The docstrings will help you to use them.
    # NOTE: Use "unittest" to check if the get methods return the right data

    def get_if(self, statement):
        """This Method returns every data which fits into the bool statement"""
        return self.data[statement]

    def get_head(self, limit=10):
        """This Method reads the head out of the data"""
        return self.data.head(limit)

    def get_tail(self):
        """This Method reads the tail out of the data"""
        return self.data.tail()

    def get_info(self, verbose=True):
        """This Method reads the info out of the data"""
        return self.data.info()

    def get_shape(self):
        """This Method reads tbd"""
        return self.data.shape

    def get_value(self, key):
        """This Method returns every value for a given key"""
        return self.data[key]

    # --------------- DATA PREPARATION ---------------

    def dropnullvalues(self):
        """ This method drops rows which contains missing values.

        See also https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
        """
        return self.data.dropna(axis=1)

    # --------------- VISUALIZATION ---------------

    def draw_hist(self):
        """This Method draws a hist diagram"""
        self.data.hist()

    def draw_facetgrid(self):
        """This Method draws a facetgrid"""
        pass

    def draw_scatter(self):
        """This Method draws a scatter plot"""
        pass


obj = example()
# print(obj.get_tail())
print(obj.get_info())
print(obj.data.dtypes)
print(obj.data.describe())
print(obj.dropnullvalues())
row = len(obj.data)
col = len(obj.data.columns)
print(row, col)

# For this plot we need a customized data set.
# Use index of the data frame for selecticing specific columns.
obj2 = obj.data.iloc[1:, :]
obj2.plot.hist()

# Show a histogram
obj.draw_hist()
plt.show()  # Very important, otherwise no plot will show up and stay
