# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B 
# с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def number_in_degree (number, degree): #2, 3
#     if degree == 1:
#         return number
#     return number_in_degree(number, degree-1)*number
# number = int(input('Введите число: '))
# degree = int(input('Введите степень: '))
# print(f'{number} in the {degree}th degree is {number_in_degree(number, degree)}')

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum_of_numbers (number_1, number_2): # 5 2  
    if number_1 == 0:
        return number_2
    elif number_2 == 0:
        return number_1
    return sum_of_numbers(number_1+1, number_2-1)
number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))
print(sum_of_numbers(number_1, number_2))
    