'''Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
*Пример:*
- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

import os
clear = lambda: os.system('clear')
clear()

print("\n***Программа преобразования десятичного числа в двоичное***")

def binary(num):
    result = []
    while True:
        if num != 0:
            if num % 2 == 0:
                result.append(0)
                num = num // 2
            elif num % 2:
                result.append(1)
                num = num // 2
        else:
            result.reverse()
            print("=>", *result, sep="")
            break

try:
    number=int(input("\nВведите число: "))
    binary(number)
except:
    print("\nНужно вводить число!")