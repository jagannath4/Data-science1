import pandas as pd
import numpy as np

df = pd.read_csv('BL-Flickr-Images-Book.csv')

print("Original DataFrame:")
print(df.head())

irrelevant_columns = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Contributors', 'Issuance type', 'Shelfmarks']
df.drop(columns=irrelevant_columns, inplace=True)

df.set_index('Identifier', inplace=True)

df['Date of Publication'] = df['Date of Publication'].str.extract(r'^(\d{4})', expand=False)

df['Place of Publication'] = np.where(df['Place of Publication'].str.contains('London'), 'London',
df['Place of Publication'].str.replace('-', ' '))
print("\nCleaned DataFrame:")
print(df.head())


