import pandas as pd
import numpy as np


file1 = 'dados/Equipamentos urbanos salvador- Campos de futebol.csv'
file2 = 'dados/Equipamentos urbanos salvador- Centros comunitários.csv'
file3 = 'dados/Equipamentos urbanos salvador- Centros religiosos.csv'
file4 = 'dados/Equipamentos urbanos salvador- Padaria.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
df4 = pd.read_csv(file4)


df1['Tipo'] = 'Campo de futebol'
df2['Tipo'] = 'Centro comunitário'
df3['Tipo'] = 'Centro religioso'
df4['Tipo'] = 'Padaria'


df1['cor'] = '#FF5733'
df2['cor'] = '#33FF57'
df3['cor'] = '#3357FF'
df4['cor'] = '#FF5733'



df = pd.concat([df1, df2, df3, df4])

df[['longitude', 'latitude']] = df['WKT'].str.extract(r'POINT \(([-\d.]+) ([-\d.]+)\)')

# Convertendo para float
df['longitude'] = df['longitude'].astype(float)
df['latitude'] = df['latitude'].astype(float)

print(df)


df.to_csv('dados/dataset_equip_urb_salvador.csv', index=False)