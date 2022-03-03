import numpy as np
import pandas as pd

print("\nMISSING DATA IN DATAFRAME")
missingDataDF = pd.DataFrame({'A': [1, 2, np.nan],
                              'B': [5, np.nan, np.nan],
                              'C': [6, 7, 8]})
print(missingDataDF)
# The default value for axis param is 0
print("\nMISSING DATA IN DATAFRAME DROPNA ROWS")
print(missingDataDF.dropna())

# Removes the columns that have Nan Value
print("\nMISSING DATA IN DATAFRAME DROPNA COLUMNS")
print(missingDataDF.dropna(axis=1))

# Remove the row that the specified number of non NaN values
print("\nMISSING DATA IN DATAFRAME THRESH")
print(missingDataDF.dropna(thresh=2))

print("\nMISSING DATA IN DATAFRAME REPLACE NaN VALUES")
print(missingDataDF.fillna(value=2))
