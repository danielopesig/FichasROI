import streamlit as st
from modules.logica import detectar_padroes, obter_entrada_ideal
from modules.race import desenhar_race
from modules.teclado import exibir_teclado

st.set_page_config(layout="centered")

st.markdown("### 🏁 Padrão ativo – Confira entrada ideal abaixo.")
entrada_ideal = None

if 'historico' not in st.session_state:
    st.session_state.historico = []

col1, col2 = st.columns(2)
with col1:
    st.markdown("⬅️ Últimos números (mais recente à esquerda):")
    st.write(" ".join(str(n) for n in st.session_state.historico[::-1]))

with col2:
    st.markdown("🎯 Entrada ideal:")
    if len(st.session_state.historico) >= 5:
        ultimos_5 = st.session_state.historico[-5:]
        padrao, entrada_ideal = detectar_padroes(ultimos_5)
        if entrada_ideal:
            st.success(f"✅ Entrada ideal sugerida: {', '.join(map(str, entrada_ideal))}")
        else:
            st.warning("⚠️ Nenhuma entrada ideal no momento.")
    else:
        st.info("ℹ️ Insira pelo menos 5 números.")

desenhar_race(entrada_ideal)

st.markdown("### 🎰 Digite o número sorteado:")
exibir_teclado()