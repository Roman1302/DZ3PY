'''Задача 1 Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
*Пример:*
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

import os
clear = lambda: os.system('clear')
clear()

print("\n***Программа суммы элементов списка, стоящих на нечётной позициях***")

from random import randint

def sum_randome(list_len):
    a,b = 0,9
    lst = [None] * list_len
    for i in range(list_len):
        lst[i] = randint(a,b)
    lst
    print(lst)
    c=0
    for i in range(1, len(lst) , 2):
        a=lst[i]
        c+=a
    print("\n->", c)

try:
    lit_length=int(input("\nВведите целое число случайных чисел: "))
    sum_randome(lit_length)
except:
    print("\nНужно вводить число!")