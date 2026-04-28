# Glosario operativo para la Etapa 2

## Objetivo

Este documento funciona como una referencia rapida para recordar herramientas, metricas, modelos y tecnicas utiles durante la **Etapa 2 — Notebooks**.

No esta organizado por tipo de problema, sino por concepto.

La idea es responder rapido:

- que es esto
- para que sirve
- cuando conviene usarlo
- cuando no conviene

---

## 1. Baselines

## Baseline

### Que es

Un punto de referencia simple contra el cual medimos si una solucion agrega valor.

### Para que sirve

- saber si el modelo mejora algo real
- evitar celebrar resultados sin contexto
- anclar despues la narrativa de negocio

### Cuando conviene

Siempre.

### Cuando no conviene omitirlo

Nunca conviene omitirlo.

## Clase mayoritaria

### Que es

En clasificacion, predecir siempre la clase mas frecuente.

### Para que sirve

Baseline rapido y explicable.

### Cuando conviene

- churn
- fraude
- riesgo

### Cuando no alcanza

Cuando el problema exige algo mas que accuracy, especialmente si la clase positiva importa mucho.

## Promedio de ultimas N observaciones

### Que es

En forecasting, usar el promedio reciente como forecast simple.

### Para que sirve

Comparar contra una regla ingenua pero razonable.

### Cuando conviene

- demanda
- ventas
- tickets
- series temporales cortas

### Cuando no alcanza

Cuando hay tendencia, promociones o estacionalidad que esa regla no captura.

---

## 2. Modelos

## Regresion Logistica

### Que es

Modelo lineal para clasificacion.

### Para que sirve

- baseline inteligente en clasificacion
- comparar contra modelos mas complejos
- tener una opcion interpretable

### Cuando conviene

- churn
- fraude
- riesgo
- cualquier clasificacion binaria defendible

### Cuando no conviene como unica opcion

Cuando sospechas relaciones no lineales fuertes.

## Random Forest

### Que es

Conjunto de arboles de decision que votan o promedian.

### Para que sirve

- capturar relaciones no lineales
- manejar bien datos tabulares
- ofrecer importancias de variables

### Cuando conviene

- churn
- fraude
- regresion tabular
- forecasting simple basado en features derivadas

### Cuando no conviene

- cuando la interpretabilidad tiene que ser muy alta
- cuando el problema exige una estructura temporal mas especializada

## Regresion Lineal

### Que es

Modelo lineal para variables continuas.

### Para que sirve

- baseline inteligente en regresion
- forecasting simple con lags
- pricing o revenue cuando la relacion es aproximadamente lineal

### Cuando conviene

- pricing
- estimacion de demanda simple
- revenue

### Cuando no conviene como unica opcion

Cuando la relacion entre variables es claramente no lineal.

## Random Forest Regressor

### Que es

Version de random forest para prediccion de valores continuos.

### Para que sirve

- mejorar regresiones simples
- capturar no linealidad sin mucha complejidad conceptual extra

### Cuando conviene

- pricing
- forecasting con features tabulares
- demanda

### Cuando no conviene

- cuando necesitas extrapolar tendencia muy lejos en el tiempo
- cuando el problema temporal exige un modelo especializado

## Reglas heuristicas / score manual

### Que es

Sistema de reglas creado a mano.

### Para que sirve

- baseline en ranking o recomendacion
- comparacion inicial antes de modelos supervisados

### Cuando conviene

- recomendacion
- priorizacion de leads
- ranking de acciones

### Cuando no conviene como solucion final

Cuando el problema requiere personalizacion real o mejora sostenida.

## Red neuronal multicapa (MLP)

### Que es

Una red neuronal artificial feed-forward con una o mas capas ocultas.

### Para que sirve

- clasificacion o regresion no lineal
- capturar relaciones mas complejas que un modelo lineal

### Cuando conviene

- cuando ya agotaste modelos tabulares mas simples
- cuando la complejidad extra esta justificada por una mejora clara

### Cuando no conviene

- en demos rapidos donde no podes defender bien el modelo
- cuando la interpretabilidad importa mucho
- cuando un modelo mas simple ya resuelve el caso

## LSTM / RNN

### Que es

Familia de redes neuronales pensadas para datos secuenciales o temporales.

### Para que sirve

