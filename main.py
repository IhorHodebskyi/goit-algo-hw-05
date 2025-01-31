
import re


def caching_fibonacci( ):
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci



def generator_numbers(values):

    suma = 0
    for value in values:
        yield value
        suma += float(value)

    return suma


def sum_profit(text):
    
    list_number = re.findall(r"\d+\.\d+", text)
    sum = 0
    for value in list_number:
        sum += float(value)
    return sum



if __name__ == '__main__':
    n = 15
    fib = caching_fibonacci()
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610




    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text)
    print(f"Загальний дохід: {total_income}")
