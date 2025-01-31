
import re
from typing import Callable, Generator


def caching_fibonacci( )->Callable[[int], int]:
    cache: dict[int, int] = {}

    def fibonacci(value: int)-> int:
        if value <= 0:
            return 0
        if value == 1:
            return 1
        if value in cache:
            return cache[value]
        cache[value] = fibonacci(value - 1) + fibonacci(value - 2)
        return cache[value]

    return fibonacci



def generator_numbers(value: str)->Generator[float, None, None]:
    list_number = re.findall(r"\d+\.\d+", value)
    for number in list_number:
        yield float(number)



def sum_profit(value: str, func: Callable[[str],Generator[float,None, None]]):
    return sum(func(value))
    




if __name__ == '__main__':
    n = 15
    fib = caching_fibonacci()
    print(fib(10))  # Виведе 55
    print(fib(15))  # Виведе 610




    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
