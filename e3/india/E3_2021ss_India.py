import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
import requests
# TODO import module for requests


class example:

    def __init__(self):
        self.data = self.read("e3\india\AB_NYC_2019.csv")
        self.url = "https://github.com/hka-mmv/dscb230-exercise/blob/main/e1/lecturer/AB_NYC_2019.csv.zip"    

    # --------------- GET THE DATA ---------------

    def fetch(self, url):
        """This Method fetches a dataset from a given url"""
        
        # NOTE: Fetching a HTTP request usually needs "try except"!
        try:
            r = requests.get(url = url, timeout=10)
            dataset=pd.read_json(r.json())
            # TODO Get the dataset via using method requests to get URL
        except requests.exceptions.Timeout:
            # Maybe set up for a retry, or continue in a retry loop
            print("Timeout of the request")
        except requests.exceptions.TooManyRedirects:
            # Tell the user their URL was bad and try a different one
            print("Your URL was bad. Please try a different one.")
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)
        return dataset

    def read(self, filename:str):
        """This method reads a given file

        It can import any file extension like json, csv, etc.
        """
        assert(filename.endswith('.csv'))

        dataf = pd.read_csv(filename)

        #v1
        #filenames=filename.split('/')

        # with (filenames, 'r') as data:
        #      dataf = pd.DataFrame(data)

        #v2
        # data = open(filename, 'r')
        # data = data.read()

        # TODO Aufgabe 1
        
        #assert(filename.endswith('.'))
        
        return dataf

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

    def get_tail(self,limit=10):
        """This Method reads the tail out of the data"""
        return self.data.tail(limit)

    def get_info(self, verbose=True):
        """This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage."""
        return self.data.info()

    def get_shape(self):
        """Return a tuple representing the dimensionality of the DataFrame."""
        return self.data.shape

    def get_value(self, key):
        """This Method returns every value for a given key"""
        return self.data[key]

    def get_type(self):
        """This Method returns dtypes of the DataFrame"""
        return self.data.dtypes

    def get_null(self):
        """This Method detect missing values """
        return self.data.isnull()

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
        g = sns.FacetGrid(self.data, col='neighbourhood_group')
        return g.map(plt.scatter, 'price', 'number_of_reviews')

    def draw_scatter(self):
        """This Method draws a scatter plot"""
        self.data.plot.scatter(x=self.data["longitude"], y=self.data["latitude"])



obj = example()
# TODO Run you tested implementation on the dataset.

# For this plot we need a customized data set.
# Use index of the data frame for selecticing specific columns.
obj2 = obj.data.iloc[1:, :]
obj2.plot.hist()

# Show a histogram
obj.draw_hist()
plt.show()  # Very important, otherwise no plot will show up and stay
