import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados (titulo, autor, dt_inicio, tipo_livro, dt_fim):
    if titulo and dt_inicio <= date.today():
        with open ('livros.csv', 'a', encoding='utf-8') as file:
            file.write(f'{titulo}, {autor}, {dt_inicio}, {tipo_livro}, {dt_fim}\n')
        st.session_state ["sucesso"] = True
    else:
        st.session_state ["sucesso"] = False

st.set_page_config (
    page_title='Estante Virtual',
    page_icon='📚'
)

st.title ('Cadastro de Livros Lidos')
st.divider()

titulo = st.text_input ('Título do livro:',
                        key='titulo_lido')

autor = st.text_input ('Autor: ',
                       key='autor')

dt_inicio = st.date_input ('Comecei no dia:', format='DD/MM/YYYY')

tipo_livro = st.selectbox ('Selecione o tipo:',
                           ['Livro físico', 'Ebook'])

if tipo_livro == 'Livro físico':
    num_paginas = st.number_input ('Número de páginas: ')
    
dt_fim = st.date_input ('Terminei no dia: ', format='DD/MM/YYYY')

st.write ('Classificação:')

classificacao = ["1", "2", "3", "4", "5"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"Você classificou o livro com {classificacao[selected]} estrela(s).")


btn_cadastrar = st.button ('Cadastrar',
                           on_click=gravar_dados,
                           args= [titulo, autor, dt_inicio, tipo_livro, dt_fim])

if btn_cadastrar:
    if st.session_state ["sucesso"]:
        st.success ('Cadastro realizado com sucesso!', icon='✅')
        st.balloons()
    else:
        st.error ('Erro no cadastro!', icon='❌')
        