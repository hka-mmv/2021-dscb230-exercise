import pandas as pd

path_prefix = "dscb230-exercise/wesm-pydatabook/pydata-book/datasets/babynames/"
names1880 = pd.read_csv(path_prefix + 'yob1880.txt',
                        names=['name', 'sex', 'births'])

print(names1880.groupby('sex').births.sum())

years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = path_prefix + 'yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)

# Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index=True)

print(names)
