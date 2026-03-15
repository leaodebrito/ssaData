import pandas as pd
import numpy as np
from pathlib import Path

dados_dir = Path(__file__).parent


file1  = dados_dir / 'Equipamentos urbanos salvador- Campos de futebol.csv'
file2  = dados_dir / 'Equipamentos urbanos salvador- Centros comunitários.csv'
file3  = dados_dir / 'Equipamentos urbanos salvador- Centros religiosos.csv'
file4  = dados_dir / 'Equipamentos urbanos salvador- Padaria.csv'
file5  = dados_dir / 'Equipamentos urbanos salvador- Centro de formação e educacao.csv'
file6  = dados_dir / 'Equipamentos urbanos salvador- Hospital.csv'
file7  = dados_dir / 'Equipamentos urbanos salvador- Mercado.csv'
file8  = dados_dir / 'Equipamentos urbanos salvador- Praça.csv'
file9  = dados_dir / 'Equipamentos urbanos salvador- Shopping.csv'
file10 = dados_dir / 'Equipamentos urbanos salvador- Drograria.csv'


df1  = pd.read_csv(file1)
df2  = pd.read_csv(file2)
df3  = pd.read_csv(file3)
df4  = pd.read_csv(file4)
df5  = pd.read_csv(file5)
df6  = pd.read_csv(file6)
df7  = pd.read_csv(file7)
df8  = pd.read_csv(file8)
df9  = pd.read_csv(file9)
df10 = pd.read_csv(file10)


df1['Tipo']  = 'Campo de futebol'
df2['Tipo']  = 'Centro comunitário'
df3['Tipo']  = 'Centro religioso'
df4['Tipo']  = 'Padaria'
df5['Tipo']  = 'Centro de formação e educação'
df6['Tipo']  = 'Hospital'
df7['Tipo']  = 'Mercado'
df8['Tipo']  = 'Praça'
df9['Tipo']  = 'Shopping'
df10['Tipo'] = 'Drogaria'


df1['cor']  = '#EF1325'
df2['cor']  = '#7F3483'
df3['cor']  = '#28B1C3'
df4['cor']  = '#107F75'
df5['cor']  = '#EC2505'
df6['cor']  = '#F12F71'
df7['cor']  = '#31838F'
df8['cor']  = '#6FD2CB'
df9['cor']  = '#FEDB91'
df10['cor'] = '#FF8C00'


df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10])

df[['longitude', 'latitude']] = df['WKT'].str.extract(r'POINT \(([-\d.]+) ([-\d.]+)\)')

df['longitude'] = df['longitude'].astype(float)
df['latitude'] = df['latitude'].astype(float)

df = df.drop_duplicates()

output = dados_dir / 'dataset_equip_urb_salvador.csv'
df.to_csv(output, index=False)
print(f"Dataset gerado: {output} ({len(df)} registros)")
