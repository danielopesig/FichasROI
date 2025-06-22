import streamlit as st

def exibir_teclado():
    cols = st.columns(9)
    for i in range(37):
        col = cols[i % 9]
        if col.button(str(i)):
            st.session_state.historico.append(i)
            st.session_state.ultimo_numero = i