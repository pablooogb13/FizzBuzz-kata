# FizzBuzz Kata 

Implementación del kata [FizzBuzz](https://codingdojo.org/kata/FizzBuzz/) con TDD.

## Reglas implementadas

- **Fizz** si el número es divisible por 3 **o** contiene un 3.
- **Buzz** si el número es divisible por 5 **o** contiene un 5.
- **Cada condición cumplida añade su palabra**. Por eso:
  - `3` → `FizzFizz` (divisible por 3 y contiene 3)
  - `5` → `BuzzBuzz` (divisible por 5 y contiene 5)
  - `15` → `FizzBuzzBuzz` (divisible por 3, divisible por 5 y contiene 5)
  - `35` → `FizzBuzzBuzz` (contiene 3, divisible por 5 y contiene 5)
  - `53` → `FizzBuzz` (contiene 3 y contiene 5)
- Si no se cumple ninguna condición, se muestra el número.

## Cómo ejecutarlo

Requisitos: Python ≥ 3.10.

El script principal se ejecuta desde su propia carpeta:

```bash
cd src/fizzbuzz
python3 fizzbuzz.py
```

Esto imprime la secuencia del 1 al 100 aplicando las reglas del Stage 2.

Si prefieres ejecutarlo desde la raíz del proyecto:

```bash
python3 src/fizzbuzz/fizzbuzz.py
```

## Cómo ejecutar los tests

Desde la raíz del proyecto:

```bash
pytest -v
```

Resultado esperado: **63 tests en verde**.

Si `pytest` no está instalado:

```bash
pip install pytest
```

## Estructura del proyecto

```
.
├── src/
│   └── fizzbuzz/
│       ├── __init__.py     # reexporta la API pública
│       └── fizzbuzz.py     # lógica + bloque __main__
├── tests/
│   └── test_fizzbuzz.py    # tests con pytest
├── pyproject.toml
├── .gitignore
└── README.md
```

## Decisiones de diseño

- **Lógica separada de la ejecución**: `fizzbuzz.py` contiene la función pura
  `fizzbuzz(n)` y, al final, un bloque `if __name__ == "__main__":` que imprime
  la secuencia. Así el archivo se puede ejecutar directamente
  (`python3 fizzbuzz.py`) y, a la vez, importar desde los tests
  (`from fizzbuzz import fizzbuzz`).
- **Reglas como datos**: las reglas son una lista de tuplas
  `(condición, texto)`. Añadir una regla nueva es una línea; el bucle principal
  no cambia. Es más declarativo que una cadena de `if/elif`.
- **`salida or str(n)`**: idiomático en Python para "si no hay nada, muestra el
  número". Evita un `if` extra y expresa la intención.
- **Interpretación del Stage 2**: cada condición cumplida añade su palabra.
  Evidencia: el enunciado dice `35 → FizzBuzzBuzz` (contiene 3, divisible por 5,
  contiene 5). Por coherencia, `3 → FizzFizz`, `5 → BuzzBuzz`,
  `15 → FizzBuzzBuzz`. Se documenta aquí porque el enunciado es ambiguo y se ha
  consultado al equipo.
- **Sin validación de rango en `fizzbuzz(n)`**: la función es pura y acepta
  cualquier entero ≥ 1. El rango 1–100 lo garantiza `fizzbuzz_sequence()`, y el
  bloque `__main__` lo imprime.
- **`fizzbuzz_sequence()` sin parámetros**: devuelve siempre la secuencia del 1
  al 100. Es lo que pide el kata y evita decisiones innecesarias sobre el orden
  de los parámetros. Si en el futuro se necesita otro rango, se pueden añadir
  parámetros opcionales sin romper las llamadas actuales.
- **Sin imports relativos en `fizzbuzz.py`**: para que `python3 fizzbuzz.py`
  funcione desde su carpeta, el archivo no usa `from .algo import ...`. El
  `__init__.py` reexporta la función para los tests, pero no interfiere con la
  ejecución directa.

## Proceso (TDD)

El código se desarrolló con ciclos Red-Green-Refactor:

1. Test: `1` → `"1"`; implementación mínima.
2. Test: `3` → `"Fizz"`; implementación mínima.
3. Test: `5` → `"Buzz"`; implementación mínima.
4. Test: `15` → `"FizzBuzz"`; refactor a acumulador con `%`.
5. Test: `13` → `"Fizz"`; añadir condición "contiene 3".
6. Test: `52` → `"Buzz"`; añadir condición "contiene 5".
7. Test: `35` → `"FizzBuzzBuzz"`; **rompe** la versión con `or` y obliga a
   separar cada condición en su propio `if`.
8. Test: `53` → `"FizzBuzz"`; confirma la interpretación.
9. Refactor: reglas como lista de tuplas.
10. Tests de secuencia completa y bloque `__main__` para ejecución directa.

La historia de commits refleja este proceso. Los tests están organizados en dos
bloques:

- **Hitos del proceso TDD** (`test_1_devuelve_1`, `test_3_devuelve_FizzFizz`,
  `test_5_devuelve_BuzzBuzz`, `test_15_devuelve_FizzBuzzBuzz`,
  `test_35_devuelve_FizzBuzzBuzz`, `test_53_devuelve_FizzBuzz`): narran los
  pasos clave.
- **Tabla parametrizada** (`test_fizzbuzz_casos`): cubre el resto de casos
  representativos sin repetir boilerplate.
- **Secuencia completa** (`test_secuencia_*`): valida `fizzbuzz_sequence()`.

## Salida esperada (extracto)

```
1
2
FizzFizz
4
BuzzBuzz
Fizz
7
8
Fizz
Buzz
11
Fizz
Fizz
14
FizzBuzzBuzz
16
17
Fizz
19
Buzz
...
```
