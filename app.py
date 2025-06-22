
import streamlit as st
from logica import detectar_padroes, obter_entrada_ideal
from teclado import exibir_teclado
from race import exibir_race_track

st.set_page_config(page_title="Investidor de Fichas", layout="centered")

st.markdown("## 🏁 Padrão ativo – Confira entrada ideal abaixo.")

if "historico" not in st.session_state:
    st.session_state.historico = []

entrada = st.session_state.historico[:5]
padrao, sugestoes = detectar_padroes(entrada), obter_entrada_ideal(entrada)

exibir_race_track(sugestoes)
st.markdown(f"### 🎯 Padrão ativo – Confira entrada ideal abaixo.")
st.success(f"✅ Entrada ideal sugerida: {', '.join(map(str, sugestoes)) if sugestoes else 'Aguardando...'}")

st.markdown("### 🎰 Digite o número sorteado:")
exibir_teclado()
