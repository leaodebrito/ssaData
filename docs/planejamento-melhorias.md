# Planejamento de Melhorias

## Visão Geral

Este documento organiza as melhorias identificadas no projeto SSA Dados em fases priorizadas, agrupando itens por tema e complexidade.

---

## Fase 1 — Correções e Ajustes Imediatos

> Baixo esforço, alto impacto. Correções de inconsistências existentes.

### 1.1 Incluir Drogarias no dataset de equipamentos
- **Problema:** o arquivo `Equipamentos urbanos salvador- Drograria.csv` existe mas não é carregado em `juntar_dataset.py`
- **Ação:** adicionar o arquivo ao script e regenerar o `dataset_equip_urb_salvador.csv`
- **Arquivo:** `dados/juntar_dataset.py`

### 1.2 Tratar seleção vazia na página de Equipamentos Urbanos
- **Problema:** se nenhum tipo de equipamento for selecionado, o mapa exibe sem feedback
- **Ação:** adicionar mensagem orientando o usuário, similar ao tratamento já feito em `dados_sociodemograficos.py`
- **Arquivo:** `equip_urbanos.py`

### 1.3 Corrigir caminhos de arquivo
- **Problema:** CSVs são referenciados com caminhos relativos, podendo falhar conforme o diretório de execução
- **Ação:** usar `pathlib.Path(__file__).parent` para construir caminhos absolutos
- **Arquivos:** `dados_sociodemograficos.py`, `equip_urbanos.py`, `dados/juntar_dataset.py`

### 1.4 Adicionar `__init__.py` ao pacote de funções
- **Problema:** `funcoes_elementos_interface/` não possui `__init__.py`, não sendo formalmente um pacote Python
- **Ação:** criar o arquivo vazio
- **Arquivo:** `funcoes_elementos_interface/__init__.py`

---

## Fase 2 — Melhorias de Interface e Usabilidade

> Melhora a experiência do usuário sem alterar os dados.

### 2.1 Adicionar cards de métricas resumidas
- **Descrição:** exibir indicadores rápidos antes dos gráficos (ex: total de habitantes, área total, densidade média) usando `st.metric`
- **Arquivo:** `dados_sociodemograficos.py`

### 2.2 Filtro de bairro na página de Equipamentos Urbanos
- **Descrição:** permitir que o usuário filtre os equipamentos também por bairro, cruzando com o dataset sócio-demográfico via coordenadas ou nome
- **Arquivo:** `equip_urbanos.py`

### 2.3 Utilizar as funções de `graficos.py`
- **Descrição:** a página de dados sócio-demográficos usa `st.bar_chart` diretamente, ignorando as funções mais ricas já implementadas (`plot_barra_empilhada`, `plot_barra_linha`)
- **Ação:** substituir os gráficos simples pelas funções do módulo de visualização
- **Arquivos:** `dados_sociodemograficos.py`, `funcoes_elementos_interface/graficos.py`

### 2.4 Melhorar legibilidade dos gráficos
- **Descrição:** adicionar rótulos, tooltips e títulos mais descritivos nos gráficos existentes
- **Arquivo:** `funcoes_elementos_interface/graficos.py`

---

## Fase 3 — Atualização e Expansão dos Dados

> Maior esforço, mas aumenta significativamente o valor da plataforma.

### 3.1 Atualizar dados demográficos para o Censo 2022
- **Descrição:** o dataset atual usa o Censo 2010. O IBGE disponibilizou os dados do Censo 2022
- **Fonte:** [IBGE — Censo 2022](https://www.ibge.gov.br/estatisticas/sociais/populacao/22827-censo-demografico-2022.html)
- **Arquivos:** `dados/dataset_salvador.csv`, `dados_sociodemograficos.py`

### 3.2 Ampliar categorias de equipamentos urbanos
- **Descrição:** incluir novos tipos de equipamentos relevantes para análise urbana:
  - Unidades Básicas de Saúde (UBS)
  - Escolas públicas municipais e estaduais
  - CRAS (Centro de Referência de Assistência Social)
  - Pontos de ônibus e terminais de transporte público
- **Arquivo:** `dados/juntar_dataset.py` e novos CSVs em `dados/`

---

## Fase 4 — Qualidade e Infraestrutura

> Melhora a manutenibilidade e confiabilidade do projeto.

### 4.1 Adicionar testes automatizados
- **Descrição:** criar testes para as funções de `graficos.py` e para o script `juntar_dataset.py`
- **Ferramenta sugerida:** `pytest`
- **Local:** criar pasta `tests/`

### 4.2 Documentar deploy
- **Descrição:** adicionar instruções para publicar a aplicação no [Streamlit Community Cloud](https://streamlit.io/cloud)
- **Arquivo:** `docs/deploy.md`

---

## Resumo de Prioridades

| # | Melhoria | Fase | Esforço | Impacto |
|---|---|---|---|---|
| 1 | Incluir Drogarias no dataset | 1 | Baixo | Médio |
| 2 | Tratar seleção vazia (Equipamentos) | 1 | Baixo | Alto |
| 3 | Corrigir caminhos de arquivo | 1 | Baixo | Alto |
| 4 | Adicionar `__init__.py` | 1 | Baixo | Baixo |
| 5 | Cards de métricas resumidas | 2 | Médio | Alto |
| 6 | Filtro de bairro em Equipamentos | 2 | Médio | Alto |
| 7 | Usar funções de `graficos.py` | 2 | Médio | Médio |
| 8 | Melhorar legibilidade dos gráficos | 2 | Baixo | Médio |
| 9 | Atualizar para Censo 2022 | 3 | Alto | Alto |
| 10 | Ampliar equipamentos urbanos | 3 | Alto | Alto |
| 11 | Testes automatizados | 4 | Alto | Médio |
| 12 | Documentar deploy | 4 | Baixo | Médio |
