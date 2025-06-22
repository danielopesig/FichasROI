
import streamlit as st
import utils

st.set_page_config(page_title="Investidor de Fichas – Leitura Estratégica", layout="wide")

st.markdown("## 🧠 Investidor de Fichas – Leitura Estratégica")
st.markdown("---")

# RaceTrack
st.markdown("### 🏁 Pista (RaceTrack) – Leitura da mesa:")
st.markdown(utils.render_racetrack(), unsafe_allow_html=True)

# Últimos 12 Números
st.markdown("### 🧮 Últimos 12 Números (mais antigo ← mais recente):")
if "history" not in st.session_state:
    st.session_state.history = []

st.write(" ➔ ".join(map(str, st.session_state.history[::-1])) if st.session_state.history else "` `")

# Entrada ideal
if len(st.session_state.history) >= 5:
    ideal = utils.get_ideal_entry(st.session_state.history[-5:])
    st.success(f"✅ Entrada ideal sugerida: {', '.join(map(str, ideal))}")
else:
    st.info("📊🔍 Aguardando mais entradas...")

# Digite o número sorteado
st.markdown("### 🎰 Digite o número sorteado:")
cols = st.columns(12)
for i in range(3):
    for j in range(12):
        number = i * 12 + j
        if number <= 36:
            with cols[j]:
                if st.button(f"{number}", key=f"btn_{number}"):
                    st.session_state.history.append(number)
                    st.experimental_rerun()

# Botões de ação
if st.button("🔄 Limpar tudo"):
    st.session_state.history = []
    st.experimental_rerun()
