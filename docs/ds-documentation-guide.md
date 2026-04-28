# Guia de uso del framework

## Que es esto

Dos templates para documentar cada proyecto de data science desde dos perspectivas complementarias:

- `technical-brief.md` — ficha tecnica para documentacion propia y portfolio
- `business-narrative.md` — narrativa orientada a venta y comunicacion con clientes

## Flujo de trabajo

### 1. Copiar los templates al proyecto

Para cada proyecto nuevo, copiar ambos archivos en la carpeta del proyecto y completarlos a medida que se avanza.

### 2. Completar la ficha tecnica primero

La ficha tecnica se completa DURANTE el desarrollo del proyecto, no al final. Si la dejamos para despues, perdemos las decisiones tecnicas y el razonamiento que las motivo.

Orden sugerido:

1. **Resumen y tipo de problema** — al inicio, cuando se define que se va a resolver
2. **Dataset** — cuando se exploran los datos por primera vez
3. **Estado de datos y prerequisitos** — al hacer el diagnostico inicial del cliente
4. **Approach tecnico** — cuando se elige el camino a seguir
5. **Metricas y resultados** — cuando se tienen resultados evaluables
6. **Limitaciones y supuestos** — al cerrar, con honestidad
7. **Stack** — al cerrar, como registro

### 3. Completar la narrativa de negocio despues

La narrativa de negocio se escribe DESPUES de tener resultados. No antes. Necesitamos datos reales o al menos estimaciones solidas para que tenga peso.

Orden sugerido:

1. **El problema** — reescribir el problema tecnico en lenguaje del cliente
2. **El costo de no actuar** — cuantificar o estimar el impacto de no hacer nada
3. **La solucion** — traducir el approach a resultado de negocio
4. **Resultados concretos** — usar los datos de la ficha tecnica pero expresados como impacto
5. **Traduccion de metricas** — forzarse a explicar cada metrica en lenguaje llano
6. **Cimientos necesarios** — solo si aplica, basandose en el diagnostico de la ficha tecnica
7. **Proximos pasos** — siempre cerrar con una accion

## Como completar cada seccion

### Ficha tecnica

#### Resumen

Escribir UNA oracion. Si necesitas mas de una, todavia no entiendes el problema lo suficiente. Formato sugerido: "Problema X resuelto mediante approach Y para lograr Z".

#### Tipo de problema

Elegir una categoria principal. Si el proyecto combina multiples tipos (ej: clustering + clasificacion), indicar ambos pero marcar cual es el principal.

Categorias comunes:
- Clasificacion (binaria o multiclase)
- Regresion
- Clustering / segmentacion
- Forecasting / series temporales
- Ranking / recomendacion
- NLP / procesamiento de texto
- Deteccion de anomalias
- Optimizacion

#### Dataset

Ser especifico. "Datos de clientes" no alcanza. Documentar:
- Fuente real (CRM, CSV exportado, API, base de datos)
- Volumen (filas, periodo temporal, granularidad)
- Features que realmente importaron para el resultado
- Problemas encontrados en la calidad (nulls, duplicados, inconsistencias)

#### Estado de datos y prerequisitos

Esta seccion existe para documentar la REALIDAD del cliente, no la ideal. Tres escenarios posibles:

1. **El cliente tiene datos listos** — escribir "Sin observaciones" y seguir
2. **El cliente tiene datos pero con problemas** — documentar que se encontro y que se recomendo mejorar
3. **El cliente no tiene infraestructura de datos minima** — documentar el diagnostico y la recomendacion. Esto puede significar que el proyecto de DS se pospone hasta que los cimientos existan

Ser descriptivo pero no prescriptivo: el objetivo es registrar que se encontro y que se sugirio, no disenar la infraestructura del cliente.

#### Approach tecnico

La justificacion es MAS importante que el nombre del modelo. Documentar:
- Que se eligio
- POR QUE se eligio (simplicidad, interpretabilidad, performance, restricciones del cliente)
- Que alternativas se consideraron y por que se descartaron

Si la eleccion fue "empece con lo mas simple y funciono", eso es una justificacion perfectamente valida.

#### Metricas y resultados

Siempre incluir un BASELINE. Un modelo con 90% de accuracy no significa nada sin saber que la regla mas simple da 85%. Documentar:
- Contra que se compara (regla simple, modelo anterior, heuristica del negocio, azar)
- Que metricas se eligieron y por que esas y no otras
- Resultados numericos concretos

#### Limitaciones y supuestos

Ser honesto. Documentar:
- Que asumimos como verdadero que podria no serlo
- Bajo que condiciones los resultados son validos
- Que pasa si cambian los datos o el contexto
- Que NO puede hacer esta solucion

#### Stack

Registro pragmatico. Listar lo que alguien necesitaria saber para reproducir o continuar el proyecto.

### Narrativa de negocio

#### El problema

