import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Investidor de Fichas", layout="centered")

st.title("🎯 WebApp Mini – Investidor de Fichas")
st.markdown("Clique nos números conforme forem saindo (da esquerda para a direita – ordem cronológica):")

# Inicializa os números
if "numeros" not in st.session_state:
    st.session_state.numeros = []

# Botões de clique 0–36
cols = st.columns(6)
for i in range(37):
    if cols[i % 6].button(str(i)):
        if len(st.session_state.numeros) >= 12:
            st.session_state.numeros.pop(0)
        st.session_state.numeros.append(i)

# Botões de ação
col1, col2 = st.columns(2)
with col1:
    if st.button("🔙 Desfazer último número"):
        if st.session_state.numeros:
            st.session_state.numeros.pop()

with col2:
    if st.button("🔄 Limpar tudo"):
        st.session_state.numeros = []

# Exibe histórico
st.markdown("### 🔢 Últimos 12 números (mais antigo → mais recente):")
st.write(" → ".join(map(str, st.session_state.numeros)))

# Últimos 5 para leitura estratégica
ultimos_5 = st.session_state.numeros[-5:]

def gerar_alerta(numeros):
    if len(numeros) < 5:
        return "🔎 Aguarde mais entradas para leitura do padrão."
    repetidos = len(set(numeros)) < len(numeros)
    if repetidos:
        return "🔁 Padrão de Repetição DETECTADO – Atenção!"
    return "🎯 Tendência detectada – veja alvos abaixo."

st.markdown("### 📊 Leitura Estratégica Atual:")
st.success(gerar_alerta(ultimos_5))

# === RACE TRACK STYLE VISUAL === #

# Mapeamento da roleta (ordem real estilo Evolution)
roleta_evolution = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8,
    23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
]

# Função para calcular alvos chamados
def alvos_por_numero(n):
    # Cada número chama seus 4 vizinhos reais
    idx = roleta_evolution.index(n)
    vizinhos = []
    for i in [-2, -1, 0, 1, 2]:
        vizinhos.append(roleta_evolution[(idx + i) % len(roleta_evolution)])
    return vizinhos

# Contagem de chamadas por número
contagem = {i: 0 for i in range(37)}
for n in ultimos_5:
    for alvo in alvos_por_numero(n):
        contagem[alvo] += 1

# Identificar alvos mais fortes
mais_fortes = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
entrada_ideal = [num for num, qtd in mais_fortes if qtd >= 2][:2]

# Exibir entrada recomendada
if entrada_ideal:
    st.markdown(f"### ✅ Entrada Ideal: {', '.join(map(str, entrada_ideal))} (alvos fortes 🔥)")
else:
    st.markdown("### ⚠️ Nenhum alvo forte claro no momento.")

# Desenhar racetrack visual
fig, ax = plt.subplots(figsize=(10, 2))
ax.set_xlim(0, 37)
ax.set_ylim(0, 1)
ax.axis('off')

for idx, n in enumerate(roleta_evolution):
    cor = "lightgray"
    emoji = ""
    if contagem[n] >= 2:
        cor = "#ff9999"  # quente
        emoji = "🔥"
    elif contagem[n] == 1:
        cor = "#a0d8f0"  # frio
        emoji = "🧊"
    ax.add_patch(plt.Circle((idx, 0.5), 0.4, color=cor, ec='black'))
    ax.text(idx, 0.5, f"{n}\n{emoji}", fontsize=8, ha='center', va='center')

st.markdown("### 🧭 RaceTrack estilo Evolution:")
st.pyplot(fig)
