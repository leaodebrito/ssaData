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


def plot_barra_linha(df, feature_bairro_x, feature_area_y, feature_densidade_y, label_y='Área (ha)'):
    """
    Gráfico de barras (área) com sobreposição de linha (densidade populacional) em segundo eixo Y.

    Parâmetros:
    - df: DataFrame com os dados.
    - feature_bairro_x: coluna com nomes dos bairros (eixo X).
    - feature_area_y: coluna de área para as barras (eixo Y esquerdo).
    - feature_densidade_y: coluna de densidade para a linha (eixo Y direito).
    - label_y: rótulo do eixo Y esquerdo.

    Retorna:
    - fig: objeto Figure do Matplotlib.
    """
    fig, ax1 = plt.subplots(figsize=(12, 8))

    sns.barplot(x=feature_bairro_x, y=feature_area_y, data=df, ax=ax1, color="#000066", label=label_y)
    ax1.set_xlabel("Bairro", fontsize=11)
    ax1.set_ylabel(label_y, fontsize=11)
    ax1.tick_params(axis='x', rotation=45)
    ax1.tick_params(axis='y')

    ax2 = ax1.twinx()
    ax2.plot(df[feature_bairro_x], df[feature_densidade_y], color='red', marker='o',
             linewidth=2, markersize=6, label='Densidade Populacional (hab/ha)')
    ax2.set_ylabel("Densidade Populacional (hab/ha)", fontsize=11, color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

    fig.tight_layout()

    return fig


def plot_barra_empilhada(df, bairro_coluna, feature, cores=None):
    """
    Gráfico de barras empilhadas com percentuais anotados nas fatias.

    Parâmetros:
    - df: DataFrame com os dados.
    - bairro_coluna: coluna com nomes dos bairros.
    - feature: lista de colunas a empilhar (ex: faixas etárias ou grupos étnicos).
    - cores: lista opcional de cores hexadecimais.

    Retorna:
    - fig: objeto Figure do Matplotlib.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    bottom = [0] * len(df)

    if cores is None:
        cores = ["#e0e0ff", "#b3b3ff", "#8080ff", "#4d4dff", "#1a1aff", "#0000cc", "#000066"]

    for i, coluna in enumerate(feature):
        valores = df[coluna].tolist()
        ax.bar(df[bairro_coluna], df[coluna], bottom=bottom, label=coluna, color=cores[i % len(cores)])

        for j, valor in enumerate(valores):
            if valor > 3:
                ax.text(j, bottom[j] + valor / 2, f"{valor:.1f}%",
                        ha="center", va="center", color="white", fontsize=8, fontweight='bold')

        bottom = [b + v for b, v in zip(bottom, valores)]

    ax.set_ylabel("Percentual (%)", fontsize=11)
    ax.set_xlabel("Bairro", fontsize=11)
    ax.tick_params(axis='x', rotation=45)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)

    plt.tight_layout()

    return fig


def histograma(df, title=None, xlabel=None):
    """
    Histograma interativo com 50 bins via Plotly.

    Parâmetros:
    - df: DataFrame com os dados.
    - title: título do gráfico.
    - xlabel: coluna a ser usada no eixo X.

    Retorna:
    - fig: objeto Figure do Plotly.
    """
    fig = px.histogram(df, x=xlabel, nbins=50, title=title,
                       labels={xlabel: xlabel},
                       template='plotly_white')
    fig.update_layout(bargap=0.05)

    return fig


def plotar_grafico_linhas_long(df, periodo='data_anuncio', bairro_col='Bairro', preco_col='preco_unitario', titulo=''):
    """
    Gráfico de linhas temporais por bairro, com interpolação linear para valores ausentes.

    Parâmetros:
    - df: DataFrame em formato longo.
    - periodo: coluna de data (convertida automaticamente para datetime).
    - bairro_col: coluna de agrupamento por bairro.
    - preco_col: coluna de valores numéricos (eixo Y).
    - titulo: título do gráfico.

    Retorna:
    - fig: objeto Figure do Plotly.
    """
    if not pd.api.types.is_datetime64_any_dtype(df[periodo]):
        df[periodo] = pd.to_datetime(df[periodo])

    df_sorted = df.sort_values(by=[periodo, bairro_col]).reset_index(drop=True)

    df_sorted[preco_col] = df_sorted.groupby(bairro_col)[preco_col].transform(
        lambda x: x.interpolate(method='linear')
    )

    fig = px.line(
        df_sorted,
        x=periodo,
        y=preco_col,
        color=bairro_col,
        title=titulo,
        labels={preco_col: 'Preço Médio (R$)', periodo: 'Período', bairro_col: 'Bairro'},
        template='plotly_white'
    )

    fig.update_layout(
        xaxis_title='Período',
        yaxis_title='Preço Médio (R$)',
        legend_title='Bairros',
        hovermode='x unified'
    )

    return fig
