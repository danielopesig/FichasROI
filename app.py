
import streamlit as st

st.set_page_config(page_title="Investidor de Fichas - Mini", layout="centered")

st.title("🎯 WebApp Mini – Investidor de Fichas")

# Entrada dos últimos 12 números
numbers = st.text_input("Digite os 12 últimos números (da direita para a esquerda, separados por vírgula):")

if numbers:
    try:
        nums = [int(n.strip()) for n in numbers.split(",") if n.strip().isdigit()]
        if len(nums) >= 5:
            ultimos_5 = nums[:5]

            # Mapeamento de alvos simplificado de exemplo (base real precisa ser substituída pela tabela do Leo)
            tabela_alvos = {
                0: [10, 20, 30],
                1: [17, 7],
                2: [22],
                3: [33],
                4: [21, 9],
                5: [25, 15, 35],
                6: [20, 17, 7],
                7: [17, 20],
                9: [19],
                10: [20, 30],
                15: [35, 9, 5],
                17: [20, 7],
                20: [17, 7],
                22: [2],
                25: [20, 22],
                30: [0, 20],
                33: [3]
            }

            alvos_total = []
            repeticoes = []
            for n in ultimos_5:
                alvos = tabela_alvos.get(n, [])
                alvos_sem_repeticao = [a for a in alvos if a != n]
                if n in alvos:
                    repeticoes.append(n)
                alvos_total.extend(alvos_sem_repeticao)

            # Contar força
            from collections import Counter
            contagem = Counter(alvos_total)
            tendencias_fortes = [num for num, freq in contagem.items() if freq >= 2]
            tendencias_fracas = [num for num, freq in contagem.items() if freq == 1]

            st.subheader("🔍 Leitura da Mesa")
            if repeticoes:
                st.warning(f"🔁 Padrão de Repetição detectado nos números: {repeticoes}")
            if tendencias_fortes:
                st.success(f"🔥 Tendência forte nos alvos: {tendencias_fortes}")
            if tendencias_fracas:
                st.info(f"🧊 Tendências fracas isoladas: {tendencias_fracas}")
        else:
            st.info("Insira ao menos 5 números para análise.")
    except Exception as e:
        st.error(f"Erro ao processar números: {e}")
