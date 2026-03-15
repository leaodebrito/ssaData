# Dados

## dataset_salvador.csv

Dados sócio-demográficos dos bairros de Salvador, baseados principalmente no **Censo 2010** do IBGE.

### Colunas

| Coluna | Descrição |
|---|---|
| `BAIRRO` | Nome do bairro |
| `População segundo o Censo de 2010` | Total de habitantes |
| `Densidade Populacional Bruta hab/ha` | Habitantes por hectare |
| `Latitude` / `Longitude` | Coordenadas geográficas do bairro |
| `área` | Área do bairro em m² |
| `Área verde` | Área verde em m² |
| `% Branca`, `% Preta`, `% Amarela`, `% Parda`, `% Indígena` | Caracterização étnica (%) |
| `0 a 4 anos` ... `acima de 65 anos` | Distribuição etária por faixa (%) |
| `População acima de 15 anos não alfabetizada (%)` | Taxa de analfabetismo |
| `Total de domicílios` | Quantidade total de domicílios |
| `Total de domicílios próprios` / `alugados` / `cedidos` | Tipo de posse do domicílio (%) |
| `Rendimento médio` | Renda média mensal (R$) — Censo 2010 |
| `Rendimento médio atualizado` | Renda média corrigida pela inflação |
| `Prefeitura bairro` | Código da prefeitura de bairro |
| `Acumulado de chuva 2019–2023 (mm)` | Precipitação acumulada anual por ano |

---

## dataset_equip_urb_salvador.csv

Dataset consolidado de equipamentos urbanos georreferenciados em Salvador.

### Colunas

| Coluna | Descrição |
|---|---|
| `WKT` | Geometria no formato WKT (`POINT (lon lat)`) |
| `nome` | Nome do equipamento |
| `descrição` | Descrição adicional (quando disponível) |
| `Tipo` | Categoria do equipamento |
| `cor` | Cor hexadecimal para visualização no mapa |
| `longitude` / `latitude` | Coordenadas geográficas extraídas do WKT |

### Tipos de Equipamentos

| Tipo | Cor |
|---|---|
| Campo de futebol | `#EF1325` |
| Centro comunitário | `#7F3483` |
| Centro religioso | `#28B1C3` |
| Padaria | `#107F75` |
| Centro de formação e educação | `#EC2505` |
| Hospital | `#F12F71` |
| Mercado | `#31838F` |
| Praça | `#6FD2CB` |
| Shopping | `#FEDB91` |

---

## Arquivos-fonte dos Equipamentos

Os equipamentos foram coletados por categoria em arquivos CSV separados, localizados na pasta `dados/`. O script `juntar_dataset.py` os consolida no `dataset_equip_urb_salvador.csv`.

| Arquivo | Tipo |
|---|---|
| `Equipamentos urbanos salvador- Campos de futebol.csv` | Campo de futebol |
| `Equipamentos urbanos salvador- Centro de formação e educacao.csv` | Centro de formação e educação |
| `Equipamentos urbanos salvador- Centros comunitários.csv` | Centro comunitário |
| `Equipamentos urbanos salvador- Centros religiosos.csv` | Centro religioso |
| `Equipamentos urbanos salvador- Drograria.csv` | Drogaria |
| `Equipamentos urbanos salvador- Hospital.csv` | Hospital |
| `Equipamentos urbanos salvador- Mercado.csv` | Mercado |
| `Equipamentos urbanos salvador- Padaria.csv` | Padaria |
| `Equipamentos urbanos salvador- Praça.csv` | Praça |
| `Equipamentos urbanos salvador- Shopping.csv` | Shopping |
