# Narrativa de Negocio

## El problema

Cada mes, un grupo de clientes deja de usar el servicio sin previo aviso. Para cuando el equipo lo detecta, el cliente ya se fue — y con el, los ingresos recurrentes que generaba. Hoy no existe una forma sistematica de identificar a tiempo que clientes estan en riesgo de irse, lo que obliga al equipo a reaccionar en lugar de prevenir.

## El costo de no actuar

Sin un sistema de alerta temprana, la empresa opera a ciegas sobre el 26% de su base de clientes que esta en riesgo de abandonar el servicio. Cada cliente perdido representa no solo el ingreso mensual que deja de entrar, sino el costo de adquirir un cliente nuevo para reemplazarlo — que en telecomunicaciones puede ser entre 5 y 7 veces mas caro que retener al existente.

Hoy, si no se hace nada, la unica estrategia es asumir que ningun cliente se va a ir. Esa estrategia no detecta ni un solo cliente en riesgo. El 100% de los abandonos pasa desapercibido hasta que ya es tarde.

## La solucion

El sistema analiza las senales de comportamiento de cada cliente — su nivel de satisfaccion, cuanto tiempo lleva con el servicio, cuanto paga, que tipo de contrato tiene, y que servicios usa — y genera una lista priorizada de quienes tienen mayor probabilidad de irse.

Esa lista llega ANTES de que el cliente tome la decision, lo que le da al equipo de retencion una ventana de accion para intervenir: ofrecer un upgrade, resolver un problema de servicio, o ajustar condiciones comerciales.

## Resultados concretos

Basados en el analisis de mas de 7,000 clientes reales:

- De cada 10 clientes que efectivamente se van, el sistema detecta 9 antes de que ocurra
- De cada 10 alertas que genera el sistema, entre 9 y 10 son clientes que realmente estan en riesgo
- El sistema mejora la capacidad de deteccion de un 0% (no hacer nada) a un 91%
- Los principales factores de riesgo identificados son: nivel de satisfaccion del cliente, antiguedad en el servicio, monto del cargo mensual, y tipo de contrato

## Traduccion de metricas

| Metrica tecnica | Significado para el negocio |
|---|---|
| Recall 91.07% | De cada 10 clientes que se van, el sistema detecta 9 antes de que ocurra |
| Precision 96.23% | De cada 10 alertas de riesgo, entre 9 y 10 son clientes que realmente se van a ir |
| Baseline (0% recall) | Sin el sistema, no se detecta a ninguno de los clientes que se van |

## Cimientos necesarios

Para que esta solucion funcione de manera sostenida, la empresa necesita:

- **Datos de satisfaccion del cliente**: algun mecanismo sistematico para medir satisfaccion (NPS, CSAT, encuestas post-atencion). Este es el factor predictivo mas fuerte — sin el, la capacidad de deteccion se reduce significativamente. Si hoy no se mide, implementar al menos un NPS trimestral es el primer paso.

- **Acceso a datos de facturacion y servicios**: informacion actualizada sobre antiguedad, cargos mensuales, tipo de contrato, y servicios contratados por cada cliente. En general, esta informacion ya existe en los sistemas de facturacion y CRM — solo necesita ser accesible de forma estructurada.

## Proximos pasos

Agendar una reunion de 30 minutos con el equipo de Customer Success o Revenue Operations para revisar estos resultados, validar que los factores de riesgo identificados coinciden con la experiencia del equipo, y definir un piloto de 4 semanas con un segmento acotado de clientes.
