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




def mostrar():
    st.title("Análise Sócio-Demográfica")
    st.write("Plataforma para análise de dados sócio-demográficos dos bairros de Salvador")

    # Carregar dados
    df = pd.read_csv('dados/dataset_salvador.csv')


    # Selecionar bairro
    bairros = df['BAIRRO'].unique()
    bairro_selecionado = st.multiselect("Selecione os bairros", bairros)



    # filtragem de dados por bairro
    dados_bairros_selecionados = df[df['BAIRRO'].isin(bairro_selecionado)]

    dados_bairros_selecionados['Área (ha)'] = dados_bairros_selecionados['área'] / 10_000
    dados_bairros_selecionados['DENSIDADE POPULACIONAL'] = dados_bairros_selecionados['População segundo o Censo de 2010'] / (dados_bairros_selecionados['Área (ha)'])
    dados_bairros_selecionados['Domicilios por hectare'] = dados_bairros_selecionados['Total de domicílios'] / (dados_bairros_selecionados['Área (ha)'])


    # Exibir os dados dos bairros selecionados
    if not dados_bairros_selecionados.empty:

        st.map(dados_bairros_selecionados, latitude='Latitude', longitude='Longitude', use_container_width=True, height=500, size=180)



        st.divider()

        col1, col2 = st.columns(2)
        with col1:
            st.write("### População por Bairro")
            st.bar_chart(dados_bairros_selecionados, x_label='Bairros', y_label='População', x='BAIRRO', y='População segundo o Censo de 2010', height=400)
        with col2:
            st.write("### Densidade Populacional por Bairro")
            st.bar_chart(dados_bairros_selecionados, x_label='Bairros', y_label='Densidade Populacional', x='BAIRRO', y='DENSIDADE POPULACIONAL', height=400)

        st.write("### Caracterização étnica dos bairros")
        caract_etnica = ['% Branca', '% Preta', '% Amarela', '% Parda', '% Indígena']
        st.bar_chart(dados_bairros_selecionados[caract_etnica], height=400, x_label='Bairros', y_label='Porcentagem')

        caract_etaria = ['0 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos', '20 a 49 anos', '50 a 64 anos', 'acima de 65 anos']
        st.bar_chart(dados_bairros_selecionados[caract_etaria], height=400, x_label='Bairros', y_label='Porcentagem')

        #st.write("*Dados obtidos a partir do senso de 2010*")


        st.divider()
        st.write("### Dados dos bairros selecionados")
        st.write("Baixe os dados dos selecionados")
        st.write(dados_bairros_selecionados)

    else:
        st.write("Nenhuma informação encontrada para os bairros selecionados.")