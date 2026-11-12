"""Demo web del buscador de noticias.  Ejecutar:  streamlit run app.py"""
from pathlib import Path

import pandas as pd
import streamlit as st

from src.buscador import Buscador

st.set_page_config(page_title="Buscador de noticias", page_icon="📰")
st.title("📰 Buscador de noticias en español")


@st.cache_resource
def cargar_buscador():
    # Usa las noticias reales si ya las descargaste; si no, el corpus de ejemplo.
    ruta = Path("data/noticias.csv")
    if not ruta.exists():
        ruta = Path("data/noticias_ejemplo.csv")
    return Buscador(pd.read_csv(ruta)), ruta.name


buscador, nombre = cargar_buscador()
st.caption(f"Corpus: {nombre} · {len(buscador.df)} noticias")

consulta = st.text_input("¿Qué noticias buscas?", placeholder="ej. inflación, elecciones, fútbol")
k = st.slider("Número de resultados", 1, 10, 5)

if consulta:
    resultados = buscador.buscar(consulta, k)
    if resultados.empty:
        st.warning("No encontré noticias relacionadas. Prueba con otras palabras.")
    for _, fila in resultados.iterrows():
        st.subheader(fila["titulo"])
        st.write(str(fila["resumen"])[:300])
        st.caption(f"{fila.get('fuente', '')} · {fila.get('fecha', '')} · relevancia {fila['puntaje']:.2f}")
        if isinstance(fila.get("link"), str):
            st.markdown(f"[Leer noticia]({fila['link']})")
        st.divider()
