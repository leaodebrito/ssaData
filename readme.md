# SSA Dados

Plataforma interativa para análise e visualização de dados urbanos de Salvador (BA), desenvolvida com foco no apoio a estudantes de Arquitetura e Urbanismo.

## Sobre

A SSA Dados permite explorar Salvador através de dados sociodemográficos e de equipamentos urbanos, oferecendo embasamento técnico para propostas arquitetônicas e intervenções urbanas.

## Funcionalidades

### Dados Sócio-Demográficos
- Seleção de bairros para análise comparativa
- Mapa de localização dos bairros selecionados
- Gráficos de população e densidade populacional
- Caracterização étnica e etária por bairro
- Exportação dos dados filtrados

### Equipamentos Urbanos
- Filtragem por tipo de equipamento urbano
- Visualização georreferenciada no mapa
- Tabela com dados detalhados dos equipamentos

## Tecnologias

- [Streamlit](https://streamlit.io/) — interface web
- [Pandas](https://pandas.pydata.org/) — manipulação de dados
- [PyDeck](https://deckgl.readthedocs.io/) — visualização de mapas
- [Plotly](https://plotly.com/) / [Matplotlib](https://matplotlib.org/) / [Seaborn](https://seaborn.pydata.org/) — gráficos

## Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/leaodebrito/ssaData.git
   cd ssaData
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

## Dados

Os datasets utilizados estão na pasta `dados/`:
- `dataset_salvador.csv` — dados sociodemográficos dos bairros (Censo 2010)
- `dataset_equip_urb_salvador.csv` — equipamentos urbanos georreferenciados

## Licença

Este projeto está licenciado sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — use, adapte e compartilhe com atribuição ao autor.

## Autor

Bruno Leão de Brito
