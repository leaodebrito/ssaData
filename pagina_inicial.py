# importar bibliotecas
import streamlit as st
import pandas as pd
import numpy as np


def mostrar():
        st.title("Plataforma SSA Dados")
        st.write("Explorando Salvador através da Arquitetura e dos Dados")

        st.divider()

        st.write("""
                 A Plataforma SSA Dados é uma ferramenta inovadora voltada para a análise e compreensão do espaço urbano de Salvador. Desenvolvida para apoiar o aprendizado e a prática dos estudantes de Arquitetura e Urbanismo, a plataforma oferece uma base estruturada de dados sociodemográficos e equipamentos urbanos, permitindo que os usuários investiguem diferentes bairros da cidade e fundamentem suas propostas arquitetônicas com embasamento técnico e analítico.

                    A plataforma possibilita a exploração interativa de informações sobre:
                    - perfil populacional, 
                    - densidade habitacional, 
                    - infraestrutura e 
                    - distribuição de serviços urbanos, 
                 
                 Fornecendo um panorama detalhado das dinâmicas territoriais de Salvador. Com essa abordagem, os estudantes podem identificar demandas específicas de cada bairro, propor intervenções arquitetônicas mais eficientes e contribuir para soluções urbanas mais sustentáveis e inclusivas.
                 Além de ser um repositório de dados, a SSA Dados busca incentivar uma abordagem baseada em evidências, promovendo a integração entre tecnologia, urbanismo e tomada de decisão informada. Dessa forma, a plataforma se torna um suporte essencial para a concepção de projetos arquitetônicos alinhados às reais necessidades da cidade e de seus habitantes.
                 """)


        st.divider()

        st.write("""
                Projeto em desenvolvimento por:
                - Bruno Leão de Brito
        """)