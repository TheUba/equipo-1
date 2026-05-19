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
# ## Descripcion breve de columnas
#
# Antes de explorar distribuciones, conviene tener un mapa rapido de que
# representa cada columna del dataset.

# %%
column_descriptions = [
    ("Age", "Edad del cliente."),
    ("Avg Monthly GB Download", "Promedio mensual de GB descargados."),
    ("Avg Monthly Long Distance Charges", "Promedio mensual de cargos por larga distancia."),
    ("Churn", "Etiqueta objetivo: 1 si el cliente abandono, 0 si no."),
    ("Churn Category", "Categoria general del motivo de churn."),
    ("Churn Reason", "Motivo especifico del churn."),
    ("Churn Score", "Score asociado al riesgo o resultado de churn."),
    ("City", "Ciudad del cliente."),
    ("CLTV", "Customer Lifetime Value estimado del cliente."),
    ("Contract", "Tipo de contrato del servicio."),
    ("Country", "Pais del cliente."),
    ("Customer ID", "Identificador unico del cliente."),
    ("Customer Status", "Estado del cliente: activo, churned, etc."),
    ("Dependents", "Indica si el cliente tiene dependientes."),
    ("Device Protection Plan", "Indica si contrato proteccion de dispositivos."),
    ("Gender", "Genero del cliente."),
    ("Internet Service", "Indica si tiene servicio de internet."),
    ("Internet Type", "Tipo de conexion a internet."),
    ("Lat Long", "Coordenadas geograficas combinadas."),
    ("Latitude", "Latitud de la ubicacion del cliente."),
    ("Longitude", "Longitud de la ubicacion del cliente."),
    ("Married", "Indica si el cliente esta casado."),
    ("Monthly Charge", "Cargo mensual del servicio."),
    ("Multiple Lines", "Indica si tiene multiples lineas telefonicas."),
    ("Number of Dependents", "Cantidad de dependientes."),
    ("Number of Referrals", "Cantidad de referidos realizados por el cliente."),
    ("Offer", "Oferta o promocion asociada al cliente."),
    ("Online Backup", "Indica si tiene respaldo online."),
    ("Online Security", "Indica si tiene seguridad online."),
    ("Paperless Billing", "Indica si usa facturacion sin papel."),
    ("Partner", "Indica si tiene pareja."),
    ("Payment Method", "Metodo de pago utilizado."),
    ("Phone Service", "Indica si tiene servicio telefonico."),
    ("Population", "Poblacion de la zona del cliente."),
    ("Premium Tech Support", "Indica si tiene soporte tecnico premium."),
    ("Quarter", "Trimestre de referencia del registro."),
    ("Referred a Friend", "Indica si refirio a un amigo."),
    ("Satisfaction Score", "Puntaje de satisfaccion del cliente."),
    ("Senior Citizen", "Indica si el cliente es adulto mayor."),
    ("State", "Estado o provincia del cliente."),
    ("Streaming Movies", "Indica si usa streaming de peliculas."),
    ("Streaming Music", "Indica si usa streaming de musica."),
    ("Streaming TV", "Indica si usa streaming de TV."),
    ("Tenure in Months", "Antiguedad del cliente en meses."),
    ("Total Charges", "Cargos totales acumulados."),
    ("Total Extra Data Charges", "Cargos acumulados por datos extra."),
    ("Total Long Distance Charges", "Cargos acumulados por larga distancia."),
    ("Total Refunds", "Reembolsos totales recibidos."),
    ("Total Revenue", "Ingresos totales generados por el cliente."),
    ("Under 30", "Indica si el cliente tiene menos de 30 anos."),
    ("Unlimited Data", "Indica si tiene plan de datos ilimitados."),
    ("Zip Code", "Codigo postal del cliente."),
]

data_dictionary = pd.DataFrame(column_descriptions, columns=["columna", "descripcion"])
data_dictionary

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
