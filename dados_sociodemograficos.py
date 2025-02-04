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
    # Exibir os dados dos bairros selecionados
    if not dados_bairros_selecionados.empty:
        st.write("Informações dos bairros selecionados:")
        st.write(dados_bairros_selecionados)

        # Criar colunas para os gráficos
        col1, col2 = st.columns(2)

        # Gráfico de área e densidade populacional
        with col1:
            st.subheader("Caracterização étnica dos bairros")
            caract_etnica = ['% Branca', '% Preta', '% Amarela', '% Parda', '% Indígena']
            fig = graph.plot_barra_empilhada(dados_bairros_selecionados, 'BAIRRO', caract_etnica)
            st.pyplot(fig)

        # Gráfico de caracterização etária dos bairros
        with col2:
            st.subheader("Caracterização etária dos bairros")
            faixas_idade = ['0 a 4 anos', '5 a 9 anos', '10 a 14 anos', '15 a 19 anos', '20 a 49 anos', '50 a 64 anos', 'acima de 65 anos']
            fig = graph.plot_barra_empilhada(dados_bairros_selecionados, 'BAIRRO', faixas_idade)
            st.pyplot(fig)

        st.divider()

        # Gráfico de caracterização étnica dos bairros
        with col1:
            st.subheader("Área dos bairros e densidade populacional")
            fig = graph.plot_barra_linha(dados_bairros_selecionados, 'BAIRRO', 'Área (ha)', 'DENSIDADE POPULACIONAL')
            st.pyplot(fig)
           

        # Gráfico de total de domicílios
        with col2:
            st.subheader("Total de domicílios")
            fig = graph.plot_barra_linha(dados_bairros_selecionados, 'BAIRRO', 'Total de domicílios', 'Total de domicílios próprios', label_y='Total de domicílios')
            st.pyplot(fig)

        st.divider()

        # Gráfico de distribuição de domicílios e rendimento médio
        with col1:
            st.subheader("Distribuição de domicílios e Rendimento médio")
            fig = graph.plot_barra_linha(dados_bairros_selecionados, 'BAIRRO', 'Domicilios por hectare', 'Rendimento médio atualizado')
            st.pyplot(fig)





    else:
        st.write("Nenhuma informação encontrada para os bairros selecionados.")