# Ficha Tecnica

## Resumen

Prediccion de abandono de clientes en una empresa de telecomunicaciones mediante clasificacion binaria con Random Forest, logrando 96.23% de precision y 91.07% de recall sobre la clase de churn.

## Tipo de problema

Clasificacion binaria

## Dataset

### Fuente y volumen

- Fuente: Telco Customer Churn (Hugging Face — aai510-group1/telco-customer-churn)
- Registros: ~7,000 clientes
- Split: 80% train (4,230 filas) / 20% test (846 filas), estratificado
- Tasa de churn en el dataset: ~26.5%

### Features relevantes

Despues de limpiar columnas con fuga de informacion y columnas no predictivas, el modelo trabajo con ~30 features agrupadas en:

- **Satisfaccion**: Satisfaction Score (factor dominante, 0.48 de importancia)
- **Antiguedad y facturacion**: Tenure in Months, Monthly Charge, Total Charges, Total Revenue
- **Tipo de contrato y pago**: Contract (Month-to-Month, One Year, Two Year), Payment Method
- **Servicios contratados**: Internet Service, Internet Type, Phone Service, Streaming, Online Security, Online Backup, Device Protection, Premium Tech Support
- **Demograficas**: Age, Gender, Married, Dependents, Senior Citizen

### Calidad de datos

- Algunos valores faltantes en columnas categoricas relacionadas a servicios (cuando el cliente no tiene ese servicio contratado). Rellenados con "Sin servicio".
- Sin duplicados ni inconsistencias mayores.
- Columnas eliminadas por fuga de informacion: Churn Category, Churn Reason, Churn Score, Customer Status, CLTV.
- Columnas eliminadas por no ser predictivas: Customer ID, City, State, Country, Zip Code, coordenadas geograficas, Population, Quarter.

## Estado de datos y prerequisitos

Sin observaciones (dataset publico, listo para uso).

En un escenario real con una empresa de telecomunicaciones, se necesitaria acceso a: sistema de facturacion (tenure, cargos), CRM (tipo de contrato, servicios), y algun mecanismo de satisfaccion del cliente (NPS, CSAT, encuestas). Si la empresa no recopila satisfaccion de cliente de manera sistematica, se recomendaria implementar al menos un NPS trimestral, dado que es el factor predictivo mas fuerte.

## Approach tecnico

### Metodo elegido

Random Forest (100 estimadores) con one-hot encoding para variables categoricas y split estratificado.

### Justificacion

- Captura relaciones no lineales entre features sin requerir escalado
- Provee feature importance nativa, lo cual es clave para comunicar al negocio POR QUE un cliente esta en riesgo
- Performance superior a Regresion Logistica en este caso (+2.2% precision, +0.4% recall)
- Robusto ante features irrelevantes y outliers

### Alternativas descartadas

- **Regresion Logistica**: se evaluo como segundo baseline. Precision 93.98%, Recall 90.63%. Buenos resultados y mas interpretable, pero Random Forest fue ligeramente superior en ambas metricas. En un escenario donde la interpretabilidad sea critica, Regresion Logistica seria una alternativa valida.
- **Gradient Boosting / XGBoost**: no se evaluo en esta iteracion. Seria el siguiente paso si se necesita exprimir mas performance, pero la mejora marginal probablemente no justifique la complejidad adicional dado los resultados actuales.

## Metricas y resultados

### Baseline

Clasificador dummy que siempre predice la clase mayoritaria (no-churn): 0% recall en churn. Esto representa "no hacer nada" — asumir que ningun cliente se va.

### Metricas de evaluacion

- **Precision (Churn)**: de los que el modelo marca como riesgo, cuantos realmente se van
- **Recall (Churn)**: de los que realmente se van, cuantos detecta el modelo

Se priorizo el recall por sobre la precision: en churn, es mejor alertar de mas (falso positivo = llamar a un cliente que estaba bien) que dejar pasar un cliente que se va (falso negativo = perder revenue).

### Resultados obtenidos

| Modelo | Precision (Churn) | Recall (Churn) |
|---|---|---|
| Baseline (siempre no-churn) | 0.00% | 0.00% |
| Regresion Logistica | 93.98% | 90.63% |
| Random Forest | 96.23% | 91.07% |

## Limitaciones y supuestos

- El dataset es de una sola empresa de telecomunicaciones en California. Los patrones no necesariamente generalizan a otras geografias o industrias.
- Satisfaction Score domina la prediccion (0.48 de importancia). Si una empresa no recopila esa metrica, el modelo perderia su feature mas fuerte y los resultados serian significativamente diferentes.
- No se implemento validacion cruzada — los resultados son sobre un unico split 80/20. Para produccion se recomendaria k-fold CV.
- El modelo no fue optimizado con hyperparameter tuning. Los resultados son con parametros por defecto.
- No se evaluo el comportamiento temporal del modelo (drift). En produccion, el modelo deberia reentrenarse periodicamente.

## Stack

- Python 3.12.13 (uv)
- pandas, numpy — manipulacion de datos
- scikit-learn 1.8.0 — modelos y evaluacion
- matplotlib, seaborn — visualizacion
- jupytext — notebooks en formato percent
- uv — gestion de dependencias
- datasets (Hugging Face) — descarga del dataset
