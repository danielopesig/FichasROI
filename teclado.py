
import streamlit as st

def exibir_teclado():
    colunas = st.columns(6)
    for i in range(37):
        if colunas[i % 6].button(str(i)):
            st.session_state.historico.insert(0, i)
            st.rerun()

    st.markdown("### 🧾 Últimos números:")
    if st.session_state.historico:
        st.write(" ⬅️ " + " | ".join(map(str, st.session_state.historico[:12])))
