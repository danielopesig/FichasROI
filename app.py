
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Investidor de Fichas – Leitura Estratégica", layout="wide")

st.title("🧠 Investidor de Fichas – Leitura Estratégica")

st.markdown("## 🏁 Pista (RaceTrack) – Leitura da mesa:")

# Ordem dos números como na pista real
race_track = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6,
    27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16,
    33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
]

# Session state para armazenar os últimos 12 números
if "ultimos_numeros" not in st.session_state:
    st.session_state.ultimos_numeros = []

# Clique nos botões
st.markdown("## 🎰 Digite o número sorteado:")
cols = st.columns(9)
for i in range(37):
    if cols[i % 9].button(str(i)):
        st.session_state.ultimos_numeros.insert(0, i)
        st.session_state.ultimos_numeros = st.session_state.ultimos_numeros[:12]

# Exibir pista com destaque no último número
ultimo = st.session_state.ultimos_numeros[0] if st.session_state.ultimos_numeros else None

html = "<div style='font-size:22px;'>"
for num in race_track:
    if num == ultimo:
        html += f"<span style='color:red; font-weight:bold; border: 2px solid red; border-radius: 50%; padding: 3px 8px;'>{num}</span> ● "
    else:
        html += f"{num} ● "
html += "</div>"

components.html(html, height=100, scrolling=True)

# Exibir últimos 12 números
st.markdown("## 🧮 Últimos 12 Números (mais antigo ← mais recente):")
st.write(" → ".join(map(str, st.session_state.ultimos_numeros[::-1])))
