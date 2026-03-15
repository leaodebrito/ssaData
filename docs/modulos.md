# Módulos

## app.py

Ponto de entrada da aplicação. Configura a página, renderiza a sidebar com o menu de navegação e direciona para o módulo correto conforme a seleção do usuário.

**Responsabilidades:**
- Configuração global (`st.set_page_config`)
- Menu de navegação via `st.sidebar.selectbox`
- Roteamento entre páginas

---

## pagina_inicial.py

Exibe a página de apresentação da plataforma.

**Função principal:** `mostrar()`

Renderiza o título, subtítulo e texto descritivo sobre os objetivos da SSA Dados.

---

## dados_sociodemograficos.py

Página de análise sócio-demográfica dos bairros de Salvador.

**Função principal:** `mostrar()`

**Fluxo:**
1. Carrega `dados/dataset_salvador.csv`
2. Permite seleção de múltiplos bairros via `st.multiselect`
3. Calcula métricas derivadas:
   - `Área (ha)` — convertida de m²
   - `DENSIDADE POPULACIONAL` — hab/ha
   - `Domicilios por hectare`
4. Exibe:
   - Mapa com localização dos bairros (`st.map`)
   - Gráfico de barras: população por bairro
   - Gráfico de barras: densidade populacional
   - Gráfico de barras: caracterização étnica (%)
   - Gráfico de barras: distribuição etária (%)
   - Tabela com os dados brutos para download

---

## equip_urbanos.py

Página de visualização de equipamentos urbanos georreferenciados.

**Função principal:** `mostrar()`

**Fluxo:**
1. Carrega `dados/dataset_equip_urb_salvador.csv`
2. Permite seleção de tipos de equipamento via `st.multiselect`
3. Exibe mapa com os equipamentos filtrados (`st.map`) com cor por tipo
4. Exibe tabela com os dados dos equipamentos selecionados

---

## funcoes_elementos_interface/graficos.py

Módulo de funções auxiliares de visualização. Usado por `dados_sociodemograficos.py`.

### Funções

#### `plot_barra_linha(df, feature_bairro_x, feature_area_y, feature_densidade_y, label_y)`

Gráfico de barras com sobreposição de linha no segundo eixo Y.

- Barras: área dos bairros (eixo Y esquerdo)
- Linha: densidade populacional (eixo Y direito)
- Retorna: `matplotlib.figure.Figure`

#### `plot_barra_empilhada(df, bairro_coluna, feature, cores)`

Gráfico de barras empilhadas com percentuais anotados.

- Ideal para caracterização étnica ou etária
- Parâmetros:
  - `df`: DataFrame com os dados
  - `bairro_coluna`: coluna com nomes dos bairros
  - `feature`: lista de colunas a empilhar
  - `cores`: lista opcional de cores hexadecimais
- Retorna: `matplotlib.figure.Figure`

#### `histograma(df, title, xlabel)`

Histograma interativo com 50 bins via Plotly.

- Retorna: `plotly.graph_objects.Figure`

#### `plotar_grafico_linhas_long(df, periodo, bairro_col, preco_col, titulo)`

Gráfico de linhas temporais por bairro, com interpolação linear para valores ausentes.

- Parâmetros:
  - `periodo`: coluna de data (convertida automaticamente para datetime)
  - `bairro_col`: coluna de agrupamento
  - `preco_col`: coluna de valores (eixo Y)
- Retorna: `plotly.graph_objects.Figure`

---

## dados/juntar_dataset.py

Script utilitário para consolidar os CSVs individuais de equipamentos em um único dataset.

**O que faz:**
1. Lê os 9 arquivos-fonte de equipamentos
2. Adiciona colunas `Tipo` e `cor` a cada DataFrame
3. Concatena todos em um único DataFrame
4. Extrai `latitude` e `longitude` da coluna `WKT`
5. Remove duplicatas
6. Salva em `dados/dataset_equip_urb_salvador.csv`

**Uso:**
```bash
python dados/juntar_dataset.py
```
