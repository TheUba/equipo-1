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
# Objetivo: entrenar un modelo de clasificacion binaria para predecir churn,
# comparar contra un baseline, y evaluar con metricas relevantes para el negocio.

# %% [markdown]
# ## Carga de datos procesados

# %%
import pandas as pd
import numpy as np

X_train = pd.read_csv("../data/processed/X_train.csv")
X_test = pd.read_csv("../data/processed/X_test.csv")
y_train = pd.read_csv("../data/processed/y_train.csv").squeeze()
y_test = pd.read_csv("../data/processed/y_test.csv").squeeze()

print(f"Train: {X_train.shape[0]} filas, {X_train.shape[1]} features")
print(f"Test:  {X_test.shape[0]} filas")
print(f"Tasa de churn en test: {y_test.mean():.2%}")

# %% [markdown]
# ## Baseline: clasificador "dummy"
#
# Antes de entrenar cualquier modelo, necesitamos un punto de referencia.
# El baseline mas simple es un clasificador que siempre predice la clase
# mayoritaria (no-churn). Esto nos dice: "si no hicieramos NADA inteligente,
# que tan bien nos iria?"
#
# Cualquier modelo que no supere este baseline no aporta valor.

# %%
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, classification_report

dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)
y_pred_dummy = dummy.predict(X_test)

accuracy_baseline = accuracy_score(y_test, y_pred_dummy)
print(f"Accuracy del baseline (predecir siempre no-churn): {accuracy_baseline:.2%}")
print()
print("Classification report del baseline:")
print(classification_report(y_test, y_pred_dummy, target_names=["No churn", "Churn"]))

# %% [markdown]
# ## Modelo 1: Regresion Logistica
#
# Empezamos con el modelo mas simple que podria funcionar.
# La regresion logistica es interpretable, rapida, y sirve como
# segundo punto de referencia antes de probar algo mas complejo.

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Escalar features (la regresion logistica es sensible a la escala)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)

accuracy_lr = accuracy_score(y_test, y_pred_lr)
print(f"Accuracy de Regresion Logistica: {accuracy_lr:.2%}")
print()
print("Classification report:")
print(classification_report(y_test, y_pred_lr, target_names=["No churn", "Churn"]))

# %% [markdown]
# ## Modelo 2: Random Forest
#
# Un paso mas: un modelo basado en arboles que captura relaciones
# no lineales sin necesidad de escalar features.

# %%
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"Accuracy de Random Forest: {accuracy_rf:.2%}")
print()
print("Classification report:")
print(classification_report(y_test, y_pred_rf, target_names=["No churn", "Churn"]))

# %% [markdown]
# ## Comparacion de modelos
#
# La accuracy sola no alcanza para un problema de churn. Lo que le importa
# al negocio es:
# - **Precision (Churn)**: de los que el modelo marca como "en riesgo", cuantos realmente se van
# - **Recall (Churn)**: de los que realmente se van, cuantos detectamos a tiempo
#
# En churn, el recall suele ser mas importante que la precision — es mejor
# alertar de mas que dejar pasar clientes que se van.

# %%
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

models = {
    "Baseline (siempre no-churn)": (y_pred_dummy, dummy),
    "Regresion Logistica": (y_pred_lr, lr),
    "Random Forest": (y_pred_rf, rf),
}

results = []
for name, (y_pred, model) in models.items():
    # Para AUC necesitamos probabilidades, el dummy no las tiene utiles
    if hasattr(model, "predict_proba"):
        if name == "Regresion Logistica":
            y_proba = model.predict_proba(X_test_scaled)[:, 1]
        else:
            y_proba = model.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, y_proba)
    else:
        auc = np.nan

    results.append({
        "Modelo": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision (Churn)": precision_score(y_test, y_pred, zero_division=0),
        "Recall (Churn)": recall_score(y_test, y_pred, zero_division=0),
        "F1 (Churn)": f1_score(y_test, y_pred, zero_division=0),
        "AUC": auc,
    })

results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))

# %% [markdown]
# ## Features mas importantes (Random Forest)
#
# Entender QUE variables pesan mas en la prediccion es clave tanto
# para validar que el modelo tiene sentido como para comunicar
# al cliente por que ciertos clientes estan en riesgo.

# %%
feature_importance = pd.DataFrame({
    "feature": X_train.columns,
    "importance": rf.feature_importances_
}).sort_values("importance", ascending=False)

print("Top 10 features mas importantes:")
print(feature_importance.head(10).to_string(index=False))

fig, ax = plt.subplots(figsize=(10, 6))
top_features = feature_importance.head(15)
ax.barh(top_features["feature"], top_features["importance"])
ax.invert_yaxis()
ax.set_title("Top 15 features — Random Forest")
ax.set_xlabel("Importancia")
plt.tight_layout()
plt.show()

# %% [markdown]
# ## Matriz de confusion (mejor modelo)

# %%
from sklearn.metrics import ConfusionMatrixDisplay

fig, ax = plt.subplots(figsize=(6, 5))
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred_rf,
    display_labels=["No churn", "Churn"],
    cmap="Blues",
    ax=ax
)
ax.set_title("Matriz de confusion — Random Forest")
plt.tight_layout()
plt.show()

# %% [markdown]
# ## Resumen de resultados
#
# Estos numeros son los que alimentan la ficha tecnica y, traducidos,
# la narrativa de negocio.

# %%
print("=" * 60)
print("RESUMEN DE RESULTADOS")
print("=" * 60)
print(f"\nMejor modelo: Random Forest")
print(f"Baseline (no hacer nada): {accuracy_baseline:.2%} accuracy")
print()
print(results_df.to_string(index=False))
print()
print("Top 5 factores de riesgo:")
for i, row in feature_importance.head(5).iterrows():
    print(f"  - {row['feature']}: {row['importance']:.4f}")
