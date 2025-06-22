import streamlit as st

def desenhar_race(alvos):
    st.markdown("### 🛣️ RaceTrack:")
    layout = [
        [5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29],
        [7, 28, 12, 35, 3, 26, 0, 32, 15, 19, 4, 21],
        [2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23],
        [10]
    ]
    for linha in layout:
        cols = st.columns(len(linha))
        for i, n in enumerate(linha):
            estilo = "background-color: green; color: white;" if alvos and n in alvos else ""
            cols[i].markdown(f"<div style='text-align:center; {estilo} border-radius:8px;'>{n}</div>", unsafe_allow_html=True)