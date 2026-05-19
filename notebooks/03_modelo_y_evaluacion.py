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
# # 03 — Modelo y evaluacion
#
# Objetivo: entrenar modelos simples para predecir churn, compararlos contra un
# baseline y evaluar solo con las metricas mas utiles para este caso:
# precision y recall.

# %% [markdown]
# ## Carga de datos procesados

# %%
import pandas as pd
import matplotlib.pyplot as plt

X_train = pd.read_csv("../data/processed/X_train.csv")
X_test = pd.read_csv("../data/processed/X_test.csv")
y_train = pd.read_csv("../data/processed/y_train.csv").squeeze()
y_test = pd.read_csv("../data/processed/y_test.csv").squeeze()

print(f"Train: {X_train.shape[0]} filas, {X_train.shape[1]} features")
print(f"Test:  {X_test.shape[0]} filas")
print(f"Tasa de churn en test: {y_test.mean():.2%}")

# %% [markdown]
# ## Baseline: predecir siempre no-churn
#
# Este baseline representa la situacion mas simple posible: asumir que ningun
# cliente se va. Si un modelo no mejora esto, no aporta valor.

# %%
from sklearn.dummy import DummyClassifier
from sklearn.metrics import classification_report

dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)
y_pred_dummy = dummy.predict(X_test)

print("Classification report del baseline:")
print(classification_report(y_test, y_pred_dummy, target_names=["No churn", "Churn"]))

# %% [markdown]
# ## Modelo 1: Regresion Logistica
#
# Empezamos con un modelo simple e interpretable. Como es sensible a la escala,
# primero estandarizamos las features.

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)

print("Classification report de Regresion Logistica:")
print(classification_report(y_test, y_pred_lr, target_names=["No churn", "Churn"]))

# %% [markdown]
# ## Modelo 2: Random Forest
#
# Este modelo agrega capacidad no lineal sin necesidad de escalar las features.

# %%
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("Classification report de Random Forest:")
print(classification_report(y_test, y_pred_rf, target_names=["No churn", "Churn"]))

# %% [markdown]
# ## Tabla comparativa
#
# Para churn, nos quedamos con dos preguntas simples:
# - **Precision**: de las alertas de churn, cuantas eran correctas
# - **Recall**: de los churn reales, cuantos detectamos a tiempo

# %%
from sklearn.metrics import precision_score, recall_score

results = pd.DataFrame([
    {
        "Modelo": "Baseline (siempre no-churn)",
        "Precision (Churn)": precision_score(y_test, y_pred_dummy, zero_division=0),
        "Recall (Churn)": recall_score(y_test, y_pred_dummy, zero_division=0),
    },
    {
        "Modelo": "Regresion Logistica",
        "Precision (Churn)": precision_score(y_test, y_pred_lr, zero_division=0),
        "Recall (Churn)": recall_score(y_test, y_pred_lr, zero_division=0),
    },
    {
        "Modelo": "Random Forest",
        "Precision (Churn)": precision_score(y_test, y_pred_rf, zero_division=0),
        "Recall (Churn)": recall_score(y_test, y_pred_rf, zero_division=0),
    },
])

print(results.to_string(index=False))

# %% [markdown]
# ## Matrices de confusion
#
# Ver la matriz de confusion ayuda a entender rapidamente donde se equivoca cada
# modelo: si deja escapar churn reales o si dispara alertas de mas.

# %%
from sklearn.metrics import ConfusionMatrixDisplay

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

model_outputs = [
    ("Baseline", y_pred_dummy),
    ("Regresion Logistica", y_pred_lr),
    ("Random Forest", y_pred_rf),
]

for ax, (title, y_pred) in zip(axes, model_outputs):
    ConfusionMatrixDisplay.from_predictions(
        y_test,
        y_pred,
        display_labels=["No churn", "Churn"],
        cmap="Blues",
        ax=ax,
        colorbar=False,
    )
    ax.set_title(title)

plt.tight_layout()
plt.show()

# %% [markdown]
# ## Resumen simple

# %%
best_model = results.sort_values("Recall (Churn)", ascending=False).iloc[0]

print("=" * 60)
print("RESUMEN DE RESULTADOS")
print("=" * 60)
print(results.to_string(index=False))
print()
print(
    f"Mejor recall: {best_model['Modelo']} "
    f"({best_model['Recall (Churn)']:.2%})"
)

# %%
