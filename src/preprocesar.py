"""Preprocesamiento de texto en español (Laboratorio 1 de la clase)."""
import re
import spacy

_nlp = None


def _get_nlp():
    """Carga el modelo de spaCy una sola vez."""
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("es_core_news_sm", disable=["parser", "ner"])
    return _nlp


def limpiar(texto: str) -> str:
    """Normalización mínima: quita HTML y URLs. NO pasa a minúsculas aquí,
    porque el lematizador de spaCy funciona mejor con el texto original."""
    texto = re.sub(r"<[^>]+>", " ", texto or "")
    texto = re.sub(r"https?://\S+", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def preprocesar(texto: str) -> list[str]:
    """Texto -> lista de lemas en minúscula, sin stopwords ni signos."""
    doc = _get_nlp()(limpiar(texto))
    return [t.lemma_.lower() for t in doc if t.is_alpha and not t.is_stop]


def preprocesar_a_texto(texto: str) -> str:
    """Igual que preprocesar(), pero devuelve un string (para TfidfVectorizer)."""
    return " ".join(preprocesar(texto))
