import streamlit as st

def exibir_race(alvos, ultimo_numero):
    numeros = list(range(37))
    linha = ""
    for n in numeros:
        cor = "green" if n in alvos else ("red" if n == ultimo_numero else "gray")
        style = f"background-color:{cor};border-radius:50%;padding:6px 10px;margin:1px;display:inline-block;"
        linha += f"<span style='{style}'>{n}</span>"
    st.markdown(f"<div style='text-align:center'>{linha}</div>", unsafe_allow_html=True)