La regla de oro: si le lees esta seccion al cliente y no asiente con la cabeza, la reescribis. Cero jerga tecnica. Hablar del dolor del negocio, no del tipo de algoritmo.

Mal: "La empresa presenta un problema de clasificacion binaria con desbalance de clases en la variable target de churn."

Bien: "Cada mes, un grupo de clientes deja de usar el servicio sin aviso previo. Cuando el equipo se da cuenta, ya es tarde para retenerlos."

#### El costo de no actuar

Cuantificar genera urgencia real. Ejemplos de enfoques:
- Costo directo: "Cada cliente perdido representa $X de ingreso anual"
- Costo de oportunidad: "El equipo dedica Y horas semanales a tareas que podrian automatizarse"
- Costo de error: "Las decisiones manuales aciertan Z% de las veces"

Si no hay datos exactos, estimar con transparencia: "Basado en el volumen reportado, estimamos que..."

#### La solucion

Describir QUE HACE, no COMO funciona. Al cliente no le importa el algoritmo, le importa el resultado.

Mal: "Se entreno un modelo de gradient boosting con validacion cruzada estratificada."

Bien: "El sistema analiza las senales de comportamiento de cada cliente y genera una lista priorizada de quienes tienen mayor riesgo de irse, para que el equipo pueda actuar antes de perderlos."

#### Resultados concretos

Usar numeros siempre que sea posible. Diferenciar entre:
- Resultados reales del proyecto (medidos, verificables)
- Estimaciones basadas en datos del proyecto (proyecciones razonables)
- Marcos de referencia de la industria (cuando no hay datos propios)

Ser transparente sobre cual es cual.

#### Traduccion de metricas

Esta seccion es el PUENTE entre la ficha tecnica y el mundo del cliente. La tabla debe completarse para cada metrica relevante del proyecto.

Ejemplos de traducciones:

| Metrica tecnica | Significado para el negocio |
|---|---|
| Precision 0.78 | De cada 10 alertas que genera el sistema, casi 8 son realmente clientes en riesgo |
| Recall 0.82 | De cada 10 clientes que efectivamente se van, el modelo detecta 8 antes de que ocurra |
| RMSE $1,200 | El error promedio en la estimacion de precio es de $1,200 |
| AUC 0.91 | El modelo distingue bien entre clientes que se van y los que se quedan |

Si no sabes como traducir una metrica, preguntate: "Si el cliente me pregunta 'y eso que significa para mi?', que le respondo?"

#### Cimientos necesarios

Completar SOLO si aplica. Esta seccion conecta directamente con "Estado de datos y prerequisitos" de la ficha tecnica, pero traducida a lenguaje de decision:

- Que necesita el cliente (sin jerga)
- Por que lo necesita (en terminos de valor, no de tecnologia)
- Que pasa si no lo hace (riesgo o limitacion concreta)

#### Proximos pasos

Siempre cerrar con UNA accion clara y concreta. No una lista de deseos, una accion.

Ejemplos:
- "Agendar una reunion de 30 minutos para revisar estos resultados con el equipo de operaciones"
- "Definir un piloto de 4 semanas con un segmento acotado de clientes"
- "Priorizar la consolidacion de las fuentes de datos para habilitar la solucion completa"

## Mapeo de dependencias entre documentos

La narrativa de negocio NO se inventa — se DERIVA de la ficha tecnica. Cada seccion de la narrativa tiene una o mas secciones de la ficha tecnica que la alimentan, y una transformacion que convierte lenguaje tecnico en lenguaje de negocio.

### Tabla de dependencias

| Narrativa de negocio | Se alimenta de (ficha tecnica) | Transformacion |
|---|---|---|
| El problema | Resumen + Tipo de problema | Reescribir eliminando toda jerga tecnica. El foco pasa del "que tipo de problema es" al "que dolor tiene el cliente" |
| El costo de no actuar | Dataset (volumen, contexto) + Metricas y resultados (baseline) | El baseline tecnico se convierte en el costo del status quo. Si el baseline es "decision manual acierta 60%", el costo es "4 de cada 10 decisiones son incorrectas" |
| La solucion | Approach tecnico (metodo elegido) | Eliminar el como y dejar solo el que hace. "Random forest con 200 estimadores" se convierte en "el sistema analiza patrones historicos y genera una recomendacion automatica" |
| Resultados concretos | Metricas y resultados (resultados obtenidos) | Traducir numeros tecnicos a impacto medible. La mejora sobre el baseline se expresa como reduccion de costos, tiempo ahorrado o errores evitados |
| Traduccion de metricas | Metricas y resultados (metricas de evaluacion + resultados obtenidos) | Conversion directa: cada metrica tecnica se reescribe como una frase que responde "y eso que significa para mi?" |
| Cimientos necesarios | Estado de datos y prerequisitos | Solo si hay observaciones. Traducir diagnostico tecnico a lenguaje de decision: que necesita, por que, y que pasa si no lo hace |
| Proximos pasos | Limitaciones y supuestos + Estado de datos y prerequisitos | Las limitaciones definen que se puede ofrecer como siguiente paso realista. Los prerequisitos pendientes pueden convertirse en una fase previa |

