import streamlit as st
from collections import deque

# Mapeamento da pista (RaceTrack)
racetrack = [
    0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5,
    24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26
]

# Estado dos últimos números
if "ultimos_numeros" not in st.session_state:
    st.session_state.ultimos_numeros = deque(maxlen=12)

# Função para atualizar os últimos números
def adicionar_numero(numero):
    st.session_state.ultimos_numeros.appendleft(numero)

# Função para voltar um número
def desfazer():
    if st.session_state.ultimos_numeros:
        st.session_state.ultimos_numeros.popleft()

# Função para limpar tudo
def limpar():
    st.session_state.ultimos_numeros.clear()

# Função para gerar alvos
def gerar_tendencias(nums):
    if len(nums) < 5:
        return "🔎 Aguarde mais entradas", []
    
    ultimos_5 = list(nums)[:5]
    if len(set(ultimos_5)) == 1:
        return "🔁 Repetição detectada – Proteja ou aguarde.", []
    
    # Exemplo simples de tendência: números pares em comum
    comuns = [n for n in ultimos_5 if n % 2 == 0]
    if comuns:
        return "🎯 Padrão ativo – Confira entrada ideal abaixo.", list(set(comuns))[:2]
    
    return "🚨 Nenhum padrão claro – Aguarde.", []

# Interface do App
st.markdown("## 🧠 Investidor de Fichas – Leitura Estratégica")
st.markdown("---")

# Exibir a pista
st.markdown("### 🏁 Pista (RaceTrack) – Leitura da mesa:")
racetrack_str = " ● ".join(str(n) for n in racetrack)
st.markdown(f"<div style='text-align:center; font-size:18px; font-weight:bold; color:#FFD700'>{racetrack_str}</div>", unsafe_allow_html=True)

# Tendência e entrada ideal
msg, sugeridos = gerar_tendencias(st.session_state.ultimos_numeros)
st.markdown(f"### 📊 {msg}")

# Últimos 12 (antigo à direita, novo à esquerda)
ultimos_formatados = " ← ".join(str(n) for n in reversed(st.session_state.ultimos_numeros))
st.markdown("### 🔢 Últimos 12 Números (mais antigo ← mais recente):")
st.markdown(f"`{ultimos_formatados}`")

# Entrada ideal
if sugeridos:
    st.success(f"✅ Entrada ideal sugerida: {', '.join(str(n) for n in sugeridos)}")

# Espaçamento
st.markdown("---")

# Teclado numérico 3 colunas
st.markdown("🎰 **Digite o número sorteado:**")

cols = st.columns(3)
for i in range(37):
    col = cols[i % 3]
    with col:
        if st.button(f"{i}"):
            adicionar_numero(i)
            st.experimental_rerun()

# Botões de controle
st.markdown("### ")
b1, b2 = st.columns(2)
with b1:
    if st.button("↩️ Voltar"):
        desfazer()
        st.experimental_rerun()
with b2:
    if st.button("🧹 Limpar"):
        limpar()
        st.experimental_rerun()
