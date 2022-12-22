#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Создать игровой инвентарь. Должна быть возможность
        добавлять в него предметы и удалять предметы из него.
Инвентарь должен быть ограничен по весу, каждый предмет имеет свой вес.
Вывод предметов должен быть с названием предмета и его весом.
"""

# инвентарь. первое число в списке по ключу означает вес одного предмета
# второе число - количество предметов этого вида в инвентаре
inventory = {
        'топор': [1100, 1],
        'пила': [400, 1],
        'нож': [150, 2],
        'молоток': [400, 1],
        'палка': [1300, 1],
        'яблоко': [176, 1],
        }

max_inventory = 5000


def summ_inventory():
    """Функция для подсчета текущего веса инвентаря"""
    t = 0
    for i, j in inventory.items():
        t += j[0] * j[1]
    return t


while True:
    print('\nСостав инвентаря на текущий момент:')
    for i, j in inventory.items():
        print(f'{i} в количестве {j[1]} шт. общим весом {j[0]*j[1]} грамм')
    action1 = input(f'__________________________________________\n'
            + f'Сейчас вес всего инвентаря составляет {summ_inventory()/1000} килограмм\n'
            + f'Максимально возможный вес - 5 килограмм\n\nДоступные действия:\n'
            + f'\t 1 Добавить предмет\n'
            + f'\t 2 Удалить предмет\n'
            + f'\t 3 Удалить из инвентаря все предметы\n'
            + f'\t 4 Выйти из скрипта\nВведите номер действия для инвентаря: ')
    if action1 == '1':
        action2 = input('Введите имя предмета, который вы хотите добавить инвентарь: ')
        if inventory.get(action2) == None:
            action3 = int(input('Введите вес добавляемого предмета в граммах: '))
            if summ_inventory() + action3 <= max_inventory:
                inventory[action2] = [action3, 1]
                print(f'Добавлено {action2} 1 шт.')
            else:
                print(f'Достигнут предел веса инвентаря,'
                        + f'разместить {action2} весом {action3} грамм не удастся')
        else:
            if summ_inventory() + inventory[action2][0] <= max_inventory:
                inventory[action2][1] += 1
                print(f'Добавлено {action2} 1 шт.')
            else:
                print(f'Достигнут предел веса инвентаря,'
                        + f'разместить {action2} весом {inventory[action2][0]} грамм не удастся')
    elif action1 == '2':
        action2 = input('Введите имя предмета,'
                + f'который вы хотите удалить из инвентаря: ')
        if inventory.get(action2) == None:
            print('Такого предмета в инвентаре нет')
        else:
            if inventory[action2][1] > 1:
                inventory[action2][1] -= 1
            else:
                inventory.pop(action2)
            print(f'Удалено {action2} 1 шт.')
    elif action1 == '3':
        inventory.clear()
        print('Все предметы из инвентаря удалены')
    elif action1 == '4':
        break
    else:
        print('!!!такой опции нет!!!')
