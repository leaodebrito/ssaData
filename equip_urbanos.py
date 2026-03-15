
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from pathlib import Path

def mostrar():
    file = Path(__file__).parent / 'dados' / 'dataset_equip_urb_salvador.csv'
    df = pd.read_csv(file)

    st.title("Equipamentos Urbanos")
    st.write("Ferramenta de apresentação de dados de equipamentos urbanos dos bairros de Salvador")

    col1, col2 = st.columns(2)

    with col1:
        tipo_equipamento = sorted(df['Tipo'].unique().tolist())
        selecionados = st.multiselect("Selecione o tipo de equipamento", tipo_equipamento)

    with col2:
        bairros_disponiveis = sorted(df['nome'].dropna().unique().tolist())
        # Carregar dataset de bairros para filtro por bairro
        bairro_file = Path(__file__).parent / 'dados' / 'dataset_salvador.csv'
        df_bairros = pd.read_csv(bairro_file)
        bairros = sorted(df_bairros['BAIRRO'].unique().tolist())
        bairros_selecionados = st.multiselect("Filtrar por bairro (opcional)", bairros)

    # Filtragem por tipo
    if selecionados:
        df_filtrado = df[df['Tipo'].isin(selecionados)]
    else:
        df_filtrado = df.copy()

    # Filtragem por bairro via proximidade geográfica (bounding box)
    if bairros_selecionados:
        coords_bairros = df_bairros[df_bairros['BAIRRO'].isin(bairros_selecionados)]
        lat_min = coords_bairros['Latitude'].min() - 0.01
        lat_max = coords_bairros['Latitude'].max() + 0.01
        lon_min = coords_bairros['Longitude'].min() - 0.01
        lon_max = coords_bairros['Longitude'].max() + 0.01
        df_filtrado = df_filtrado[
            (df_filtrado['latitude'] >= lat_min) & (df_filtrado['latitude'] <= lat_max) &
            (df_filtrado['longitude'] >= lon_min) & (df_filtrado['longitude'] <= lon_max)
        ]

    if df_filtrado.empty:
        st.info("Nenhum equipamento encontrado para os filtros selecionados.")
        return

    # Cards de métricas
    total = len(df_filtrado)
    tipos_encontrados = df_filtrado['Tipo'].nunique()
    col1, col2 = st.columns(2)
    col1.metric("Equipamentos encontrados", total)
    col2.metric("Tipos diferentes", tipos_encontrados)

    st.map(df_filtrado, latitude='latitude', longitude='longitude', color='cor', size=100, use_container_width=True, height=800)

    st.dataframe(df_filtrado[['nome', 'Tipo', 'latitude', 'longitude']].reset_index(drop=True), use_container_width=True)
