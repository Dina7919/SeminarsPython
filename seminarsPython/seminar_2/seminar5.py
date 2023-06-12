# 1. Последовательностью Фибоначчи 
# называется последовательность 
# чисел a0, a1, ..., an, ..., где

# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

# Требуется найти N-е число Фибоначчи

# def fibo(n): #5  0 1 1 2 3 5 8 
#     if n in [0, 1]: #5 in [0,1]
#         return n 
#     return fibo(n-1) + fibo(n-2) #3+2/2+1/1+1/0+1
# n = int(input('Enter a number: '))
# print(f'The element #{n} of Fibo sequence is: {fibo(n)}')

# def func(n): #3
#     if n == 0: 
#         return 1
#     return 1 + func(n-1) 
# print(func(5))

# 2. Хакер Василий получил доступ к 
# классному журналу и хочет заменить все 
# свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет 
# оценки Василия, но наоборот: 
# все максимальные – на минимальные.

# import random
# marks = [random.randint(1,5) for _ in range(10)]
# print(marks)
# max_marks = max(marks)
# min_marks = min(marks)
# for i in range (len(marks)):
#     if marks[i] == max_marks: marks[i] = min_marks
# print(marks)

# 3. Напишите функцию, 
# которая принимает одно число и 
# проверяет, является ли оно простым

# def prime_numbers (n, div=2): #div - делитель
#     if div == n//2 + 1:
#         print('yes')
#     elif n % div == 0:
#         print(f'no, делитель {div}')
#     else:
#         prime_numbers(n, div+1)
# value = int(input('Введите число: '))
# prime_numbers(value)

# правильное решение:

# def is_simple(num: int) -> bool:
#     if num in [1,2]:
#         return True
#     elif num%2 == 0:
#         return False
#     else:
#         for i in range(3, num//2+1, 2):
#             if num%i == 0:
#                 return False
#     return True
# num = int(input('Введите число: '))
# print(f'Число {num} ' + ('простое' if is_simple(num) else 'составное'))

# Задача 4 
# Дано натуральное число N и 
# последовательность из N элементов. 
# Требуется вывести эту последовательность 
# в обратном порядке.

# def fibo(n): #5  0 1 1 2 3 5 8 
#     if n in [0, 1]: #5 in [0,1]
#         return n 
#     return fibo(n-1) + fibo(n-2) #3+2/2+1/1+1/0+1
# n = int(input('Enter a number: '))
# print(f'The element #{n} of Fibo sequence is: {fibo(n)}')

# def print_sequence(n: int, s='') -> str:
#     if n != 0:
#         s = s + str(n) + ' '
#         return print_sequence(n-1, s)
#     else:
#         return s
# n = int(input('Введите N:'))
# print(print_sequence(n))

def reverse_list(num:int) -> str:
    if num == 0:
        return ''
    return f'{num} ' + reverse_list(num-1)


