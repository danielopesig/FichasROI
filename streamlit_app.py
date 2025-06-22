
import streamlit as st

st.set_page_config(page_title="Investidor de Fichas", layout="centered")

st.markdown("## 🏁 Padrão ativo – Confira entrada ideal abaixo.")

# RaceTrack (simulação)
st.markdown("### 🎯 RaceTrack")
racetrack_numbers = list(range(37))
alvo_ativos = [2, 4]  # Exemplo de alvos fortes

cols = st.columns(len(racetrack_numbers))
for i, col in enumerate(cols):
    if i in alvo_ativos:
        col.markdown(f"<div style='background-color:green; color:white; border-radius:50%; padding:8px; text-align:center'>{i}</div>", unsafe_allow_html=True)
    else:
        col.markdown(f"<div style='background-color:gold; color:black; border-radius:50%; padding:8px; text-align:center'>{i}</div>", unsafe_allow_html=True)

# Sugestão de entrada
st.markdown("#### 🎯 Entrada ideal: até 1 vizinho (3 fichas)")

# Últimos 12 números (mais recente à esquerda)
ultimos = [12, 31, 17, 34, 28, 19, 34, 25, 33, 0, 7, 5]
st.markdown("### 🧮 Últimos 12 Números (mais antigo ← mais recente):")
st.markdown(" ➝ ".join(map(str, reversed(ultimos))))

# Teclado numérico vertical
st.markdown("### 🤖 Digite o número sorteado:")
for i in range(37):
    st.button(str(i))