- modelar dependencias temporales
- forecasting mas complejo
- secuencias de texto o eventos

### Cuando conviene

- cuando la estructura secuencial es central
- cuando un enfoque tabular con lags ya no alcanza

### Cuando no conviene

- en demos iniciales si no tenes claro por que supera a un baseline defendible
- cuando el dataset es pequeno o el problema se resuelve bien con tecnicas mas simples

## Transformer

### Que es

Arquitectura de redes neuronales basada en mecanismos de atencion. Es la base de muchos modelos modernos de NLP y tambien aparece en vision y series temporales.

### Para que sirve

- tareas avanzadas de lenguaje natural
- embeddings
- clasificacion de texto
- resumen, extraccion, generacion

### Cuando conviene

- cuando el problema principal es texto
- cuando queres usar un modelo preentrenado en lugar de entrenar desde cero

### Cuando no conviene

- cuando el problema es tabular simple y no justifica esa complejidad
- cuando no podes explicar su uso mas alla de "porque funciona"

## Modelo preentrenado

### Que es

Un modelo que ya fue entrenado previamente por terceros y que se reutiliza tal cual o con adaptaciones menores.

### Para que sirve

- acelerar demos
- resolver tareas complejas sin entrenar desde cero
- aprovechar conocimiento ya encapsulado

### Cuando conviene

- NLP
- embeddings
- clasificacion de texto
- casos donde entrenar desde cero es inviable

### Cuando no conviene

- cuando el problema exige trazabilidad total del entrenamiento
- cuando no tenes claridad sobre limitaciones, sesgos o costo operativo

## LLM

### Que es

Un modelo grande de lenguaje basado normalmente en transformers y preentrenado a gran escala.

### Para que sirve

- clasificar texto
- resumir
- extraer entidades o temas
- generar explicaciones o borradores de narrativa

### Cuando conviene

- cuando el problema involucra texto no estructurado
- cuando usarlo como caja negra es suficiente para un demo exploratorio
- cuando su valor esta en acelerar una solucion, no en entrenar un modelo propio

### Cuando no conviene

- cuando el demo exige trazabilidad tecnica fina del modelo
- cuando la alucinacion o la variabilidad de salida vuelven riesgosa la solucion
- cuando un enfoque simple o deterministico ya alcanza

### Regla practica para este framework

Si usas un LLM, asumilo como **componente externo preentrenado**, no como algo que vas a entrenar en el demo. La pregunta correcta no es "como lo entreno", sino "para que subtarea concreta me sirve y como valido su salida".

---

## 3. Metricas

## Accuracy

### Que es

Porcentaje total de predicciones correctas.

### Formula conceptual

Accuracy = aciertos totales / casos totales

o, en clasificacion:

Accuracy = (verdaderos positivos + verdaderos negativos) / total

### Frase para no olvidarlo

"De todo lo que evaluo el modelo, cuanto acerto en total."

### Ejemplo rapido

Supongamos 100 clientes:

- 95 no se van
- 5 si se van

El modelo predijo 8 clientes como positivos:

- 4 realmente se iban -> verdaderos positivos
- 4 no se iban -> falsos positivos
- quedo 1 cliente que si se iba sin detectar -> falso negativo
- entonces acerto 91 negativos + 4 positivos

Accuracy = (4 + 91) / 100 = 95 => 95%

### Para que sirve

Vista general del rendimiento.

### Cuando conviene

Como metrica secundaria en clasificacion.

### Cuando no conviene usarla sola

Cuando hay clases desbalanceadas.

## Precision

### Que es

De los casos marcados como positivos, cuantos eran realmente positivos.

### Formula conceptual

Precision = verdaderos positivos / positivos predichos

### Frase para no olvidarlo

"De lo que el modelo marco, cuanto era verdad."

### Ejemplo rapido

Usando el mismo ejemplo:

- el modelo marco 8 clientes como positivos
- de esos 8, 4 realmente se iban

Precision = 4 / 8 = 50 => 50%

### Para que sirve

Medir la calidad de las alertas.

### Cuando conviene

- fraude
- riesgo
- churn cuando revisar alertas cuesta mucho

### Cuando no conviene priorizarla sola

Cuando dejar pasar positivos reales es demasiado costoso.

## Recall

### Que es

De los positivos reales, cuantos detecta el modelo.

