import pandas as pd

df = pd.DataFrame({'Animal': ['Falcon', 'Falcon', 'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})
print("ORIGINAL VALUE")
print(df)

print("\nGROUP BY")
print(df.groupby('Animal'))  # Does not return any meaningful value. Just an address from the memory

arrays = [['Falcon', 'Falcon', 'Parrot', 'Parrot'], ['Captive', 'Wild', 'Captive', 'Wild']]
index = pd.MultiIndex.from_arrays(arrays, names=('Animal', 'Type'))
df = pd.DataFrame({'Max Speed': [390., 350., 30., 20.]}, index=index)

print("\nORIGINAL VALUE")
print(df)

print("\nMEAN ON GROUP BY")
print(df.groupby('Animal').mean())

print("\nMIN ON GROUP BY")
print(df.groupby('Animal').min())

print("\nMAX ON GROUP BY")
print(df.groupby('Animal').max())

print("\nCOUNT ON GROUP BY")
print(df.groupby('Animal').count())

print("\nDESCRIBE ON GROUP BY")
print(df.groupby('Animal').describe())

print("\nTRANSPOSE ON GROUP BY")
print(df.groupby('Animal').describe().transpose())

print("\nTRANSPOSE ON GROUP BY FOR A PARTICULAR VALUE")
print(df.groupby('Animal').describe().transpose()['Falcon'])

print("\nMEAN ON GROUP BY LEVEL 0")
print(df.groupby(level=0).mean())

print("\nMEAN ON GROUP BY LEVEL TYPE")
print(df.groupby(level="Type").mean())
