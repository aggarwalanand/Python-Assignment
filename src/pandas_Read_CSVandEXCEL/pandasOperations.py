import pandas as pd

df = pd.read_csv('1_Sales.csv')

print("\nORIGINAL VALUE")
print(df)

print("\nDESCRIBE")
print(df.describe())

print("\nUNIQUE VALUES")
print(df['SalesRep'].unique())

print("\nNUMBER OF UNIQUE VALUES")
print(df['SalesRep'].nunique())

print("\nNUMBER OF TIMES EACH UNIQUE VALUE OCCURS")
print(df['SalesRep'].value_counts())

print("\nSELECT VALUES BASED ON THE CONDITIONS SPECIFIED")
print(df[(df['Units Sold'] > 100) & (df['Month'] == 'Jan')])

print("\nAPPLYING FUNCTIONS")


def twice(x):
    return x * 2


print("\nAPPLYING FUNCTION TWICE")
print(df['Units Sold'].apply(twice))

print("\nAPPLYING FUNCTION LEN")
print(df['SalesRep'].apply(len))


def compute_aup(cols):
    return cols[0] / cols[1]


# axis=1 => the functions will be applied to each row
print("\nAPPLYING FUNCTION COMPUTE_AUP ON EACH ROW")
# This line creates a new column in DATAFRAME
df['AUP'] = df[['Sales', 'Units Sold']].apply(compute_aup, axis=1)
print(df['AUP'])

print("\nNEW VALUE WITH AUP COLUMN ADDED")
print(df.head())

print("\nPERMANENTLY DELETE A COLUMN")
del df['AUP']
print(df.head())

print("\nPRINT THE COLUMNS")
print(df.columns)

print("\nPRINT THE INDEX")
print(df.index)

print("\nPRINT THE WHETHER VALUE IS NULL EACH CELL")
print(df.isnull())

print("\nPRINT THE NUMBER OF NULL VALUES IN EACH COLUMN")
print(df.isnull().sum())

print("\nSORT VALUES ASCENDING")
print(df.sort_values('Sales'))

print("\nSORT VALUES DESCENDING")
print(df.sort_values(by='Sales', ascending=False))

# Pivot is used to summarize a table based on the parameter that we want
print("\nPIVOT A TABLE")
print(df.pivot_table(values='Sales', index=['Month'], columns=['SalesRep']))

print(df.isnull())

'''
Links to see the code to print only the rows that have NaN or Null value 
https://datatofish.com/rows-with-nan-pandas-dataframe/
https://www.kite.com/python/answers/how-to-find-the-indices-of-rows-in-a-pandas-dataframe-containing-nan-values-in-python
'''
print("\nONLY PRINT THE VALUES THAT HAVE ONE NaN or NULL")
rows_with_nan = [index for index, row in df.iterrows() if row.isnull().any()]
print(rows_with_nan)
print(df.loc[rows_with_nan])
print(df[df.isna().any(axis=1)])
print(df[df.isnull().any(axis=1)])
