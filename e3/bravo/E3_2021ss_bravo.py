import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv

# TODO import module for requests
import requests


class example:

    def __init__(self):
        self.data = self.read("AB_NYC_2019(cleaned).csv")
        self.url = "https://github.com/hka-mmv/dscb230-exercise/blob/main/e1/lecturer/AB_NYC_2019.csv.zip"


    # --------------- GET THE DATA ---------------

    def fetch(self, url):
        """This Method fetches a dataset from a given url"""

        # NOTE: Fetching a HTTP request usually needs "try except"!
        try:
            # TODO Get the dataset via using method requests to get URL
            dataset = pd.read_csv(self.url)
            
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            print("Timeout")

        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            print("Fehlerhafte URL")

        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)

        return dataset


    def read(self, filename):
        """This method reads a given file

        It can important any file extension like json, csv, etc.
        """
        data = None
        # TODO Aufgabe 1
        # NOTE: Use "assert" if filename contains a dot for the extension (data not okay, data.csv okay)

        assert(filename == r'.\.csv')

        data = pd.read_csv(filename)
        
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
        """This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage."""
        return self.data.info()

    def get_shape(self):
        """Return a tuple representing the dimensionality of the DataFrame."""
        return self.data.shape

    def get_value(self, key):
        """This Method returns every value for a given key"""
        return self.data[key]

    # --------------- DATA PREPARATION ---------------

    # TODO
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
        # Frage: Welche Spalten?
        pass

    def draw_scatter(self):
        """This Method draws a scatter plot"""
        # Frage: Welche Spalten?
        pass


obj = example()
# TODO Run you tested implementation on the dataset.

# For this plot we need a customized data set.
# Use index of the data frame for selecticing specific columns.
obj2 = obj.data.iloc[1:, :]
obj2.plot.hist()

# Show a histogram
obj.draw_hist()
plt.show()  # Very important, otherwise no plot will show up and stay
