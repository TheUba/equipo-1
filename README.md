# DS Business Demo Template

Template base **notebook-first** para demos de Data Science orientados a negocio.

## Objetivo

Este repositorio sirve como base para:

- trabajar problemas de DS con notebooks en formato `py:percent`
- documentar el caso desde una perspectiva tecnica y de negocio
- usar un ejemplo de referencia concreto (**churn**) sin mezclar todavia backend y frontend live-only
- evolucionar luego hacia un demo desplegable con DS integrada

## Alcance actual

Esta primera version del template cubre:

- entorno reproducible con `pyenv` + `.python-version` + `uv`
- notebooks locales con `jupyter` + `jupytext`
- ejemplo de churn como caso de referencia
- documentacion base del caso:
  - `technical-brief.md`
  - `business-narrative.md`
- documentacion metodologica en `docs/`

Todavia NO incluye:

- backend live-only
- frontend
- contrato HTTP implementado
- Docker

## Estructura

```txt
notebooks/   notebooks en formato .py:percent sincronizados con Jupytext
data/raw/    datos crudos locales (no versionados)
data/processed/ datos procesados locales (no versionados)
src/         espacio para codigo reutilizable
docs/        guias y documentacion metodologica de DS
```

## Requisitos

- `pyenv`
- Python `3.12.13`
- `uv`

## Setup

### 1. Instalar la version de Python si no la tenes

```bash
pyenv install 3.12.13
```

### 2. Instalar dependencias del proyecto

```bash
uv sync
```

## Como levantar el proyecto

### Abrir notebooks con Jupyter Notebook

```bash
uv run jupyter notebook notebooks/
```

### Abrir notebooks con JupyterLab

```bash
uv run jupyter lab
```

## Flujo de trabajo recomendado

1. Trabajar los notebooks en `notebooks/`
2. Mantenerlos versionados como `.py:percent` con Jupytext
3. Documentar decisiones y resultados en:
   - `technical-brief.md`
   - `business-narrative.md`
4. Usar las guias de `docs/` para no empezar desde cero

## Documentacion disponible

- `docs/ds-documentation-guide.md` — como completar la ficha tecnica y la narrativa de negocio
- `docs/stage-2-notebooks-guide.md` — criterio base para disenar la etapa de notebooks
- `docs/stage-2-operational-glossary.md` — glosario operativo de metricas, modelos, limpieza y visuales

## Caso de referencia incluido

El template incluye un ejemplo de **prediccion de churn** como referencia inicial de trabajo. Ese ejemplo sirve para mostrar:

- baseline
- comparacion de modelos
- metricas de clasificacion
- traduccion de resultados a negocio

## Nota sobre Jupytext

Este template esta pensado para trabajo local con Jupyter/JupyterLab y Jupytext. El objetivo es tener notebooks ligeros, versionables y compatibles con un flujo serio de proyecto.
