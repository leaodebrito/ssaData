
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

def mostrar():
    file = 'dados/dataset_equip_urb_salvador.csv'
    df = pd.read_csv(file)

    st.title("Equipamentos Urbanos")
    st.write("Ferramenta de apresentação de dados de equipamentos urbanos dos bairros de Salvador")

    #st.write(df)

    #selecionar equipamento
    tipo_equipamento = df['Tipo'].unique().tolist()

    print(tipo_equipamento)
    selecionados = st.multiselect("Selecione o tipo de equipamento", tipo_equipamento)

    
# Filtrando o DataFrame corretamente
    df_equipamentos = df[df['Tipo'].isin(selecionados)]

    st.map(df_equipamentos, latitude='latitude', longitude='longitude', color='cor', size=100, use_container_width=True, height= 800)

    st.write(df_equipamentos)
