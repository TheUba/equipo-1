# Guia base para la Etapa 2 — Notebooks

## Objetivo

Esta guia define un criterio base para trabajar la **Etapa 2 — Notebooks** sin empezar de cero en cada proyecto.

No es un formulario para completar mecanicamente. Es una referencia para decidir con criterio:

- que baseline usar
- que modelos comparar
- que metricas tienen sentido
- que artefactos visuales producir
- que cosas sirven solo para trabajo tecnico
- que cosas vale la pena llevar luego al front

## Principio general

La Etapa 2 debe producir una salida tecnica **defendible, estructurada y reutilizable**.

Eso significa:

1. partir de un baseline simple
2. comparar contra al menos un modelo mas inteligente
3. elegir metricas coherentes con el tipo de problema
4. producir artefactos tecnicos que luego puedan alimentar ficha tecnica, narrativa y demo

## Regla de alcance

Esta guia asume el alcance defendible ya definido en `docs/guide.md`:

- exploracion basica
- preparacion simple
- baseline
- modelo simple
- modelo mas complejo
- comparacion clara
- visuales minimos

Queda fuera por defecto:

- tuning avanzado
- stacking
- SMOTE y tecnicas complejas de balanceo
- validacion cruzada avanzada
- visuales tecnicos que no aportan a negocio

---

## Estructura minima esperada de la Etapa 2

La salida de notebooks deberia poder resumirse en algo de esta forma:

```yaml
notebook_outputs:
  dataset_summary: {}
  preprocessing: {}
  baseline: {}
  model_candidates: []
  selected_model: ""
  model_rationale: []
  visual_artifacts: {}
```

No hace falta que siempre tenga exactamente esos nombres, pero SI debe existir una salida equivalente.

---

## Como pensar el baseline

El baseline no es un adorno. Es el punto de referencia sin el cual no se puede decir si la solucion aporta valor.

### Regla practica

El baseline debe ser:

- simple
- explicable
- razonable para el tipo de problema

### Ejemplos por tipo de problema

#### Churn / clasificacion binaria

- predecir siempre la clase mayoritaria
- usar una regla de negocio simple si existe

Ejemplo:

- "asumir que ningun cliente se va"

#### Forecasting de demanda

- promedio de ultimas N semanas
- ultima observacion conocida
- promedio de mismo periodo anterior

Ejemplo:

- `last_4_weeks_average`

#### Pricing / regresion

- promedio historico
- precio actual como estimacion constante
- regla lineal simple

#### Recomendacion / ranking

- items mas populares
- ranking fijo por ventas historicas
- recomendacion no personalizada

#### Fraude / deteccion de riesgo

- clasificar todo como no fraude
- regla heuristica simple del negocio

### Pregunta de control

Si no podes explicar el baseline en una frase simple, probablemente no es un buen baseline.

---

## Como elegir modelos candidatos

La idea NO es probar todo. La idea es comparar inteligentemente.

### Regla minima

Siempre comparar:

1. baseline
2. un modelo simple
3. un modelo algo mas potente pero todavia defendible

### Modelos sugeridos por tipo de problema

## 1. Churn / clasificacion

### Baseline
- clase mayoritaria

### Modelo simple
- Regresion Logistica

### Modelo mas potente pero defendible
- Random Forest

### Comentario

Esta combinacion es muy buena para demos porque:

- la regresion logistica es interpretable
- random forest agrega capacidad no lineal
- la comparacion es clara

## 2. Forecasting de demanda

### Baseline
- promedio ultimas semanas
- naive forecast

### Modelo simple
- Regresion Lineal con lags y rolling means

### Modelo mas potente pero defendible
- Random Forest Regressor

### Comentario

No hace falta empezar con Prophet, XGBoost o modelos avanzados de series temporales. Primero hay que demostrar que una solucion simple ya mejora una referencia naive.

## 3. Pricing / regresion

### Baseline
- promedio historico
- precio actual fijo

### Modelo simple
- Regresion Lineal

### Modelo mas potente pero defendible
- Random Forest Regressor

### Comentario

La comparacion sirve para ver si la no linealidad realmente agrega valor o si una relacion lineal ya alcanza.

## 4. Recomendacion / ranking

### Baseline
- top populares

### Modelo simple
- score por reglas (popularidad + recencia + categoria)

### Modelo mas potente pero defendible
- ranking supervisado simple o afinidad basada en features

### Comentario

En demos iniciales, muchas veces una buena heuristica supera en claridad a un modelo complejo. Eso esta bien.

## 5. Fraude / riesgo

### Baseline
- siempre no fraude

### Modelo simple
- Regresion Logistica

### Modelo mas potente pero defendible
- Random Forest

### Comentario

La diferencia contra churn es que aca la precision suele pesar mas, porque los falsos positivos cuestan revision manual.

---

## Como elegir metricas

La metrica depende del tipo de problema y de la decision de negocio.

## 1. Churn / clasificacion

### Metricas utiles
- accuracy
- precision
- recall
- F1
- AUC

### Que suele importar mas
- recall cuando perder un caso es caro
- precision cuando revisar falsos positivos es costoso

### Que puede ir al front
- recall traducido
- precision traducida
- comparacion contra baseline

### Que puede quedar tecnico
- classification report completo
- metricas por clase sin traducir

## 2. Forecasting / demanda

### Metricas utiles
- MAE
- RMSE
- MAPE

### Que suele importar mas
- error promedio interpretable
- estabilidad del forecast

### Que puede ir al front
- error promedio traducido
- comparacion de error contra baseline
- desvio esperado en lenguaje de negocio

