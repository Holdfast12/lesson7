#!/usr/bin/python3
"""Написать функцию, принимающую строку-пароль.
Функция должна проверить подходит ли этот пароль условиям и вернуть
        True - если подходит;
        False - если не подходит. Условия:
    ◦ Должен быть не менее 6 символов;
    ◦ Должен содержать хотя бы одну цифру;
    ◦ Не должен состоять только из цифр;
    ◦ Не должен содержать слово “password” в любом регистре.
"""

import re


def check_passwd(stroka):
    """Функция, принимающая строку-пароль и проверяющая выполнение условий.
    """
    if (len(stroka) >= 6 and
            re.search('\d', stroka) != None and
            re.search('\D', stroka) != None and
            re.search('password', stroka.lower()) == None):
        return True
    else:
        return False


print(check_passwd(input('Введите пароль на проверку: ')))