### Formula conceptual

Recall = verdaderos positivos / positivos reales

### Frase para no olvidarlo

"De lo que era verdad, cuanto encontro el modelo."

### Ejemplo rapido

Usando el mismo ejemplo:

- en la realidad habia 5 clientes que si se iban
- el modelo detecto 4 de esos 5

Recall = 4 / 5 = 80 => 80%

### Para que sirve

Medir capacidad de deteccion.

### Cuando conviene

- churn
- fraude
- cualquier caso donde perder un positivo sea caro

### Cuando no conviene priorizarlo solo

Cuando demasiados falsos positivos vuelven inviable la operacion.

## F1

### Que es

Balance entre precision y recall.

### Para que sirve

Comparar modelos cuando importan ambas cosas.

### Cuando conviene

Como metrica de equilibrio en clasificacion.

### Cuando no conviene usarla sola

Cuando el negocio claramente prioriza precision o recall.

## AUC

### Que es

Medida de que tan bien separa el modelo clases positivas y negativas.

### Para que sirve

Comparar capacidad discriminativa general.

### Cuando conviene

Como metrica tecnica de apoyo en clasificacion.

### Cuando no conviene llevarla sola al front

Cuando no esta traducida a lenguaje de negocio.

## MAE

### Que es

Error absoluto medio.

### Para que sirve

Saber en promedio cuanto se desvian las predicciones.

### Cuando conviene

- forecasting
- pricing
- revenue

### Cuando no conviene usarla sola

Cuando tambien importa penalizar mas los errores grandes.

## RMSE

### Que es

Raiz del error cuadratico medio.

### Para que sirve

Penalizar mas los errores grandes.

### Cuando conviene

- forecasting
- pricing
- cualquier regresion donde errores extremos importan mucho

### Cuando no conviene usarla sola

Cuando queres una explicacion mas intuitiva del error promedio.

## MAPE

### Que es

Error porcentual absoluto medio.

### Para que sirve

Expresar error como porcentaje, muy util para negocio.

### Cuando conviene

- forecasting
- demanda
- ventas

### Cuando no conviene

Cuando hay valores muy cercanos a cero.

## R²

### Que es

Proporcion de variabilidad explicada por el modelo.

### Para que sirve

Medir ajuste general en regresion.

### Cuando conviene

Como apoyo tecnico en pricing o regresion.

### Cuando no conviene llevarla sola al negocio

Cuando nadie puede traducirla a impacto concreto.

## Precision@k / Recall@k

### Que es

Metricas de ranking que miran la calidad del top-k de resultados.

### Para que sirve

Evaluar recomendacion o priorizacion.

### Cuando conviene

- ranking
- recomendacion
- leads prioritarios

### Cuando no conviene

Cuando el problema no es de ranking.

---

## 4. Tecnicas de limpieza y preparacion de datos

## Eliminar columnas con fuga de informacion

### Que es

Quitar variables que contienen informacion que solo existiria despues del evento que queremos predecir.

### Para que sirve

Evitar trampa tecnica.

### Cuando conviene

Siempre que haya sospecha de leakage.

### Cuando no conviene omitirlo

Nunca.

## Eliminar columnas no predictivas

### Que es

Quitar IDs, comentarios libres, metadata o columnas que no agregan señal util.

### Para que sirve

Reducir ruido y sobreajuste.

### Cuando conviene

Siempre que la columna no tenga valor explicativo claro.

## Imputacion con mediana

### Que es

Rellenar faltantes numericos con la mediana.

### Para que sirve

Solucion simple y robusta a outliers.

### Cuando conviene

En el alcance defendible del framework.

### Cuando no conviene

Si la ausencia en si misma tiene significado mas fuerte que el valor imputado.

## Imputacion con valor descriptivo

### Que es

Rellenar faltantes categoricos con una categoria como `Sin servicio` o `Desconocido`.

### Para que sirve

Conservar informacion sobre ausencia.

### Cuando conviene

Cuando el faltante representa una condicion de negocio real.

## One-hot encoding

### Que es

Transformar categorias en columnas binarias.

### Para que sirve

Permitir que modelos tabulares trabajen con categorias.

### Cuando conviene

En demos simples con cardinalidad baja o moderada.

### Cuando no conviene

