from itertools import zip_longest #для zip. если например несовпадает количество элементов первого и второго списка
# map - ф-ция высшего порядка. В качестве ф-ции принимает другие ф-ции.
# Делает код почище. Принимаем ф-цию ко всем элементам коррекции
# filter - если true - пропускает, если false - не пропускает
#enumerate - нумерация коллекции
#zip - сбор в картежи
#lambda - та же самая ф-ция

# обычный код 
# my_string = '1234e56s78g90'
# my_string = list(my_string)
# print(my_string)

# for i in range (len(my_string)):
#     my_string[i] = int(my_string[i])

# print(my_string)

# в map

# my_string = list(map(int, my_string))
# print(my_string)

# my_string = list(map(lambda x: x + '1', my_string))
# print(my_string)

# my_string = list(map(функция, коллекция))

# filter

# my_string = list(filter(lambda x: not x.isdigit(), my_string))
# print(my_string)

# enumerate

# for i in enumerate(my_string):
#     print(i)

# for i, item in enumerate(my_string):
#     print(i, item)

my_num = '1234567890'
my_let = 'sgdjfndkwkesf'
list_1 = list(my_num)
list_2 = list(my_let)
# print(list_1)
# print(list_2)

# new_list = []
# # for i, item in enumerate(list_1):
# #     new_list.append((list_1[i], list_2[i]))

# new_list = list(zip(list_1, list_2))
# print(new_list)
# new_list = list(zip_longest(list_1, list_2, fillvalue='Ничего'))
# print(new_list)

# def is_digit(num: str):
#     return num.isdigit()
# lambda x: x.isdigit() # из метода сделали функцию

# Задача_1. У вас есть код, который вы не можете менять (так часто бывает когда код в глубине программы используется множество раз и вы не хот ите ничего сломать);
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] или любой другой список
# transformed_values = list(map[transformation, values])
# Единственный способ вашего взаимодействия с кодом - посредством задания функции transformation
# однако вы поняли, что для вашей текущей задачи не нужно никак преобразовывать список значений, а нужно получить его как есть
# напишите такое лямбда-выражение transformation, чтобы transformation_values получился копией values. 

# transformation = lambda x : x

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# transformed_values = list(map[transformation, values])

# Задача_2. Планеты вращаются вокруг звёзд по эллиптическим арбитам
# Назовём самой далекой планетой ту, арбита которой имеет самую ьольшую площадь
# Напишите ф-ция find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по которой вращается самая далёкая планета
# Круговые арбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были запущены на круговые арбитф
# Результатом ф-ции должен быть картеж, содержащий длины полуосей эллипса орбиты самой далекой планеты
# Каждая орбита представляет из себя кортеж из пару чисел - полуосей ее элипса.
# Площадь эллипса вычисляется по формуле: s = piab, где a и b - длины полуосей эллипса
# При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: вначале вычислить самуцю большую площадь эллипса,
# а затем найти сам эллипс, имеющий такую площадь
# Гарантируется, что самая далекая планета ровно одна

# import random

# def generate_sequence_of_orbits(count_of_orbits: int) -> list[tuple[int, int]]:
#     result = [(random.randint(1,10), random.randint(1, 10)) for _ in range(count_of_orbits)]
#     return result

# def find_farthest_orbit(list_of_orbits: list[tuple[int, int]]) -> tuple[int, int]:
#     squeres = [(i, kortej[0]*kortej[1]) for i, kortej in enumerate(list_of_orbits) if kortej[0] != kortej[1]]
#     max_squeres = max(squeres, key = lambda x : x[1])
#     return list_of_orbits[max_squeres[0]]

# orbits = generate_sequence_of_orbits(10)
# print(orbits)
# print(find_farthest_orbit(orbits))

# Задача_3
# Напишите функцию sane_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращает True.
# если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

def same_by(characteristic, objects) -> bool:
    return len(set(map(characteristic, objects))) <= 1

col = [2, 4, 8, 22, 14, 13] #объекты

print(same_by(lambda x: x % 2, col)) #характиристика