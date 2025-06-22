import streamlit as st

def exibir_teclado():
    cols = st.columns(9)
    for i in range(37):
        if cols[i % 9].button(str(i)):
            st.session_state.historico.append(i)
    if st.button("🔄 Limpar"):
        st.session_state.historico = []