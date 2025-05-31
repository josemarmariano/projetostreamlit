import streamlit as st
from datetime import date
import time 

def gravar_dados(nome,data,tipo):
    if nome and data <= date.today():
        st.session_state['sucesso'] = True
        with open('clientes.csv','a',encoding='utf-8') as f:
            f.write(f'{nome};{data};{tipo} \n')
    else:
        st.session_state['sucesso'] = False

st.set_page_config(
    page_title='Cadastro de Clientes',
)

st.title('Cadastro de Clientes')
st.divider()

nome = st.text_input('Digite o Nome do Cliente')
dt_nasc = st.date_input('Data de Nascimento',format="DD/MM/YYYY")
tipo_pessoa = st.selectbox('Tipo de Pessoa',['','Fisica','Juridica'])

btn_cadastrar = st.button('Cadastrar',
                            on_click=gravar_dados,
                            args=[nome,dt_nasc,tipo_pessoa])

if btn_cadastrar:
    if st.session_state['sucesso']:
        x = st.success('Registro gravado')
        time.sleep(2)
        x.empty()
    else:
        x = st.error('Registro não foi salvo')
        time.sleep(2)
        x.empty()