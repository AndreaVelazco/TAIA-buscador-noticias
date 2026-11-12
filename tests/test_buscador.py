import pandas as pd
from src.buscador import Buscador


def _buscador():
    df = pd.DataFrame({
        "titulo": ["El gato juega con la pelota", "El perro juega en el parque"],
        "resumen": ["", ""],
    })
    return Buscador(df)


def test_devuelve_el_documento_mas_relevante():
    assert _buscador().buscar("pelota", k=1).iloc[0]["titulo"].startswith("El gato")


def test_sin_coincidencias_devuelve_vacio():
    assert _buscador().buscar("astronomía").empty
