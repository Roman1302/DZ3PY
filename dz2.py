'''Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

import os
clear = lambda: os.system('clear')
clear()

print("\n***Программа суммы элементов списка, стоящих на нечётной позициях***")

from random import randint

def composition(list_len):
    a,b = 0,9
    lst = [None] * list_len
    for i in range(list_len):
        lst[i] = randint(a,b)
    lst
    
    if list_len%2==0:
        c = [None] * int(list_len/2)
        for i in range(len(c)):
            c[i]=lst[i]*lst[-i-1]
        print("\n", lst, "=>", c)
    else:
        c = [None] * int(list_len/2+1)
        for i in range(len(c)):
            c[i]=lst[i]*lst[-i-1]
        print("\n", lst, "=>", c)
    return
    
try:
    lit_length=int(input("\nВведите целое число случайных чисел: "))
    composition(lit_length)
except:
    print("\nНужно вводить число!")