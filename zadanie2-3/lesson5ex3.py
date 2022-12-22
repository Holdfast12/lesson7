#!/usr/bin/python3
# Написать функцию, которая возвращает заданное число Фибоначчи (рекурсия).

def fibonacci(n):
    """Функция, возвращающая заданное число Фибоначчи через рекурсию.
    """
    if n in (1, 2):
        return 1
    elif n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)


fib_number = input('Введите нужный номер числа Фибоначчи: ')
try:
    fib_number = int(fib_number)
except ValueError:
    print('Неправильный ввод. Номер числа Фибоначчи может быть только одиночным целым положительным числом')
else:
    if fib_number >= 0:
        print(fibonacci(fib_number))
    else:
        print('Номер числа Фибоначчи не может быть отрицательным числом')
        