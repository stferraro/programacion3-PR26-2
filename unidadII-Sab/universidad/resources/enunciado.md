# Práctica: Sistema de Gestión Académica (Estudiante / Materias)

## Unidad II — Programación Orientada a Objetos

### Objetivo de aprendizaje

Diseñar e implementar un pequeño sistema que modele la relación entre un
estudiante y las materias que cursa, aplicando **encapsulamiento** (atributos
privados con acceso controlado mediante propiedades) y **composición** (un
`Estudiante` está compuesto por una colección de objetos `Materias`), para
luego determinar si el estudiante aprobó el semestre según su promedio
ponderado.

### Contexto

Una universidad necesita un módulo que permita registrar los datos de un
estudiante, las materias que cursó junto con el número de créditos y la nota
obtenida en cada una, y calcular automáticamente si el estudiante aprobó el
semestre según el promedio ponderado por créditos.

### Especificación de las clases

#### `Materias`

Representa una materia cursada por un estudiante.

| Atributo  | Visibilidad | Tipo  |
|-----------|-------------|-------|
| nombre    | privada     | str   |
| creditos  | privada     | int   |
| nota      | privada     | float |

- Todos los atributos son privados (`__nombre`, `__creditos`, `__nota`) y se
  acceden únicamente a través de propiedades (`@property` / `@<attr>.setter`).
- `get_valor()`: retorna `creditos * nota` (el "peso" de la materia dentro del
  promedio ponderado).
- `__str__()`: retorna una descripción legible de la materia.

#### `Estudiante`

Representa a un estudiante y la lista de materias que cursó.

| Atributo  | Visibilidad | Tipo  |
|-----------|-------------|-------|
| nombre    | privada     | str   |
| apellido  | privada     | str   |
| cedula    | privada     | str   |
| carrera   | privada     | str   |
| correo    | privada     | str   |
| telefono  | privada     | str   |
| materias  | privada     | list[Materias] |

- Todos los atributos son privados y se acceden mediante propiedades.
- `agregar_materia(materia)`: agrega un objeto `Materias` a la lista de
  materias cursadas por el estudiante.
- `get_promedio_ponderado()`: calcula el promedio ponderado por créditos:

  ```
  promedio = Σ(creditos_i × nota_i) / Σ(creditos_i)
  ```

  > Importante: el promedio **no** es un simple promedio aritmético de las
  > notas. Una materia con más créditos debe pesar más en el resultado final
  > que una materia con menos créditos.

- `aprobo_semestre(nota_minima)`: retorna `True` si `get_promedio_ponderado()`
  es mayor o igual a `nota_minima`, `False` en caso contrario.
- `__str__()`: retorna los datos del estudiante junto con el detalle de cada
  materia cursada.

### Escala de calificación

- La nota de cada materia va de **0 a 20**.
- La nota mínima para **aprobar el semestre** es **10**.

### Requisitos técnicos

1. **Encapsulamiento**: ningún atributo debe ser accedido ni modificado
   directamente desde fuera de la clase; todo acceso pasa por una propiedad.
2. **Composición**: `Estudiante` no hereda de `Materias`; en cambio, mantiene
   una lista de objetos `Materias` como parte de su estado (relación "tiene
   un/a", no "es un/a").
3. **Promedio ponderado correcto**: la nota final de un estudiante debe
   reflejar el peso real de los créditos de cada materia, no solo la cantidad
   de materias cursadas.
4. **Determinación de aprobación**: el sistema debe poder responder, para
   cualquier estudiante, si aprobó o no el semestre, comparando su promedio
   ponderado contra la nota mínima de aprobación (10).

### Entregables

- Código fuente organizado en el proyecto `universidad`:
  - `src/models/materias.py`
  - `src/models/estudiante.py`
  - `src/views/view.py` (capa de presentación, separada de los modelos)
- Un script principal (`main.py`) que:
  - cree un estudiante,
  - lo inscriba en varias materias con distintos créditos y notas,
  - muestre el resumen del estudiante, su promedio ponderado, y si aprobó o
    no el semestre.

### Criterios de evaluación

| Criterio                                                    | Puntos |
|----------------------------------------------------------------|:------:|
| Encapsulamiento correcto en `Materias` y `Estudiante`           |   25   |
| Composición `Estudiante` – `Materias` bien implementada         |   20   |
| Cálculo correcto del promedio ponderado por créditos            |   25   |
| Método `aprobo_semestre()` correctamente implementado           |   15   |
| Separación entre modelos (`models/`) y presentación (`views/`)  |   10   |
| `__str__` bien implementado en ambas clases                     |    5   |

### Preguntas de reflexión (para entregar junto al código)

1. ¿Por qué el promedio ponderado se calcula dividiendo entre la suma de
   créditos y no entre la cantidad de materias?
2. ¿Qué diferencia hay entre la relación de `Estudiante` con `Materias` en
   este ejercicio y la relación de herencia que usaste en el ejercicio de
   figuras geométricas?
3. ¿Qué pasaría con el promedio ponderado si `Estudiante` no tuviera ninguna
   materia cargada al llamar a `get_promedio_ponderado()`? ¿Cómo lo
   solucionarías?
