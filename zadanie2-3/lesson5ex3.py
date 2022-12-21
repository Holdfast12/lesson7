#!/usr/bin/python3

#Написать функцию, которая возвращает заданное число Фибоначчи (рекурсия).

def fibonacci(n):
    '''
    Функция, возвращающая заданное число Фибоначчи через рекурсию.
    '''
    if n in (1, 2):
        return 1
    elif n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)


nomer = input('Введите нужный номер числа Фибоначчи: ')
try:
    nomer = int(nomer)
except ValueError:
    print('Неправильный ввод. Номер числа Фибоначчи может быть только одиночным целым положительным числом')
else:
    if nomer >= 0:
        print(fibonacci(nomer))
    else:
        print('Номер числа Фибоначчи не может быть отрицательным числом')
        