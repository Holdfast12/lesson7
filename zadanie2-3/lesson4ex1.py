#!/usr/bin/python3
# Реализовать сортировку списка методом пузырька.
# Должен сортироваться список чисел

# получаем список чисел от пользователя и создаем list
l = list(map(lambda n: float(n) if '.' in n else int(n),
        (input('\nВведите числа списка для сортировки через пробел: ').split())))

def sort_list(t):
    """Функция, которая принимает на вход список чисел
    и возвращает его отсортированным
    """
    t_list = t.copy()
    for i in range(len(t_list)):
        for j in range(len(t_list)-i-1):
            if t_list[j] > t_list[j+1]:
                t_list[j], t_list[j+1] = t_list[j+1], t_list[j]
    return(t_list)

print(f'Отсортированный список: {sort_list(l)}')
