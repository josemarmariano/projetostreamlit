import streamlit as st
import pandas as pd


st.title('Consulta de Clientes')
st.divider()

dados = pd.read_csv('clientes.csv',delimiter=';')

st.dataframe(dados)
