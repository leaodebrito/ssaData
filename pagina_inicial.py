# importar bibliotecas
import streamlit as st
import pandas as pd
import numpy as np


def mostrar():
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