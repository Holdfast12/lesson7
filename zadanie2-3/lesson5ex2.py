#!/usr/bin/python3
#Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму.

def summa(*args):
    '''Функция, принимающая сколько угодно числовых и текстовых параметров
    (в том числе и 0) и возвращающая их суммы.
    '''
    t_chisel = 0
    t_strok = ''
    for i in args:
        if type(i) == int or type(i) == float:
            t_chisel += i
        elif type(i) == str:
            t_strok += i
    return t_chisel, t_strok


parametri = input('Введите параметры через пробел, чтобы получить их сумму: ').split()
for i in range(len(parametri)):
    try:
        parametri[i] = float(parametri[i]) if '.' in parametri[i] else int(parametri[i])
    except ValueError:
        print(f'Параметр {parametri[i]} будет принят как текстовый')

summa_chisel, summa_strok = summa(*parametri)

print(f'=======================================\n'
        + f'Для введенных параметров\n'
        + f'\tсумма чисел будет равна: {summa_chisel}\n'
        + f'\tсумма строк будет такой: {summa_strok}')
