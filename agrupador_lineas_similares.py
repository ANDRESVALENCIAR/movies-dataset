# ============================================================
# Programa: agrupador_lineas_similares.py
# Autor: ChatGPT & Andrés Valencia
# Descripción:
#   Agrupa productos con descripciones o líneas similares
#   usando similitud de texto (TF-IDF + Cosine Similarity)
# ============================================================

import pandas as pd
import numpy as np
import re
import unicodedata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# === 1. Cargar archivo ===
archivo = "lineas_y_descripciones.xlsx"   # Cambia si el nombre es distinto
df = pd.read_excel(archivo)
df.columns = [c.strip().upper() for c in df.columns]

# Verificar columnas esperadas
if not {"LINEA", "DESCRIPCION"}.issubset(df.columns):
    raise ValueError("El archivo debe tener columnas llamadas 'LINEA' y 'DESCRIPCION'")

# === 2. Preprocesar texto ===
def limpiar_texto(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).lower()
    texto = unicodedata.normalize("NFD", texto).encode("ascii", "ignore").decode("utf-8")  # quitar tildes
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)  # quitar símbolos
    texto = re.sub(r"\s+", " ").strip()
    return texto

df["TEXTO"] = (df["LINEA"].astype(str) + " " + df["DESCRIPCION"].astype(str)).apply(limpiar_texto)

# === 3. Calcular matriz de similitud ===
vectorizer = TfidfVectorizer(stop_words="spanish")
tfidf_matrix = vectorizer.fit_transform(df["TEXTO"])
sim_matrix = cosine_similarity(tfidf_matrix)

# === 4. Agrupar por similitud > umbral ===
umbral = 0.65  # Ajusta si quieres agrupar más o menos agresivo
grupos = [-1] * len(df)
grupo_actual = 0

for i in range(len(df)):
    if grupos[i] == -1:
        similares = np.where(sim_matrix[i] >= umbral)[0]
        for idx in similares:
            grupos[idx] = grupo_actual
        grupo_actual += 1

df["GRUPO_SUGERIDO"] = grupos

# === 5. Generar etiqueta de grupo más representativa ===
grupo_nombres = (
    df.groupby("GRUPO_SUGERIDO")["LINEA"]
    .agg(lambda x: x.mode().iat[0] if not x.mode().empty else x.iloc[0])
    .to_dict()
)
df["NOMBRE_GRUPO"] = df["GRUPO_SUGERIDO"].map(grupo_nombres)

# === 6. Recomendaciones automáticas ===
recomendaciones = []
for _, g in df.groupby("GRUPO_SUGERIDO"):
    if len(g) > 3:
        recomendacion = "Fusionar en línea consolidada"
    elif len(g) > 1:
        recomendacion = "Evaluar fusión parcial"
    else:
        recomendacion = "Mantener independiente"
    recomendaciones.extend([recomendacion] * len(g))
df["RECOMENDACION"] = recomendaciones

# === 7. Guardar resultados ===
salida = "agrupaciones_lineas.csv"
df.to_csv(salida, index=False, encoding="utf-8-sig")

print("\n✅ Análisis completado. Archivo generado:", salida)
print("Grupos creados:", len(set(grupos)))
print(df.head(10))
