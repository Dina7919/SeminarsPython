# print('Введите фамилию:')
# familiya=input ()
# print('Введите имя:')
# name=input ()
# print('Введите отчество:')
# otch=input ()
# my_list = ['A', 'A1', 'B', 'B1']
# A1 = my_list[0]
# print('Номер акта:')
# number=input ()
# print('Дата заключения акта:')
# data=input ()
# print('Аудитор: ')
# print(f'\n Фамилия: {familiya} \n Имя: {name} \n Отчество: {otch} \n Уровень специализации: {A1} \n Номер акта: {number} \n Дата заключения акта: {data}')

# print('Введите код показателя:')
# kod_pokaz=input ()
# my_list = ['Da', 'Net']
# Da = my_list[0]
# my_list = ['Уровень ошибок', 'Уровень ошибок в аудиторской проверке','Уровень соответствия стандартам аудита']
# Uroven_oshibok = my_list[0]
# print('Введите уровень ошибок в отчетности:')
# oshibka_otch=input ()
# print('Введите уровень ошибок в аудиторской проверке:')
# oshibka_audit=input ()
# print('Введите уровень соответствия стандартам:')
# standart=input ()
# print('Показатели: ')
# print(f'\n Код показателя: {kod_pokaz} \n Соответствуют ли стандартам? {Da} \n Уровень: {Uroven_oshibok} \n Уровень ошибок в отчетности: {oshibka_otch}')
# print(f'\n Уровень ошибок в аудиторской проверке: {oshibka_audit} \n Уровень соответствия стандартам: {standart}')

# report_code = 3
# executor = "Каримов Карим Каримович"
# report_result = "уровень ошибок отчетности был выявлен, отчет сформирован и отправлен"
# indicator_code = 2
# auditor_code = 1
# check_date = "11.03.2023"

# print("Код отчета:", report_code)
# print("Исполнитель:", executor)
# print("Вывод отчета о результатах:", report_result)
# print("Код показателя:", indicator_code)
# print("Код аудитора:", auditor_code)
# print("Дата проверки:", check_date)

total_errors = 10
total_operations = 3
total_checked_operations = 4
total_requirements_met = 6
total_requirements = 9

reporting_errors_level = total_errors / total_operations
audit_errors_level = total_errors / total_checked_operations
audit_standards_compliance_level = total_requirements_met / total_requirements

print(f'Уровень ошибок отчетности: {reporting_errors_level}')
print(f'Уровень ошибок в аудиторской проверке: {audit_errors_level}')
print(f'Уровень соответствия стандартам аудита: {audit_standards_compliance_level}')











# список. 
# Длины нет. 
# Определенного типа данных нет
list = [9, '6', [3,4], (3,4)]

# картеж неизменяемый
# запятая нужна только в том случае, если запятая одна
my_tuple = (3,)
# print(type(my_tuple))

# множества
mt_tuple = ()
my_set = set([2, 3, 4, 4, 5])
# print(my_set)

# словарь. 
# ключь неизменяемый
my_set = {}

# print(keyword.kwlist) # выведет все элементы, которыми нельзя называть переменные


# 19. Дана последовательность из N 
# целых чисел и число K. 
# Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# my_list = [i for i in range(10)]
# shift = int(input('На сколько сдвигаем вправо?'))
# for _ in range(shift):
#     my_list.insert(0, my_list.pop()) # поп возвращает значение
# print(my_list)

# 21. Напишите программу для печати всех
# уникальных значений в словаре.

# dictionary = {'up': '↑', 'left' : '←', 'down' : '↓', 'right' : '→'}
# keys = set()
# for i in dictionary:
#     for key in dictionary.keys():
#         keys.add(key)
# print(keys)

# dictionary = {'up': '↑', 'left' : '←', 'down' : '↓', 'right' : '→'}
# keys = set()
# for i in dictionary:
#     for (k,v) in i.items():
#         keys.add(k)
# print(k)

# правильное:

# dictionary = {'up': '↑', 'left' : '←', 'down' : '↓', 'right' : '→'}
# unique_values = set()
# for i in dictionary:
#     for value in i.values():
#         unique_values.add(value)
# print(unique_values)

# 23. Дан список, состоящий из целых чисел. 
# Напишите программу, которая 
# подсчитает количество элементов списка, 
# больших предыдущего (элемента с предыдущим 
# номером)

# list = [2, 4, 6, 8, 3, 5, 7, 3, 7]
# count = 0
# print(list)
# for i in range(1, len(list)):
#     if(list[i] > list[i-1]):
#         count+=1
# print(count)

