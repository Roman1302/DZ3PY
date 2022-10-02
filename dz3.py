'''Задача 3. Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным 
и минимальным значением дробной части элементов.
*Пример:*
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

import os
clear = lambda: os.system('clear')
clear()

print("\n***Программа нахождения разницы между максимальным \nи минимальным значением дробной части элементов***")

import random

def composition(list_len):
    lst = [None] * list_len
    for i in range(list_len):
        lst[i] = round(random.uniform(0.0, 119.9),2)
    lst
    print(lst)
    
    for i in range(list_len):
        while lst[i]>=1:
            lst[i]=round((lst[i]-1),2)
        lst[i]
    lst
    # print(lst)
    
    min = lst[0]
    for a in lst:
        if a < min:
            min = a
    # print ("min: ", min)

    max = lst[0]
    for a in lst:
        if a > max:
            max = a
    # print("max: ", max)

    a=max-min
    print("=>", round(a,2))

try:
    lit_length=int(input("\nВведите целое число случайных чисел: "))
    composition(lit_length)
except:
    print("\nНужно вводить число!")