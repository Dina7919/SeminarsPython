# TIME = 500



# num = input('Введите число')
# # num_str = str(num)



# for i in range(10): # делает последовательность от 1 до 10
#     print(i)

# for - foreach
# while - просто while

# Задача_1

# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# number = int(input('Введите пробел: '))

# fact = 1
# i = 1

# while i <= number:
#     fact *= 1
#     i = i+1

# print(fact)

# for i in range(1, number+1):
#     fact *= i
# print(fact)

# for i in range(number):
#     fact *= i
# print(fact)

# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = int(input('Введите натуральное число: '))
# # 1 2 3 5 8 13
# i = 0
# first = 1
# second = 2
# while i <= a:
#     fibonacci = first + second
#     i += 1
#     first = second
#     second = fibonacci
#     # print(fibonacci)
#     if (fibonacci == a):
#         print("number = ")
#         print(i)

# number = int(input("Введите число: "))
# first = 0
# second = 1
# index = 1
# while second < number:
#     first, second = second, first + second #первая позиция ровна первой позиции. Вторая позиция ровна 2-й позиции: first = second, second = first + second
#     index += 1
# print(index if second == number else -1)

# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. 
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. 
# Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе.

# import random
# today = 0
# random.randint(-3,3)
# i = 0
# while(i < 30):
#     temp = random.randint(-3,3)
#     print(temp)
#     if (temp < 0):
#         today = 0
#     if (temp > 0 ):
#         today = today + 1
#     i = i + 1
# print("today = ")
# print(today)

# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

import random
n = int(input('Введите количество арбузов: '))
max_weight = 0
index = 0
arbuz = 0
while(index < n):
    arbuz = random.randint(10000,30000)
    min_weight = arbuz
    print(arbuz)
    if (arbuz > max_weight):
        max_weight = arbuz
    if (arbuz < min_weight):
        arbuz = min_weight
    index = index + 1
print(max_weight) 
print(min_weight)


# i = 0
# while(i < 30):
#     temp = random.randint(-3,3)
#     print(temp)
#     if (temp < 0):
#         today = 0
#     if (temp > 0 ):
#         today = today + 1
#     i = i + 1
# print("today = ")

