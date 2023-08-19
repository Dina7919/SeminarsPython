# # Списки
# #1-способ

# list_1 = [] # пустой список
# list_1 = list() 
# list_1 = [1, 2, 3, 8]
# print(list_1)
# print(*list_1) # перечисление чисел без скобок

# for i in list_1:
#     print(i) #перечисление числел 

# print(len(list_1)) # длина списка
# print(list[3]) #выводим элементы по индексам

# # добавление элементов

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # 8 добавляется в конец
# print(list_1)
# list_1 = []
# print(list_1)
# for i in range(5): # добавление значений от 0 до 4
#     list_1.append(i)
#     print(list_1)

# # удаление элементов

# list_1 = [12, 7, -1, 21, 0]
# a = list_1.pop()
# print(a) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# # удаление конкретного элемента из списка

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(1)) # 12
# print(list_1) # [7, -1, 21, 0]

# # добавление элемента на нужную позицию

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]

# # вваод элементов

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])              #1
# print(list_1[1])              #2
# print(list_1[-1])             #10
# print(list_1[-5])             #6
# print(list_1[:])              #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])             #[1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9])            #[3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])          #[]
# print(list_1[0:len(list_1):6])#[1, 7]
# print(list_1[::6])            #[1, 7]

# Кортежи

# t = () # пустой кортеж
# print(type(t))

# t = (1)
# print(type(t))

# t = (1, 5, 3,)
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))

# v = tuple(v) # преобразование в кортеж
# print(v)
# print(type(v))

# # распаковка кортежа 

# a, b = 1, 2 #присваивание
# a,b,c = v
# print(a, b, c)

# # Чем кортеж отличается/схожен со списком

# t = (1, 2, 3, 5,)
# for i in range(len(t)):
#     print(t[i]) # все работает
# t[0] = 2 # ошибка

# #это тоже самое что и список, но изменять их мы не можем

# # Словари

# d = {}
# d = dict()
# d['q'] = 'qwerty'
# print(d)
# d['w'] = 'werty'
# print(d['q'])

# # работа со словарями

# dictionary = {}
# dictionary = {'up': '↑', 'left' : '←', 'down' : '↓', 'right' : '→'}
# print(dictionary)
# print(dictionary['left'])
# print(dictionary['up'])
# dictionary['left'] = '⇐'
# print(dictionary['left'])
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
# # up : ↑
# # down : ↓
# # right : →
# dictionary[895] = 98998
# print(dictionary)
# print(dictionary.items())
# for (k,v) in dictionary.items(): # k - ключ, v - значение
#     print(k, v)
# # up : ↑
# # down : ↓
# # right : →

# Множества

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors) # вводится в конец
# colors.remove('red')
# print(colors) #error
# colors.discard('red') #ok
# print(colors)
# colors.clear() # удаление всех значений
# print(colors) #set()

# # Операции со множествами

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# # замороженное множество (не можем его изменять)

# a = {1, 8, 6}
# b = frozenset(a)
# print(b)

# Ошибки:

# # SyntaxError (Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first > number_second # !!!!!
# print(number_first)
# # Отсутствие :

# # IndentationError (Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first)
# # Отсутствие отступов

# # TypeError (Типовая ошибка)
# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа

# # ZeroDivisionError (Деление на 0)
# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя

# # KeyError(Ошибка ключа)
# dictionary = {1:'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует

# #NameError (Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существкет

# # ValueError (Ошибка значения)
# text = 'Python'
# print(int(text))
# # нельзя символы перевести в целые числа