# 📰 Buscador de noticias en español

Aplicación web que recibe una consulta (por ejemplo, "inflación") y devuelve las noticias
más relevantes de un corpus en español, ordenadas por similitud.

**Técnicas de NLP:** preprocesamiento en español (normalización, stopwords, lematización con spaCy),
representación TF-IDF y similitud coseno (scikit-learn).
**Entregable:** aplicación web con Streamlit.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate          # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download es_core_news_sm
```

## Uso

```bash
# 1. (Opcional) Descargar noticias reales desde feeds RSS. Se pueden ejecutar varios días seguidos.
python -m src.obtener_datos

# 2. Abrir la demo
streamlit run app.py
```

Si `data/noticias.csv` no existe, la app usa `data/noticias_ejemplo.csv`
(24 noticias **ficticias** solo para probar que todo funciona).

## Pruebas

```bash
python -m pytest
```

## Estructura

```
app.py                     # Interfaz web (Streamlit)
src/preprocesar.py         # Limpieza, tokenización, stopwords y lematización
src/buscador.py            # TF-IDF + similitud coseno
src/obtener_datos.py       # Script que descarga noticias desde RSS
data/noticias_ejemplo.csv  # Corpus de prueba (ficticio)
tests/                     # Pruebas automatizadas
```

## Estado del proyecto (Evidencia 3 — demo al 50%)

- [x] Repositorio y estructura
- [x] Script de obtención de datos (RSS)
- [x] Preprocesamiento en español
- [x] Búsqueda TF-IDF + coseno
- [x] Demo web básica
- [ ] Evaluación con consultas de prueba (precision@k, MRR)
- [ ] Filtro por fecha y resaltado de términos
- [ ] Informe (máx. 4 páginas)
