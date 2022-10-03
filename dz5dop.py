'''задача5 HARD необязательная.
Сгенерировать массив случайных целых чисел размерностью m*n 
(размерность вводим с клавиатуры) , причем чтоб количество элементов было четное. 
Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива, 
причем чтобы каждый гарантированно переместился на другое место 
и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, 
то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.'''

import os
clear = lambda: os.system('clear')
clear()

print("\n***Программа перемешивания значений в таблице***")

from random import randint
len_mass = int(input("Количество столбцов: ")) # задаем длину массива(списка из списков)
len_elem = int(input("Количество строк: ")) # количество элементов в элементе(подсписке)
if (len_mass*len_elem)%2==0:
    a,b = 10,99 # диапазон, можно задавать через input()
    mass = [[randint(a,b) for _ in range(len_elem)] for _ in range(len_mass)] #задаем рандомный массив
    for i in range(len(mass)): #выводим на печать 
        for j in range(len(mass[i])):
            print(mass[i][j], end='    ')
        print()

    print("--------------")

    mass2 = [[randint(a,b) for _ in range(len_elem)] for _ in range(len_mass)] #задаем рандомный массив
    a=mass[0][0]
    if len_elem<len_mass:
        b=mass[len_elem-1][len_mass-1]
    else: 
        r=len_elem
        len_elem=len_mass
        len_mass=r
        b=mass[len_elem-1][len_mass-1]
    for i in range(len(mass)): #выводим на печать 
        for j in range(len(mass[i])):
            mass2[i][j] = mass[j][i]
            mass2[0][0]=b
            mass2[len_elem-1][len_mass-1]=a
            print(mass2[i][j], end='    ')
        print()
else:
    input("\nТаблица не соответствует условиям")


        
    
