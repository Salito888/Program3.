---
description: Api Árbol Binario de búsqueda (ABB) con FastAPI.
auto_execution_mode: 1
---


# REQUERIMIENTO: API ÁRBOL BINARIO DE BÚSQUEDA (ABB)

## Descripción General
Desarrollar una API REST con FastAPI para gestionar un Árbol Binario de Búsqueda (ABB) que demuestre casos de desbalance con valores altos, positivos y negativos.

## Fase MODEL
### Estructura de Nodo
- Atributos:
  - valor: entero (soporta valores negativos y positivos grandes)
  - izquierdo: referencia al nodo hijo izquierdo
  - derecho: referencia al nodo hijo derecho

### Comportamiento del ABB
- Propiedad fundamental: para cada nodo:
  - Todos los valores en subárbol izquierdo son menores
  - Todos los valores en subárbol derecho son mayores
- No realiza auto-balanceo automático
- Puede degenerar en lista enlazada con inserciones ordenadas

## Fase SERVICE
### Funcionalidades del Servicio ABB
1. *Inserción de valores*
   - Acepta enteros positivos y negativos
   - Rango recomendado: -1000 a 1000
   - No permite valores duplicados

2. *Verificación de balance*
   - Calcula diferencia de altura entre subárboles
   - Considera desbalanceado si diferencia > 1 en cualquier nodo

3. *Operaciones de consulta*
   - Recorrido in-order
   - Estructura completa del árbol
   - Estado de balance

4. *Ejemplo desbalanceado*
   - Secuencia específica que cause desbalance
   - Valores: [100, -50, 200, -25, 300, -75, 400, -10, 500, -100, 600]

### Respuestas del Servicio
- Formato JSON estructurado
- Incluir: mensaje, estado de balance, recorrido in-order, estructura del árbol

## Fase CONTROLLER
### Endpoints FastAPI
1. *POST /insertar*
   - Body: {"valor": integer}
   - Response: estado completo después de inserción

2. *GET /estado*
   - Response: estado actual del árbol
   - Incluye: balance, recorrido, estructura

3. *POST /ejemplo-desbalanceado*
   - Crea árbol desbalanceado predefinido
   - Response: estado del árbol creado

### Especificaciones Técnicas
- Framework: FastAPI
- Puerto: 8000
- Formato respuestas: JSON
- Documentación automática: /docs
- Tipado de datos estricto

## Criterios de Validación
- El árbol debe reportar "balanceado": false con la secuencia desbalanceada
- Debe manejar correctamente valores negativos
- La estructura del árbol debe reflejar la propiedad BST
- API debe ser completamente funcional y documentada