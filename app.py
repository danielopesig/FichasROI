import streamlit as st
from logica import detectar_padroes, obter_entrada_ideal
from race import exibir_race
from teclado import exibir_teclado

st.set_page_config(page_title="Investidor de Fichas", layout="centered")

st.markdown("## 🏁 Padrão ativo – Confira entrada ideal abaixo.")

if "historico" not in st.session_state:
    st.session_state.historico = []

numero = st.session_state.get("ultimo_numero", None)
entrada_ideal, padrao, alvos = detectar_padroes(st.session_state.historico)

exibir_race(alvos, numero)
st.markdown(f"### 🎯 {padrao}")
st.success(f"✅ Entrada ideal sugerida: {', '.join(map(str, entrada_ideal))}" if entrada_ideal else "Aguardando padrão...")

exibir_teclado()
