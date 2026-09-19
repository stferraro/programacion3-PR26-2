# Práctica: Sistema de Figuras Geométricas

## Unidad II — Programación Orientada a Objetos

### Objetivo de aprendizaje

Diseñar e implementar un pequeño sistema de figuras geométricas aplicando los
cuatro pilares de la Programación Orientada a Objetos: **abstracción**,
**encapsulamiento**, **herencia** y **polimorfismo**, siguiendo el diagrama de
clases UML provisto en `resources/diagram.drawio`.

### Contexto

Una empresa dedicada a la fabricación de piezas necesita un módulo que permita
calcular el área y el perímetro de distintas figuras geométricas planas, sin
que el código cliente tenga que conocer los detalles internos de cada figura
ni duplicar lógica de cálculo. Se le pide implementar el modelo de clases que
se muestra en el diagrama UML adjunto.

### Diagrama de clases

El diagrama define una clase base `FiguraGeometrica` de la cual heredan tres
figuras concretas: `Rectangulo`, `Cuadrado` y `Triangulo`.

```
                    FiguraGeometrica
                     (clase base)
                    /      |      \
                   /       |       \
          Rectangulo   Triangulo   Cuadrado
```

### Especificación de las clases

#### `FiguraGeometrica` (clase base / abstracta)

Representa el comportamiento común a toda figura geométrica. No debe poder
instanciarse directamente: define el "contrato" que toda figura concreta debe
cumplir.

- Métodos abstractos que cada subclase está obligada a redefinir:
  - `get_area()`
  - `get_perimetro()`
  - `__str__()`

#### `Rectangulo` (hereda de `FiguraGeometrica`)

| Atributo | Visibilidad | Tipo  |
|----------|-------------|-------|
| base     | pública     | float |
| altura   | pública     | float |

- `get_area()`: retorna `base * altura`
- `get_perimetro()`: retorna `2 * (base + altura)`
- `__str__()`: retorna una descripción legible del rectángulo (dimensiones,
  área y perímetro)

#### `Cuadrado` (hereda de `FiguraGeometrica`)

| Atributo | Visibilidad | Tipo  |
|----------|-------------|-------|
| lado     | pública     | float |

- `get_area()`: retorna `lado ** 2`
- `get_perimetro()`: retorna `4 * lado`
- `__str__()`: retorna una descripción legible del cuadrado

> Pista de diseño: ¿podría `Cuadrado` reutilizar la lógica de `Rectangulo` en
> lugar de heredar directamente de `FiguraGeometrica`? Justifique su decisión.

#### `Triangulo` (hereda de `FiguraGeometrica`)

| Atributo | Visibilidad | Tipo  |
|----------|-------------|-------|
| lado1    | pública     | float |
| lado2    | pública     | float |
| lado3    | pública     | float |

Un triángulo queda completamente definido por sus tres lados; no se piden
`base` ni `altura` como datos separados porque `base` sería en realidad uno
de los lados, y pedirlos por separado permitía crear triángulos inconsistentes
(por ejemplo, una `base` que no coincidiera con ningún lado real).

- `get_area()`: se calcula con la **fórmula de Herón**, a partir del
  semiperímetro `s = perímetro / 2`:
  `área = √(s · (s − lado1) · (s − lado2) · (s − lado3))`
- `get_perimetro()`: retorna `lado1 + lado2 + lado3`
- `__str__()`: retorna una descripción legible del triángulo
- El constructor debe validar la **desigualdad triangular** (la suma de dos
  lados cualesquiera debe ser mayor al tercero) y lanzar una excepción si los
  lados no forman un triángulo válido.

### Requisitos técnicos

1. **Abstracción**: `FiguraGeometrica` debe modelarse como clase abstracta
   (por ejemplo, usando `ABC` y `@abstractmethod` en Python), impidiendo que
   se cree una instancia directa de ella.
2. **Encapsulamiento**: los atributos deben validarse al asignarse (no se
   permiten valores negativos o iguales a cero para lados, bases o alturas).
   Utilice propiedades (`@property`) o métodos de acceso para proteger el
   estado interno de cada objeto.
3. **Herencia**: `Rectangulo`, `Cuadrado` y `Triangulo` deben extender
   `FiguraGeometrica` y reutilizar su interfaz común.
4. **Polimorfismo**: implemente una función o script que reciba una lista de
   objetos `FiguraGeometrica` (de distintos tipos) y calcule/imprima el área
   y el perímetro de cada una invocando siempre los mismos métodos
   (`get_area()`, `get_perimetro()`), sin distinguir el tipo concreto de la
   figura mediante `if`/`isinstance`.
