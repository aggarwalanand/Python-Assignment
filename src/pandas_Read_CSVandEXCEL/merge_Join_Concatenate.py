import pandas as pd

df1 = pd.read_csv('6_concatenate_df1.csv')
df2 = pd.read_csv('6_concatenate_df2.csv')
df3 = pd.read_csv('6_concatenate_df3.csv')
print("ORIGINAL VALUE DF1")
print(df1)
print("\nORIGINAL VALUE DF2")
print(df2)
print("\nORIGINAL VALUE DF3")
print(df3)

print("\nCONCAT DF1, DF2, DF3")
print(pd.concat([df1, df2, df3]))

print("\nCONCAT DF1, DF2, DF3 BASED ON AXIS")
print(pd.concat([df1, df2, df3], axis=1))

# Merge is like Equi Joins of SQL. Here it adds the columns. No need to specify Index
left = pd.read_csv('6_merge_df1.csv')
right = pd.read_csv('6_merge_df2.csv')

print("\nORIGINAL VALUE LEFT")
print(left)
print("\nORIGINAL VALUE RIGHT")
print(right)

print("\nMERGE DATA - SHOW ALL VALUES OF LEFT TABLE")
print(pd.merge(left, right, how='left', on='Cust_ID'))

print("\nMERGE DATA - SHOW ALL VALUES OF RIGHT TABLE")
print(pd.merge(left, right, how='right', on='Cust_ID'))

# # Like Non-equi joins of SQL. Index needs to be specified in Joins.
left.set_index('Cust_ID', inplace=True)
right.set_index('Cust_ID', inplace=True)

print("\nJOIN DATA")
print(left.join(right))

print("\nJOIN DATA WITH HOW")
print(left.join(right, how='left'))
