

import streamlit as st
import pandas as pd
import numpy as np

import dados_sociodemograficos
import equip_urbanos
import pagina_inicial

# Configuração da página
st.set_page_config(page_title="SSA Dados", layout="wide")

# Tela principal
def main():
    #st.sidebar.image("logo.png", use_column_width=True)

    # Menu de navegação
    st.sidebar.image('assets/farol_salvador.png')
    st.sidebar.title("SSA Dados")
    st.sidebar.divider()

    page = st.sidebar.selectbox("Selecione a página desejada:", 
                                ["Página Inicial", 
                                 "Dados sócio-demográficas", 
                                 "Equipamentos urbanos"])

    # Conteúdo das páginas
    if page == "Página Inicial":
        pagina_inicial.mostrar()

    elif page == "Dados sócio-demográficas":
        dados_sociodemograficos.mostrar()

    elif page == "Equipamentos urbanos":
        equip_urbanos.mostrar()

    st.divider()

if __name__ == "__main__":
    main()

