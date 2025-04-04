import streamlit as st
import pandas as pd

dados = pd.read_csv ('livros.csv')

st.title ('Livros Cadastrados')
st.divider()

st.dataframe (dados)