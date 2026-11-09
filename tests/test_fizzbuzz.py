from fizzbuzz import fizzbuzz

def test_1_devuelve_1():          assert fizzbuzz(1) == "1"
def test_3_devuelve_Fizz():       assert fizzbuzz(3) == "FizzFizz"   # ojo: 3 se repite
def test_5_devuelve_Buzz():       assert fizzbuzz(5) == "BuzzBuzz"
def test_15_devuelve_FizzBuzzBuzz(): assert fizzbuzz(15) == "FizzBuzzBuzz"
def test_13_contiene_3():         assert fizzbuzz(13) == "Fizz"
def test_52_contiene_5():         assert fizzbuzz(52) == "Buzz"
def test_35_FizzBuzzBuzz():       assert fizzbuzz(35) == "FizzBuzzBuzz"
def test_53_FizzBuzz():           assert fizzbuzz(53) == "FizzBuzz"
