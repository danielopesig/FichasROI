import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Investidor de Fichas", layout="centered")

st.title("🎯 WebApp Mini – Investidor de Fichas")
st.markdown("Clique nos números conforme a ordem da roleta Evolution (mais recente à esquerda):")

if "numeros" not in st.session_state:
    st.session_state.numeros = []

# Grade estilo roleta
grade = [
    [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],
    [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
]

st.markdown("### 🎰 Grade de entrada:")
for linha in grade:
    cols = st.columns(len(linha))
    for i, numero in enumerate(linha):
        if cols[i].button(str(numero), key=f"btn_{numero}"):
            st.session_state.numeros.insert(0, numero)
            if len(st.session_state.numeros) > 12:
                st.session_state.numeros.pop()

if st.button("🎯 Zero (0)"):
    st.session_state.numeros.insert(0, 0)
    if len(st.session_state.numeros) > 12:
        st.session_state.numeros.pop()

st.markdown("### 🔢 Últimos 12 números (mais recente à esquerda):")
st.write(" ← ".join(map(str, st.session_state.numeros)))

ultimos_5 = st.session_state.numeros[:5]

def gerar_alerta(numeros):
    if len(numeros) < 5:
        return "🔎 Aguarde mais entradas para leitura do padrão."
    repetidos = len(set(numeros)) < len(numeros)
    if repetidos:
        return "🔁 Padrão de Repetição DETECTADO – Atenção!"
    return "🎯 Tendência detectada – veja alvos abaixo."

st.markdown("### 📊 Leitura Estratégica Atual:")
st.success(gerar_alerta(ultimos_5))

roleta_evolution = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8,
    23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
]

def alvos_por_numero(n):
    idx = roleta_evolution.index(n)
    return [roleta_evolution[(idx + i) % len(roleta_evolution)] for i in [-2, -1, 0, 1, 2]]

contagem = {i: 0 for i in range(37)}
for n in ultimos_5:
    for alvo in alvos_por_numero(n):
        contagem[alvo] += 1

mais_fortes = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
entrada_ideal = [num for num, qtd in mais_fortes if qtd >= 2][:2]

if entrada_ideal:
    st.markdown(f"### ✅ Entrada Ideal: {', '.join(map(str, entrada_ideal))} (alvos fortes 🔥)")
else:
    st.markdown("### ⚠️ Nenhum alvo forte claro no momento.")

fig, ax = plt.subplots(figsize=(10, 2))
ax.set_xlim(0, 37)
ax.set_ylim(0, 1)
ax.axis('off')

for idx, n in enumerate(roleta_evolution):
    cor = "lightgray"
    emoji = ""
    if contagem[n] >= 2:
        cor = "#ff9999"
        emoji = "🔥"
    elif contagem[n] == 1:
        cor = "#a0d8f0"
        emoji = "🧊"
    ax.add_patch(plt.Circle((idx, 0.5), 0.4, color=cor, ec='black'))
    ax.text(idx, 0.5, f"{n}\n{emoji}", fontsize=8, ha='center', va='center')

st.markdown("### 🧭 RaceTrack estilo Evolution:")
st.pyplot(fig)
