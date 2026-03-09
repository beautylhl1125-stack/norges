import pandas as pd
from pdb import run
df = pd.read_csv("norges_data/equity.csv",sep=';')
df['Ownership'] = df['Ownership'].str.replace('%', '').astype(float)
print(df.head())
top_countries = df.groupby('Country')['Market Value(USD)'].sum().nlargest(10)
print(top_countries)
industry_analysis = df.groupby('Industry')['Market Value(USD)'].sum().sort_values(ascending=False)
top_companies = df.nlargest(10, 'Market Value(USD)')[['Name', 'Country', 'Market Value(USD)']]



