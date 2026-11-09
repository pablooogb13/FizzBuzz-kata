import pytest

from fizzbuzz import fizzbuzz


# ---------------------------------------------------------------------------
# Hitos del proceso TDD (narrativa)
# ---------------------------------------------------------------------------

def test_1_devuelve_1():
    """Caso base: un número sin reglas se devuelve tal cual."""
    assert fizzbuzz(1) == "1"


def test_3_devuelve_FizzFizz():
    """3 es divisible por 3 y contiene un 3: dos condiciones de Fizz."""
    assert fizzbuzz(3) == "FizzFizz"


def test_5_devuelve_BuzzBuzz():
    """5 es divisible por 5 y contiene un 5: dos condiciones de Buzz."""
    assert fizzbuzz(5) == "BuzzBuzz"


def test_15_devuelve_FizzBuzzBuzz():
    """15 es divisible por 3, divisible por 5 y contiene un 5."""
    assert fizzbuzz(15) == "FizzBuzzBuzz"


def test_35_devuelve_FizzBuzzBuzz():
    """35 contiene 3, es divisible por 5 y contiene 5.

    Este caso rompe la implementación con `or`: obliga a separar cada
    condición en su propio `if` para acumular dos Buzz.
    """
    assert fizzbuzz(35) == "FizzBuzzBuzz"


def test_53_devuelve_FizzBuzz():
    """53 contiene 3 y contiene 5, pero no es divisible por ninguno."""
    assert fizzbuzz(53) == "FizzBuzz"


# ---------------------------------------------------------------------------
# Tabla de casos (cobertura)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("n, esperado", [
    (2, "2"),
    (4, "4"),
    (7, "7"),
    (8, "8"),
    (11, "11"),
    (13, "Fizz"),          # contiene 3
    (14, "14"),
    (16, "16"),
    (19, "19"),
    (22, "22"),
    (26, "26"),
    (29, "29"),
    (31, "Fizz"),          # contiene 3
    (34, "Fizz"),          # contiene 3
    (37, "Fizz"),          # contiene 3
    (41, "41"),
    (43, "Fizz"),          # contiene 3
    (46, "46"),
    (47, "47"),
    (49, "49"),
    (52, "Buzz"),          # contiene 5
    (58, "Buzz"),          # contiene 5
    (59, "Buzz"),          # contiene 5
    (61, "61"),
    (62, "62"),
    (64, "64"),
    (67, "67"),
    (68, "68"),
    (71, "71"),
    (73, "Fizz"),          # contiene 3
    (74, "74"),
    (76, "76"),
    (77, "77"),
    (79, "79"),
    (82, "82"),
    (83, "Fizz"),          # contiene 3
    (85, "BuzzBuzz"),      # divisible por 5 y contiene 5
    (86, "86"),
    (88, "88"),
    (89, "89"),
    (91, "91"),
    (92, "92"),
    (94, "94"),
    (97, "97"),
    (98, "98"),
])
def test_fizzbuzz_casos(n, esperado):
    assert fizzbuzz(n) == esperado


# ---------------------------------------------------------------------------
# Secuencia completa (1..100)
# ---------------------------------------------------------------------------

def test_secuencia_tiene_100_elementos():
    from fizzbuzz import fizzbuzz_sequence
    assert len(fizzbuzz_sequence()) == 100


def test_secuencia_extremos():
    from fizzbuzz import fizzbuzz_sequence
    seq = fizzbuzz_sequence()
    assert seq[0] == "1"                  # 1
    assert seq[2] == "FizzFizz"           # 3
    assert seq[4] == "BuzzBuzz"           # 5
    assert seq[14] == "FizzBuzzBuzz"      # 15
    assert seq[34] == "FizzBuzzBuzz"      # 35
    assert seq[52] == "FizzBuzz"          # 53
    assert seq[99] == "Buzz"          # 100 (divisible por 5)
