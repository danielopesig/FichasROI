
import streamlit as st

def exibir_race_track(alvos):
    st.markdown("### 🎯 Race Track")
    racetrack = []
    for i in range(37):
        if i in alvos:
            racetrack.append(f":green_circle:{i}")
        else:
            racetrack.append(str(i))
    st.write(" ".join(racetrack))