### Que puede quedar tecnico
- detalles de residuos
- analisis de error por corte muy fino

## 3. Pricing / regresion

### Metricas utiles
- MAE
- RMSE
- R²

### Que suele importar mas
- error absoluto promedio
- diferencia frente a baseline

### Que puede ir al front
- error promedio traducido a dinero
- escenarios comparados

### Que puede quedar tecnico
- residuos detallados
- distribuciones de error demasiado finas

## 4. Recomendacion / ranking

### Metricas utiles
- precision@k
- recall@k
- hit rate
- uplift si existe experimento

### Que suele importar mas
- capacidad de poner items relevantes arriba

### Que puede ir al front
- mejora contra popularidad simple
- top items o top segmentos

### Que puede quedar tecnico
- metricas por usuario muy detalladas

## 5. Fraude / riesgo

### Metricas utiles
- precision
- recall
- F1
- AUC

### Que suele importar mas
- precision si el costo de falsa alarma es alto
- recall si el costo de fuga es alto

### Que puede ir al front
- porcentaje de alertas utiles
- porcentaje de fraude detectado

### Que puede quedar tecnico
- curvas y thresholds detallados

---

## Artefactos visuales sugeridos

Estos artefactos se producen en notebooks. Algunos despues alimentan el front y otros sirven solo para trabajo tecnico.

## Regla general

Cada visual debe responder una pregunta.

Si no responde una pregunta clara, sobra.

## 1. Churn / clasificacion

### Visuales utiles en notebooks
- distribucion del target
- comparacion de modelos
- top drivers
- matriz de confusion

### Visuales que conviene llevar al front
- comparacion contra baseline
- top drivers
- matriz de confusion simplificada

### Visuales que suelen quedarse en notebooks
- histogramas exploratorios
- correlaciones tecnicas
- tablas largas de errores

## 2. Forecasting

### Visuales utiles en notebooks
- serie historica
- forecast vs actual
- comparacion de error entre modelos
- factores o supuestos clave

### Visuales que conviene llevar al front
- serie temporal principal
- comparacion contra baseline
- drivers o supuestos principales

### Visuales que suelen quedarse en notebooks
- residuos detallados
- descomposiciones tecnicas complejas

## 3. Pricing / regresion

### Visuales utiles en notebooks
- real vs predicho
- comparacion de error
- escenarios de precio
- top drivers

### Visuales que conviene llevar al front
- escenarios comparados
- mejora frente a baseline
- drivers principales

### Visuales que suelen quedarse en notebooks
- scatter plots tecnicos sin contexto
- residuos detallados

## 4. Recomendacion / ranking

### Visuales utiles en notebooks
- top items por score
- comparacion con populares
- rendimiento por segmento

### Visuales que conviene llevar al front
- top items / top segmentos
- uplift o mejora frente a baseline

### Visuales que suelen quedarse en notebooks
- matrices muy tecnicas
- detalles por usuario individual

## 5. Fraude / riesgo

### Visuales utiles en notebooks
- comparacion de modelos
- top señales de fraude
- matriz de confusion

### Visuales que conviene llevar al front
- top señales
- comparacion contra baseline
- confusion simplificada

### Visuales que suelen quedarse en notebooks
- curvas tecnicas avanzadas
- thresholds detallados

---

## Que deberia salir de notebooks y que no

## Si deberia salir de notebooks

- resumen del dataset
- decisiones de preprocessing
- baseline
- comparacion de modelos
- modelo seleccionado
- justificacion de seleccion
- metricas finales
- artefactos visuales estructurados

## No deberia salir de notebooks como salida final

- copy comercial definitivo
- recomendaciones ejecutivas finales redactadas
- decisiones de UI
- textos de venta listos para cliente

Eso se resuelve despues en:

- `technical-brief.md`
- `business-narrative.md`
- `demo/config/demo.yaml`
- `demo/results/analysis.yaml`

---

## Plantilla de salida sugerida

```yaml
notebook_outputs:
  dataset_summary:
    rows: 0
    columns: 0
    target: ""
  preprocessing:
    dropped_columns: []
    missing_strategy: ""
    derived_features: []
  baseline:
    label: ""
    metrics: {}
  model_candidates:
    - label: ""
      metrics: {}
    - label: ""
      metrics: {}
  selected_model: ""
  model_rationale: []
  visual_artifacts: {}
```

Esta plantilla no reemplaza el trabajo de notebooks. Solo da una forma minima para capturar su salida.

---

## Preguntas de control antes de cerrar la Etapa 2

1. ¿El baseline es realmente simple y explicable?
2. ¿Los modelos comparados tienen sentido para este tipo de problema?
3. ¿Las metricas elegidas responden a la decision de negocio?
4. ¿Hay al menos un artefacto visual que luego pueda ir al front?
5. ¿Se puede explicar por que se eligio el modelo final?
6. ¿La salida de notebooks se puede traducir a ficha tecnica sin inventar nada?
7. ¿La narrativa futura podria apoyarse en estos resultados sin humo?

Si alguna de estas preguntas no puede responderse bien, la Etapa 2 no esta lista para pasar a la Etapa 3.

---

## Regla final

La Etapa 2 no existe para producir el mejor modelo posible.

Existe para producir una salida tecnica:

- suficiente para resolver el caso
- defendible por quien presenta el demo
- reutilizable por la ficha tecnica
- traducible a narrativa de negocio
- estructurable para API y UI

Si cumple eso, entonces esta bien resuelta dentro del framework.
