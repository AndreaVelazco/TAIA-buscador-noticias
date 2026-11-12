"""Motor de búsqueda: TF-IDF + similitud coseno (Laboratorios 2 y 3)."""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.preprocesar import preprocesar_a_texto


class Buscador:
    def __init__(self, df: pd.DataFrame):
        """df debe tener las columnas: titulo, resumen (y opcionalmente fuente, fecha, link)."""
        self.df = df.reset_index(drop=True)
        textos = (self.df["titulo"].fillna("") + ". " + self.df["resumen"].fillna(""))
        self.vectorizador = TfidfVectorizer()
        self.matriz = self.vectorizador.fit_transform(textos.map(preprocesar_a_texto))

    def buscar(self, consulta: str, k: int = 5) -> pd.DataFrame:
        """Devuelve las k noticias más parecidas a la consulta, con su puntaje."""
        q = self.vectorizador.transform([preprocesar_a_texto(consulta)])
        puntajes = cosine_similarity(q, self.matriz).ravel()
        orden = puntajes.argsort()[::-1][:k]
        resultado = self.df.iloc[orden].copy()
        resultado["puntaje"] = puntajes[orden]
        return resultado[resultado["puntaje"] > 0]
