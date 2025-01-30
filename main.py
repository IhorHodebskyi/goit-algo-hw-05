
import re


def caching_fibonacci(n, cache = {}):


    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci(n)



def generator_numbers(values):

    suma = 0
    for value in values:
        yield value
        suma += float(value)

    return suma


def sum_profit(text, generator_function):
    
    generator = generator_function(re.findall(r"\d+\.\d+", text))
    sum = 0
    for value in generator:
        sum += float(value)
    return sum



if __name__ == '__main__':
    n = 15
    print(caching_fibonacci(n))




    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
