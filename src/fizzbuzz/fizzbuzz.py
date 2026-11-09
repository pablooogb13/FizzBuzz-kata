def fizzbuzz(n):
    reglas = [
        (n % 3 == 0, "Fizz"),
        ("3" in str(n), "Fizz"),
        (n % 5 == 0, "Buzz"),
        ("5" in str(n), "Buzz"),
    ]
    salida = "".join(texto for cond, texto in reglas if cond)
    return salida or str(n)

if __name__ == "__main__":
    for number in range(1, 101):
        print(fizzbuzz(number))
