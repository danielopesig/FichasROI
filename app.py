import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Investidor de Fichas", layout="centered")

st.markdown("## 🧠 Investidor de Fichas – Leitura Estratégica")
st.markdown("---")

# Estado
if "numeros" not in st.session_state:
    st.session_state.numeros = []

# Dados da roleta Evolution
roleta_evolution = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8,
    23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
]

def alvos_por_numero(n):
    idx = roleta_evolution.index(n)
    return [roleta_evolution[(idx + i) % len(roleta_evolution)] for i in [-2, -1, 0, 1, 2]]

# === Pista (RaceTrack) ===
st.markdown("### 🏁 Pista (RaceTrack) – Leitura da mesa:")
fig, ax = plt.subplots(figsize=(14, 2.5))
ax.axis('off')

contagem = {i: 0 for i in range(37)}
ultimos_5 = st.session_state.numeros[-5:]

for n in ultimos_5:
    for alvo in alvos_por_numero(n):
        contagem[alvo] += 1

for idx, n in enumerate(roleta_evolution):
    cor = "lightgray"
    emoji = ""
    if contagem[n] >= 2:
        cor = "#ff9999"
        emoji = "🔥"
    elif contagem[n] == 1:
        cor = "#a0d8f0"
        emoji = "🧊"
    ax.add_patch(plt.Circle((idx, 0.5), 0.5, color=cor, ec='black'))
    ax.text(idx, 0.5, f"{n}", fontsize=10, ha='center', va='center')

st.pyplot(fig)

# === Tendência Detectada ===
def gerar_alerta(numeros):
    if len(numeros) < 5:
        return "🔎 Aguarde mais entradas para leitura."
    if len(set(numeros)) < len(numeros):
        return "🔁 Repetição detectada – Proteja ou aguarde."
    return "🎯 Padrão ativo – Confira entrada ideal abaixo."

st.markdown(f"### 📊 {gerar_alerta(ultimos_5)}")

# === Últimos 12 números ===
st.markdown("### 🔢 Últimos 12 Números (mais recente ⟵ mais antigo):")
if st.session_state.numeros:
    st.write(" ⟵ ".join(map(str, reversed(st.session_state.numeros))))
else:
    st.info("Aguardando entradas...")

# === Entrada ideal ===
mais_fortes = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
entrada_ideal = [num for num, qtd in mais_fortes if qtd >= 2][:2]

if entrada_ideal:
    st.success(f"✅ Entrada ideal sugerida: {', '.join(map(str, entrada_ideal))}")
else:
    st.warning("⚠️ Nenhum alvo forte claro.")

st.markdown("---")

# === Teclado numérico em 3 colunas verticais ===
st.markdown("### 🎰 Digite o número sorteado:")

col_a, col_b, col_c = st.columns(3)

colunas = [
    list(range(0, 13)),     # 0 a 12
    list(range(13, 25)),    # 13 a 24
    list(range(25, 37))     # 25 a 36
]

for col, nums in zip([col_a, col_b, col_c], colunas):
    for n in nums:
        if col.button(str(n), key=f"tecla_{n}"):
            st.session_state.numeros.append(n)
            if len(st.session_state.numeros) > 12:
                st.session_state.numeros.pop(0)

# === Botões Voltar e Limpar ===
col1, col2 = st.columns(2)
with col1:
    if st.button("🔙 Voltar"):
        if st.session_state.numeros:
            st.session_state.numeros.pop()
with col2:
    if st.button("🧹 Limpar"):
        st.session_state.numeros = []

st.markdown("---")
