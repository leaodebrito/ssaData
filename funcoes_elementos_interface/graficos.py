# 
# Funções de visualização de dados
#
# Autor: Bruno Leão
#


# Importando bibliotecas
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


import pandas as pd
import numpy as np


def plot_barra_linha(df, feature_bairro_x, feature_area_y, feature_densidade_y, label_y = 'Área (ha)'):
    """
    Função para gerar gráfico de barras com sobreposição em linha de densidade populacional
    """

        # Criação do gráfico com dois eixos y
    fig, ax1 = plt.subplots(figsize=(12, 8))

    # Gráfico de barras para área
    sns.barplot(x=feature_bairro_x, y=feature_area_y, data=df, ax=ax1, color= "#000066")
    ax1.set_xlabel("")
    ax1.set_ylabel(label_y)
    ax1.tick_params(axis='y')

    # Segundo eixo y para a densidade populacional
    ax2 = ax1.twinx()
    ax2.plot(df[feature_bairro_x], df[feature_densidade_y], color='red', marker='o', label='Densidade Populacional')
    ax2.set_ylabel("Densidade Populacional (hab/ha)")
    ax2.tick_params(axis='y')

    # Títulos e legendas
    #ax1.set_title("Área dos Bairros e Densidade Populacional")
    fig.tight_layout()  # Para melhor ajuste

    return fig


def plot_barra_empilhada(df, bairro_coluna, feature, cores=None):
    """
    Função para gerar gráfico de barras empilhadas com a caracterização etária dos bairros.

    Parâmetros:
    - df: DataFrame com os dados.
    - bairro_coluna: Nome da coluna que contém os bairros.
    - faixa_etaria_colunas: Lista com os nomes das colunas de cada faixa etária.
    - cores: Lista de cores para cada faixa etária (opcional).

    Retorna:
    - fig: Objeto da figura do Matplotlib com o gráfico gerado.
    """
    # Configuração do gráfico
    fig, ax = plt.subplots(figsize=(12, 8))
    bottom = [0] * len(df)

    # Definindo cores padrão, caso não sejam fornecidas
    if cores is None:
        cores = ["#e0e0ff", "#b3b3ff", "#8080ff", "#4d4dff", "#1a1aff", "#0000cc", "#000066"]

    # Criando barras empilhadas para cada faixa etária
    for i, coluna in enumerate(feature):
        valores = df[coluna]
        ax.bar(df[bairro_coluna], df[coluna], bottom=bottom, label=coluna, color=cores[i % len(cores)])

        for j, valor in enumerate(valores):
            ax.text(j, bottom[j] + valor / 2, f"{valor:.2f}%", ha="center", va="center", color="white", fontsize=8)


        # Atualizando a base para a próxima faixa etária
        bottom = [i + j for i, j in zip(bottom, df[coluna])]

    # Ajustes de rótulos e título
    ax.set_ylabel("Percentual")
    #ax.set_xlabel("Bairro")
    ax.legend(title="Faixa Etária", bbox_to_anchor=(1.05, 1), loc='upper left')

    # Ajuste de layout
    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig



def histograma(df, title=None, xlabel=None):
    
    fig = px.histogram(df, x=xlabel, nbins=50, title=title)

    return fig


def plotar_grafico_linhas_long(df, periodo='data_anuncio', bairro_col='Bairro', preco_col='preco_unitario',titulo=''):
    """
    Plota um gráfico de linhas contínuas a partir de um DataFrame no formato longo.

    Parâmetros:
        df (pd.DataFrame): DataFrame em formato longo com colunas para período, bairro e preço.
        periodo (str): Nome da coluna que representa o período (eixo x do gráfico).
        bairro_col (str): Nome da coluna que representa os bairros.
        preco_col (str): Nome da coluna que representa os preços.

    Retorno:
        None: Exibe o gráfico interativo.
    """
    # Converter o período para datetime, se necessário
    if not pd.api.types.is_datetime64_any_dtype(df[periodo]):
        df[periodo] = pd.to_datetime(df[periodo])

    # Ordenar os dados por período e bairro
    df_sorted = df.sort_values(by=[periodo, bairro_col]).reset_index(drop=True)

    # Preencher valores ausentes com interpolação (por bairro)
    df_sorted[preco_col] = df_sorted.groupby(bairro_col)[preco_col].transform(lambda x: x.interpolate(method='linear'))

    # Criar o gráfico de linhas
    fig = px.line(
        df_sorted,
        x=periodo,
        y=preco_col,
        color=bairro_col,
        title=titulo,
        labels={preco_col: 'Preço Médio', periodo: 'Período', bairro_col: 'Bairros'}
    )

    # Melhorar o layout
    fig.update_layout(
        xaxis_title='Período',
        yaxis_title='Média de Preço',
        legend_title='Bairros',
        template='plotly_white',
        hovermode='x unified'
    )

    return fig