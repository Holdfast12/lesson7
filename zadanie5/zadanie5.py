#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Установить через pip библиотеку numpy. С помощью этой библиотеки cоздать массив 3x3 со случайными значениями, вывести его. Транспонировать его и вывести.

import numpy
from random import randint


a = numpy.array([[randint(1, 100) for i in range(3)] for j in range(3)])

print(f'Вот созданный массив 3х3 со случайными значениями:\n{a}')

a = a.transpose()
print(f'Вот этот массив 3х3 после транспонирования:\n{a}')