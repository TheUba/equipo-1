# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 02 — Preparacion de datos y feature engineering
#
# Objetivo: preparar un dataset limpio y listo para entrenar un modelo de
# clasificacion binaria de churn.

# %% [markdown]
# ## Carga de datos

# %%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/raw/telco_churn.csv")
print(f"Shape original: {df.shape}")
df.head()

# %% [markdown]
# ## Eliminacion de columnas con fuga de informacion
#
# Estas columnas existen PORQUE el cliente ya se fue. Usarlas para predecir
# churn seria trampa — en produccion no las tendriamos disponibles antes
# de que el churn ocurra.

# %%
leak_columns = [
    "Churn Category",    # razon categorizada del churn (solo existe post-churn)
    "Churn Reason",      # razon especifica del churn (solo existe post-churn)
    "Churn Score",       # score calculado (posible fuga circular)
    "Customer Status",   # "Churned", "Stayed", "Joined" — ES el target con otro nombre
    "CLTV",              # customer lifetime value — calculado con datos post-hoc
]

df = df.drop(columns=leak_columns)
print(f"Shape despues de eliminar columnas con fuga: {df.shape}")

# %% [markdown]
# ## Eliminacion de columnas no predictivas
#
# Columnas que son identificadores o datos geograficos granulares
# que no aportan poder predictivo generalizable.

# %%
id_columns = [
    "Customer ID",
    "City",
    "State",
    "Country",
    "Zip Code",
    "Latitude",
    "Longitude",
    "Lat Long",
    "Population",
    "Quarter",
]

df = df.drop(columns=id_columns)
print(f"Shape despues de eliminar columnas no predictivas: {df.shape}")
print(f"\nColumnas restantes ({len(df.columns)}):")
print(df.columns.tolist())

# %% [markdown]
# ## Analisis de tipos de datos
#
# Necesitamos entender que columnas son numericas, cuales categoricas,
# y cuales ya estan codificadas como binarias (0/1).

# %%
# Separar por tipo
binary_cols = [col for col in df.columns if df[col].dropna().isin([0, 1]).all() and col != "Churn"]
numeric_cols = [col for col in df.select_dtypes(include=[np.number]).columns
                if col not in binary_cols and col != "Churn"]
categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

print(f"Binarias (ya codificadas): {len(binary_cols)}")
print(binary_cols)
print(f"\nNumericas continuas: {len(numeric_cols)}")
print(numeric_cols)
print(f"\nCategoricas: {len(categorical_cols)}")
print(categorical_cols)

# %% [markdown]
# ## Tratamiento de valores faltantes

# %%
missing = df.isnull().sum()
missing_report = missing[missing > 0]

if len(missing_report) == 0:
    print("No hay valores faltantes")
else:
    print("Valores faltantes:")
    print(missing_report)
    print()

    # Para categoricas: rellenar con "Sin servicio" (indica que no tiene ese servicio)
    for col in categorical_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna("Sin servicio")
            print(f"  {col}: rellenado con 'Sin servicio'")

    # Para numericas: rellenar con la mediana
    for col in numeric_cols:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"  {col}: rellenado con mediana ({median_val})")

# %% [markdown]
# ## Codificacion de variables categoricas
#
# Usamos one-hot encoding para las categoricas restantes.
# Son pocas categorias por columna, asi que no explota la dimensionalidad.

# %%
print("Categorias por columna:")
for col in categorical_cols:
    print(f"  {col}: {df[col].nunique()} — {df[col].unique()}")

# %%
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
print(f"\nShape despues de encoding: {df_encoded.shape}")

# %% [markdown]
# ## Separacion de features y target

# %%
X = df_encoded.drop(columns=["Churn"])
y = df_encoded["Churn"]

print(f"Features: {X.shape}")
print(f"Target: {y.shape}")
print(f"Tasa de churn: {y.mean():.2%}")

# %% [markdown]
# ## Split train/test
#
# Usamos 80/20 con estratificacion para mantener la proporcion de churn
# en ambos conjuntos.

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Train: {X_train.shape[0]} filas ({y_train.mean():.2%} churn)")
print(f"Test:  {X_test.shape[0]} filas ({y_test.mean():.2%} churn)")

# %% [markdown]
# ## Guardar datasets procesados

# %%
X_train.to_csv("../data/processed/X_train.csv", index=False)
X_test.to_csv("../data/processed/X_test.csv", index=False)
y_train.to_csv("../data/processed/y_train.csv", index=False)
y_test.to_csv("../data/processed/y_test.csv", index=False)

print("Datasets guardados en data/processed/")
print(f"  X_train: {X_train.shape}")
print(f"  X_test:  {X_test.shape}")

# %%
