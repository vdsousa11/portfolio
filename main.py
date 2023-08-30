import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Francisco Corte-Real")
    content = """
    Teste, para depois criar um texto
    
    """
    st.info(content)


info1 = ("Below you can find some of the apps I have built in Python. Feel free to contact me.")

st.info(info1)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])

