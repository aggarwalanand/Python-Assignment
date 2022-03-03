import pandas as pd

print("\nDATAFRAMES\n")
print("\nNEWS_SALES.XLSX")
df = pd.read_excel("3_NEWS_Sales.xlsx", sheet_name="NEWS")
print(df)

# inplace = True => the dataframe will be replaced
# Change Index of the data frame
df.set_index('Month', inplace=True)
print(df)

print("\nNEWS_SALES.XLSX - COLUMN")
print(df['North'])

# Two sq brackets as we are passing list as subscript
print("\nNEWS_SALES.XLSX - COLUMNS")
print(df[['North', 'South']])

# Here Jan has now become an Index, so loc is used
print("\nNEWS_SALES.XLSX - INDEX")
print(df.loc['Jan'])

print("\nNEWS_SALES.XLSX - TYPE")
print(type(df['North']))
print(type(df.loc['Jan']))

print("\nCONCATENATE TWO COLS")
df['North_South'] = df['North'] + df['South']  # Here it will add the values of North and South cols. If operator
print(df)

# Axis - 1 => Column
# Axis - 0 => Row
# inplace = True => the dataframe will be replaced
# First param is the header
print("\nDROP COL")
df.drop('North_South', axis=1, inplace=True)
print(df)

# Axis - 1 => Column
# Axis - 0 => Row
# inplace = True => the dataframe will be replaced
# First param is the index
print("\nDROP ROW")
df.drop('Jan', axis=0)
print(df)

print("\nFetch based on integer Index")
print(df.iloc[2])

print("\nFetch value for a particular cell")
print(df.loc['Mar', 'South'])

print("\nFetch value for multiple Index")
print(df.loc[['Feb', 'Mar'], ['East', 'West']])

print("\nCONDITIONAL SELECTION")
# Gives the boolean
print(df > 5000)

# Gives the values based on condition passed
print("\n")
print(df[df > 5000])
print("\n")
print(df[df['North'] > 8000][['East', 'West']])
print("\n")
print(df[(df['North'] > 8000) & (df['East'] > 5000) & df['West'] > 3000])
print("\n")

# inplace = True => the dataframe will be replaced
df.reset_index()
print(df)

print("\nINDEX NAMES")
print(df.index.names)
