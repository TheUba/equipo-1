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
# # 01 — Descarga y exploracion del dataset
#
# Dataset: Telco Customer Churn (Hugging Face)
# Fuente: https://huggingface.co/datasets/aai510-group1/telco-customer-churn

# %% [markdown]
# ## Descarga del dataset

# %%
from datasets import load_dataset
import pandas as pd

dataset = load_dataset("aai510-group1/telco-customer-churn")
df = dataset["train"].to_pandas()

# Guardar copia local en CSV
df.to_csv("../data/raw/telco_churn.csv", index=False)
print(f"Dataset descargado: {df.shape[0]} filas, {df.shape[1]} columnas")

# %% [markdown]
# ## Vista general

# %%
df.head()

# %%
df.info()

# %%
df.describe()

# %% [markdown]
# ## Variable target: Churn

# %%
print(df["Churn"].value_counts())
print(f"\nTasa de churn: {df['Churn'].mean():.2%}")

# %% [markdown]
# ## Valores faltantes

# %%
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_report = pd.DataFrame({"faltantes": missing, "porcentaje": missing_pct})
missing_report[missing_report["faltantes"] > 0].sort_values("porcentaje", ascending=False)

# %% [markdown]
# ## Distribuciones principales

# %%
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

sns.histplot(df["Tenure in Months"], kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Tenure (meses)")

sns.histplot(df["Monthly Charge"], kde=True, ax=axes[0, 1])
axes[0, 1].set_title("Cargo mensual")

sns.histplot(df["Total Revenue"], kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Revenue total")

sns.countplot(x="Churn", data=df, ax=axes[1, 1])
axes[1, 1].set_title("Distribucion de Churn")

plt.tight_layout()
plt.show()

# %% [markdown]
# ## Churn por tipo de contrato

# %%
churn_by_contract = df.groupby("Contract")["Churn"].mean().sort_values(ascending=False)
print(churn_by_contract)
print()

fig, ax = plt.subplots(figsize=(8, 4))
churn_by_contract.plot(kind="bar", ax=ax)
ax.set_title("Tasa de churn por tipo de contrato")
ax.set_ylabel("Tasa de churn")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# %%
