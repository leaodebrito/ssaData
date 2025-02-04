

import streamlit as st
import pandas as pd
import numpy as np

import dados_sociodemograficos
import equip_urbanos

# Configuração da página
st.set_page_config(page_title="SSA Dados", layout="wide")

# Tela principal
def main():
    #st.sidebar.image("logo.png", use_column_width=True)

    # Menu de navegação
    page = st.sidebar.selectbox("Navegação", 
                                ["Página Inicial", 
                                 "Dados sócio-demográficas", 
                                 "Equipamentos urbanos"])

    # Conteúdo das páginas
    if page == "Página Inicial":
        st.title("Bem-vindo(a),")
        st.write("Abaixo um resumo de seus projetos")

        # Seção: Preços de venda
        st.markdown("### Preços de venda")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Apartamentos"):
                st.write("Dados sobre preços de venda de apartamentos.")
        
        with col2:
            if st.button("Casas"):
                st.write("Dados sobre preços de venda de casas.")
        
        with col3:
            if st.button("Terrenos"):
                st.write("Dados sobre preços de venda de terrenos.")

    elif page == "Dados sócio-demográficas":
        dados_sociodemograficos.mostrar()

    elif page == "Equipamentos urbanos":
        equip_urbanos.mostrar_pagina()

    st.divider()

if __name__ == "__main__":
    main()

