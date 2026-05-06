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

- entorno reproducible con `.python-version` + `uv`
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

- `uv`

## Windows + WSL 2 (Ubuntu)

Si quieres trabajar en este proyecto desde una maquina con Windows, la forma recomendada es usar **WSL 2 con Ubuntu**.

### 1. Instalar WSL 2 y Ubuntu

Ejecuta en **PowerShell como administrador**:

```bash
wsl --install --web-download -d Ubuntu
```

Luego reinicia la PC si el sistema lo solicita.

### 2. Configurar Ubuntu

- Abre **Ubuntu** desde el menú de inicio.
- Crea tu usuario y contraseña para WSL.

### 3. Verificar que Ubuntu esté corriendo en WSL 2

Ejecuta en **PowerShell como administrador**:

```bash
wsl -l -v
```

Verifica que **Ubuntu** tenga `2` en la columna `VERSION`.

## Instalar `uv`

Instala `uv` siguiendo la documentacion oficial para **Linux**:

- https://github.com/astral-sh/uv#installation

Para este caso, usa la opcion de **standalone installers** para **Linux**.

Este paso aplica tanto si trabajas en **Linux host** como si trabajas dentro de **Ubuntu en WSL**.

Si acabas de instalarlo, reinicia la terminal o recarga tu shell antes de seguir.

## Entrar al proyecto desde Linux

Con `uv` ya instalado, entra a la carpeta del repositorio desde tu terminal de Linux.

Este paso aplica tanto para **Linux host** como para **Ubuntu en WSL**.

## Setup

La version de Python requerida esta pineada en `.python-version`; `uv` la resolvera automaticamente si hace falta.

### 1. Sincronizar entorno y dependencias

```bash
uv sync
```

## Como levantar el proyecto

### Abrir notebooks con Jupyter Notebook

```bash
uv run jupyter notebook notebooks/ --ServerApp.port=12001
```

## Flujo de trabajo recomendado

1. Trabajar los notebooks en `notebooks/`
2. Mantenerlos versionados como `.py:percent` con Jupytext
3. Documentar decisiones y resultados en:
   - `technical-brief.md`
   - `business-narrative.md`
4. Usar las guias de `docs/` para no empezar desde cero

## Como agregar paquetes nuevos

Si necesitas una dependencia que no esta en `uv.lock`, agregala con `uv add`.

### Dependencia de runtime

```bash
uv add nombre-del-paquete
```

### Dependencia de desarrollo

```bash
uv add --dev nombre-del-paquete
```

Esto actualiza:

- `pyproject.toml`
- `uv.lock`
- el entorno local `.venv`

Ejemplo:

```bash
uv add plotly
```

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

Este template esta pensado para trabajo local con Jupyter Notebook y Jupytext. El objetivo es tener notebooks ligeros, versionables y compatibles con un flujo serio de proyecto.
