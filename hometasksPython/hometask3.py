# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# n = int(input("Введите длину списка: "))
# list_numbers = [i for i in range(n)]
# number = int(input("Введите число: "))
# count = 0
# print(list_numbers)
# for i in range(0, len(list_numbers)):
#     if list_numbers[i] == number:
#         count += 1
# print(count)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# n = int(input("Введите длину списка: "))
# from random import randint
# list_numbers = [randint(0, 10) for i in range(n)]
# number = int(input("Введите число: "))
# count = 0
# index = 0
# min_index = 0
# print(list_numbers)
# min = list_numbers[0] # 23
# for i in range(0, len(list_numbers)): # 23 56 75 24 64 (43)
#     if (list_numbers[i] < number): #24 < 43
#         difference = number - list_numbers[i] # 19
#         index = i # 3
#     else:
#         difference = list_numbers[i] - number # 
#         index = i # 
#     if (min > difference): #13 > 19
#         min  = difference # 13
#         min_index = index # 1
# print(list_numbers[min_index])


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; 
# Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.

# *Пример:*

# ноутбук
#     12

play_eng = {1 : ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 2 : ['D', 'G'], 3 : ['B', 'C', 'M', 'P'], 4 : ['F', 'H', 'V', 'W', 'Y'], 5 : ['K'], 8 : ['J', 'X'], 10 : ['Q', 'Z']}
play_rus = {1 : ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 2 : ['Д', 'К', 'Л', 'М', 'П', 'У'], 3 : ['Б', 'Г', 'Ё', 'Ь', 'Я'], 4 : ['Й', 'Ы'], 5 : ['Ж', 'З', 'Х', 'Ц', 'Ч'], 8 : ['Ш', 'Э', 'Ю'], 10 : ['Ф', 'Щ', 'Ъ']}
word_eng = input("Введите слово на английском: ")
word_eng_1 = word_eng.upper()
print(word_eng_1)
sum = 0
words_list = []  
for i in word_eng_1: 
    words_list.append(i) 
for (k,v) in play_eng.items():
    v_eng = []
    v_eng = v
    for i in words_list: # 0-3 (0) 'M'
        for l in v_eng: # A ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
            if l == i: # 'A' = 'M'
                sum += k 
print(sum)

sum = 0

word_rus = input("Введите слово на русском: ")
word_rus_1 = word_rus.upper()
for i in word_rus_1: 
    words_list.append(i) 
for (k,v) in play_rus.items():
    v_rus = []
    v_rus = v
    for i in words_list: 
        for l in v_rus: 
            if l == i: 
                sum += k 
print(sum)