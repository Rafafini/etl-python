import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as pl


st.image('https://s3.amazonaws.com/gupy5/production/companies/944/career/28027/images/2021-09-21_14-00_mainImage.jpg')

arquivo = st.file_uploader(
    '*Efetue o upload do arquivo CSV*',
    type=['csv']
)

print(arquivo)

st.title('Teste 2')

st.title('Teste 3')