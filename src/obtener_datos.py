"""Script de obtención de datos: descarga noticias desde feeds RSS.

Uso:  python -m src.obtener_datos
Cada ejecución AGREGA noticias nuevas a data/noticias.csv (sin duplicar).
Un feed RSS solo trae las ~20-50 noticias más recientes, así que ejecútalo
varias veces en distintos días para ir acumulando un corpus más grande.
"""
import re
from pathlib import Path

import feedparser
import pandas as pd

FEEDS = {
    "BBC Mundo": "https://feeds.bbci.co.uk/mundo/rss.xml",
    "El País": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada",
    "RPP": "https://rpp.pe/feed",
    "20minutos": "https://www.20minutos.es/rss/",
}
SALIDA = Path("data/noticias.csv")


def _sin_html(texto: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", texto or "")).strip()


def descargar() -> pd.DataFrame:
    filas = []
    for fuente, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
            for e in feed.entries:
                filas.append({
                    "titulo": _sin_html(e.get("title", "")),
                    "resumen": _sin_html(e.get("summary", "")),
                    "fuente": fuente,
                    "fecha": e.get("published", ""),
                    "link": e.get("link", ""),
                })
            print(f"{fuente}: {len(feed.entries)} noticias")
        except Exception as error:  # un feed caído no debe detener el script
            print(f"{fuente}: error ({error})")
    return pd.DataFrame(filas)


def main():
    nuevas = descargar()
    if nuevas.empty:
        print("No se descargó nada. Revisa tu conexión o las URLs de FEEDS.")
        return
    if SALIDA.exists():
        nuevas = pd.concat([pd.read_csv(SALIDA), nuevas])
    nuevas = nuevas.drop_duplicates(subset="link").dropna(subset=["titulo"])
    SALIDA.parent.mkdir(exist_ok=True)
    nuevas.to_csv(SALIDA, index=False)
    print(f"Total guardado en {SALIDA}: {len(nuevas)} noticias")


if __name__ == "__main__":
    main()
