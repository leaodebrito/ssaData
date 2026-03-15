#
# Plataforma Build Up - Página de Dados Sócio-Demográficos
# Página de apresentação de dados da cidade de salvador
#
# Autor: Bruno Leão de Brito
#

# importar bibliotecas
import streamlit as st
import pandas as pd
import numpy as np

import funcoes_elementos_interface.graficos as graph
from pathlib import Path


def mostrar():
    st.title("Análise Sócio-Demográfica")
    st.write("Plataforma para análise de dados sócio-demográficos dos bairros de Salvador")

    # Carregar dados
    df = pd.read_csv(Path(__file__).parent / 'dados' / 'dataset_salvador.csv')

    # Selecionar bairro
    bairros = df['BAIRRO'].unique()
    bairro_selecionado = st.multiselect("Selecione os bairros", bairros)

    # filtragem de dados por bairro
    dados = df[df['BAIRRO'].isin(bairro_selecionado)].copy()

    dados['Área (ha)'] = dados['área'] / 10_000
    dados['DENSIDADE POPULACIONAL'] = dados['População segundo o Censo de 2010'] / dados['Área (ha)']
    dados['Domicilios por hectare'] = dados['Total de domicílios'] / dados['Área (ha)']

    # Exibir os dados dos bairros selecionados
    if not dados.empty:

        # Cards de métricas resumidas
        total_pop = int(dados['População segundo o Censo de 2010'].sum())
        area_total = dados['Área (ha)'].sum()
        densidade_media = dados['DENSIDADE POPULACIONAL'].mean()
        total_domicilios = int(dados['Total de domicílios'].sum())

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("População total", f"{total_pop:,}".replace(",", "."))
        col2.metric("Área total", f"{area_total:,.1f} ha".replace(",", "."))
        col3.metric("Densidade média", f"{densidade_media:.1f} hab/ha")
        col4.metric("Total de domicílios", f"{total_domicilios:,}".replace(",", "."))

        st.divider()

        st.map(dados, latitude='Latitude', longitude='Longitude', use_container_width=True, height=500, size=180)

        st.divider()

        # Gráfico de barras com linha de densidade (área x densidade)
        st.write("### Área e Densidade Populacional por Bairro")
        fig_barra_linha = graph.plot_barra_linha(
            dados,
            feature_bairro_x='BAIRRO',
            feature_area_y='Área (ha)',
            feature_densidade_y='DENSIDADE POPULACIONAL',
            label_y='Área (ha)'
        )
        st.pyplot(fig_barra_linha)

        st.divider()

        # Caracterização étnica
        st.write("### Caracterização Étnica dos Bairros")
        caract_etnica = ['% Branca', '% Preta', '% Amarela', '% Parda', '% Indígena']
        cores_etnia = ['#4e79a7', '#333333', '#f28e2b', '#76b7b2', '#59a14f']
        fig_etnia = graph.plot_barra_empilhada(dados, 'BAIRRO', caract_etnica, cores=cores_etnia)
        st.pyplot(fig_etnia)

        # Caracterização etária
        st.write("### Distribuição Etária dos Bairros")
        caract_etaria = ['0 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos', '20 a 49 anos', '50 a 64 anos', 'acima de 65 anos']
        fig_etaria = graph.plot_barra_empilhada(dados, 'BAIRRO', caract_etaria)
        st.pyplot(fig_etaria)

        st.divider()
        st.write("### Dados dos bairros selecionados")
        st.dataframe(dados, use_container_width=True)

    else:
        st.info("Selecione ao menos um bairro para visualizar os dados.")