### Reglas del mapeo

1. **No inventar contenido en la narrativa que no exista en la ficha tecnica.** Si no tenes metricas, no podes escribir resultados concretos. Si no hiciste diagnostico de datos, no podes escribir cimientos necesarios.

2. **La transformacion siempre va en una direccion: tecnico a negocio.** Nunca al reves. La ficha tecnica es la fuente de verdad, la narrativa es la traduccion.

3. **Si una seccion de la ficha tecnica esta incompleta, la seccion correspondiente de la narrativa queda bloqueada.** Esto es intencional — fuerza a completar la ficha primero.

4. **El baseline es el ancla de toda la narrativa.** Sin baseline no hay "costo de no actuar", no hay "mejora", no hay "resultados concretos" con contexto. Es la seccion mas critica de la ficha tecnica para la narrativa.

### Flujo visual

```
FICHA TECNICA                          NARRATIVA DE NEGOCIO
─────────────                          ────────────────────

Resumen ──────────────────────────────> El problema
Tipo de problema ─────────────────┘

Dataset (volumen, contexto) ──────────> El costo de no actuar
Metricas y resultados (baseline) ─┘

Approach tecnico ─────────────────────> La solucion

Metricas y resultados ────────────────> Resultados concretos
         │
         └────────────────────────────> Traduccion de metricas

Estado de datos y prerequisitos ──────> Cimientos necesarios
                        │
                        └─────────────> Proximos pasos
Limitaciones y supuestos ─────────┘
```

## Alcance tecnico de las notebooks

Este framework esta disenado para demos defendibles, no para competencias de Kaggle. La complejidad de la parte de DS debe mantenerse dentro de limites que permitan explicar cada decision tomada. Si no podes explicar por que lo hiciste, no deberias haberlo hecho.

### Incluido

#### Exploracion (notebook 01)

- Carga de datos y verificacion de shape
- Revision de tipos de datos
- Distribucion de la variable target
- Reporte de valores faltantes
- Visualizaciones basicas: histogramas, countplots, barplots por categoria

#### Preparacion (notebook 02)

- Identificar y eliminar columnas con fuga de informacion
- Eliminar columnas no predictivas (IDs, metadata, coordenadas)
- Tratamiento simple de faltantes: rellenar con mediana (numericas) o con un valor descriptivo (categoricas), o eliminar filas si son pocas
- Encoding de categoricas con one-hot encoding
- Split train/test estratificado
- Guardar datasets procesados

#### Modelo y evaluacion (notebook 03)

- Establecer un baseline dummy (clasificador que predice la clase mayoritaria)
- Entrenar un modelo simple (ej: Regresion Logistica)
- Entrenar un modelo mas complejo (ej: Random Forest) para contrastar
- Tabla comparativa de metricas: accuracy, precision, recall, F1, AUC
- Feature importance del mejor modelo
- Matriz de confusion del mejor modelo

### Excluido (por ahora)

Estas tecnicas no estan prohibidas — estan fuera del alcance actual porque requieren un nivel de comprension mas profundo para ser defendidas. Cuando se dominen, se pueden incorporar al alcance.

- Feature engineering avanzado (creacion de features nuevas, interacciones, agregaciones)
- Tecnicas de balanceo de clases (SMOTE, oversampling, undersampling)
- Hyperparameter tuning (GridSearch, RandomizedSearch)
- Validacion cruzada (k-fold)
- Curva ROC y graficos tecnicos que no se traducen a negocio
- Stacking, ensembling avanzado
- Feature selection automatizada
- Pipelines de scikit-learn

### Criterio para expandir el alcance

Una tecnica pasa de "excluida" a "incluida" cuando se cumplen estas dos condiciones:

1. Podes explicar a alguien sin conocimiento tecnico QUE hace y POR QUE la usaste
2. Podes explicar a alguien tecnico POR QUE la elegiste sobre las alternativas

Si solo cumple la primera, todavia es una caja negra. Si solo cumple la segunda, no la podes traducir a narrativa de negocio. Necesitas ambas.

## Errores comunes a evitar

1. **Completar la narrativa de negocio antes de tener resultados** — sin datos, es ficcion
2. **Copiar la jerga tecnica a la narrativa de negocio** — si dice "accuracy", no es narrativa de negocio
3. **Dejar la ficha tecnica para el final** — se pierden las decisiones y el contexto
4. **No incluir baseline en las metricas** — un numero sin referencia no comunica nada
5. **Omitir limitaciones por miedo a parecer debil** — las limitaciones honestas generan confianza, no desconfianza
6. **Forzar "Cimientos necesarios" cuando no aplica** — si el cliente tiene todo en orden, no inventar prerequisitos
