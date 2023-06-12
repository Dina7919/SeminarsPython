# my_string = 'shdjfncjdbsjnc'

# my_list = list(my_string)

# print(my_list)

# # Напишите программу, которая принимает 
# # на вход строку, и отслеживает, сколько раз
# #  каждый символ уже встречался. 
# # Количество повторов добавляется к 
# # символам с помощью постфикса формата _n. 
# # Input: a a a b c a a d c d d 
# # Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# my_string = 's f h d s f h k g d a d h j f s'
# my_list = my_string.split()
# print(my_list)
# dict_count = {}
# for letter in my_list:
#     dict_count[letter] = dict_count.get(letter, 0) + 1 # если есть значение, то добавим letter, если нет, то 0
#     print(letter if dict_count.get(letter) == 1 else 
#           f'{letter}_{dict_count.get(letter) - 1}', end= ' ')

# Задача №27. Решение в группах 
# Пользователь вводит текст(строка). 
# Словом считается последовательность 
# непробельных символов идущих подряд, 
# слова разделены одним или 
# большим числом пробелов. 
# Определите, сколько различных слов 
# содержится в этом тексте. 
# Input: She sells sea shells on the sea 
# shore The shells that she sells are 
# sea shells I'm sure.So if she sells 
# sea shells on the sea shore 
# I'm sure that the shells are sea shore 
# shells Output: 13

# str_split = input('Enter text: ').lower()

# str_cnt = {}

# for word in str_split:
#     str_cnt[word] = str_cnt.get(word, 0) + 1 # если есть значение, то добавим letter, если нет, то 0
#     for (k,v) in str_cnt.items(): # k - ключ, v - значение
#         if (k == ' '):
#             count = v
# print(f'Number of words in the text is: {count+1}')

# Правильное решение:

# import string

# my_string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore".lower()

# for ch in string.punctuation:
#     my_string = my_string.replace(ch, ' ')

# text = set(my_string.split())
# print(text)
# print(len(text))

# Задача №29. 
# Решение в группах Ваня и Петя поспорили, 
# кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных
# целых чисел. Требуется определить значение
# наибольшего элемента последовательности, 
# которая завершается первым встретившимся 
# нулем (число 0 не входит в 
#        последовательность)”. 
# Однако 2 друга оказались не такими 
# смышлеными. Никто из ребят не смог 
# до конца сделать это задание. 
# Они решили так: у кого будет 
# меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, 
# студентам.

# n = 1
# max_number = -1
# while n != 0:
#     if n > max_number:
#         max_number = n
#     n = int(input('Введите число: '))
# print(max_number if max_number != -1 else "Вы ничего не ввели")

# Правильное решение

# num = int(input('Введите число: '))
# max_value = -1

# while num != 0:
#     if max_value < num:
#         max_value = num
#     num = int(input('Введите число: '))
# print(max_value if max_value != -1 else 'Список пуст')

# 2 задачи в одну

import random 

my_list = [random.randint(0, 50) for _ in range (20)]
print(my_list)
number = int (input('Введите искомое число: '))
count_num = my_list.count(number)
print(f'count_num: {count_num}')

closest = my_list[0]
if count_num == 0:
    for num in my_list:
        if abs(number - num) < abs(number - closest):
            closest = num
print(count_num if count_num > 0 else f'Ближайшее к {number} число {closest}')