Con categorias de cardinalidad enorme sin una estrategia mejor pensada.

## Lag features

### Que es

Usar valores pasados como variables explicativas.

### Para que sirve

Forecasting simple y defendible.

### Cuando conviene

- demanda
- ventas
- series temporales

### Cuando no conviene

Si la serie no tiene continuidad temporal suficiente.

## Rolling mean

### Que es

Promedio movil sobre una ventana temporal.

### Para que sirve

Capturar tendencia reciente suavizada.

### Cuando conviene

Forecasting y series temporales simples.

### Cuando no conviene

Si suaviza demasiado una señal donde los picos son importantes.

---

## 5. Tratamiento de outliers

## Winsorization

### Que es

Recortar valores extremos a un limite superior o inferior razonable.

### Para que sirve

Reducir el efecto de outliers extremos sin eliminar registros.

### Cuando conviene

- promociones extremas
- errores de carga evidentes
- variables continuas con valores absurdos

### Cuando no conviene

Cuando el extremo es una señal real importante del negocio.

## Eliminar outliers

### Que es

Quitar registros extremos.

### Para que sirve

Limpiar datos claramente corruptos.

### Cuando conviene

Cuando tenes evidencia de error de captura.

### Cuando no conviene

Cuando el outlier puede ser un caso de negocio real.

## Mantener outliers y documentarlos

### Que es

No tocarlos, pero reconocer que existen.

### Para que sirve

Preservar fenomenos reales del negocio.

### Cuando conviene

Cuando los extremos son parte del problema y no errores.

---

## 6. Artefactos visuales

## Baseline comparison

### Que es

Comparacion visual entre baseline, modelo simple y modelo final.

### Para que sirve

Mostrar si realmente hubo mejora.

### Cuando conviene

Siempre que haya baseline.

### Cuando puede ir al front

Casi siempre.

## Top drivers / feature importance

### Que es

Visual de variables mas influyentes.

### Para que sirve

Responder "por que el modelo dice esto".

### Cuando conviene

- churn
- fraude
- pricing
- forecasting con features tabulares

### Cuando puede ir al front

Si es simple y entendible.

## Matriz de confusion

### Que es

Tabla de aciertos y errores en clasificacion.

### Para que sirve

Entender donde falla el modelo.

### Cuando conviene

Clasificacion.

### Cuando puede ir al front

Solo simplificada.

## Forecast vs actual

### Que es

Comparacion entre valores observados y proyectados.

### Para que sirve

Mostrar comportamiento temporal de la prediccion.

### Cuando conviene

Forecasting.

### Cuando puede ir al front

Casi siempre, como visual principal.

## Escenarios

### Que es

Comparacion de opciones o bandas posibles.

### Para que sirve

Pricing, revenue, planeamiento.

### Cuando conviene

Cuando el caso exige comparar decisiones y no solo predecir un valor.

### Cuando puede ir al front

Muy bien, si se presenta claro.

---

## 7. Que suele quedarse en notebooks

Normalmente quedan en notebooks:

- histogramas exploratorios
- residuos detallados
- correlaciones tecnicas
- tablas largas de errores
- experimentos descartados
- graficos tecnicos sin traduccion de negocio

No porque sean inutiles, sino porque sirven para pensar tecnicamente, no para contar el caso.

---

## 8. Que suele escalar al demo

Normalmente escalan bien al demo:

- baseline comparison
- top drivers
- confusion simplificada
- forecast vs actual
- escenarios
- metricas traducidas

La regla es simple:

si el artefacto ayuda a explicar problema, evidencia, confianza o accion, puede escalar al demo.

---

## 9. Preguntas rapidas de uso

### ¿No se que baseline elegir?

Elegí la regla mas simple que una persona del negocio podria entender y aplicar hoy.

### ¿No se que modelo comparar?

Usá uno simple e interpretable y uno un poco mas potente pero todavia defendible.

### ¿No se que metrica mostrar?

Elegí la que mejor responda la decision de negocio, no la mas famosa.

### ¿No se que visual llevar al front?

Llevá el que mejor responda una de estas preguntas:

- ¿mejora algo?
- ¿por que?
- ¿como se ve en la practica?

### ¿No se si una tecnica conviene?

Si no podes explicarla con claridad tecnica y de negocio, probablemente todavia no conviene usarla en este framework.
