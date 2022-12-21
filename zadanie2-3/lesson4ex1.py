#!/usr/bin/python3
#Реализовать сортировку списка методом пузырька.
#Должен сортироваться список чисел

#получаем список чисел от пользователя
l = list(map(lambda n: float(n) if '.' in n else int(n),
        (input('\nВведите числа списка для сортировки через пробел: ').split())))

for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print(f'Отсортированный список: {l}')
