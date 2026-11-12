from src.preprocesar import preprocesar


def test_lematiza_y_quita_stopwords():
    assert preprocesar("¡Los niños están jugando en el parque!") == ["niño", "jugar", "parque"]


def test_quita_urls_y_html():
    assert preprocesar("<p>Mira https://ejemplo.com el parque</p>") == ["mirar", "parque"]
