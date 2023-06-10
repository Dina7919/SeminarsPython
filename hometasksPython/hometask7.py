# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Cтихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

# def print_poem():
#     poem = input("Введите стихотворение, разделяя слова дефисами, а фразы пробелами: ")
#     return poem

# def poem_by_sentences(poem: str):
#     words = poem.split(" ")
#     sentences = list(map(lambda x : x.split(), words))
#     return sentences

# def rythm (sentences: list[str]):
#     vowel_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'A', 'E', 'И', 'Ё', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я']
#     count = 0
#     counts = []
#     letters = [(list(sentences[i])) for i in range(len(sentences))]
#     for i in letters:
#         for j in i:
#             for l in range(len(vowel_letters)):
#                 if j == vowel_letters[l]:
#                     count += 1
#         counts.append(count)
#         count = 0
#     rythm = counts[0]
#     for i in range(len(counts)):
#          if counts[i] != rythm:
#             neravn += 1 
#     if neravn >= 1:
#         unswer = "Пам парам" 
#     else:
#         unswer = "Парам пам-пам"
#     return unswer

# poem = print_poem()
# print(poem)

# semtences = poem_by_sentences(poem)
# print(semtences)

# letters = rythm(semtences)
# print(letters)


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         row = ""
#         for j in range (1, num_columns+1):
#             row += str(operation(i,j)) + " "
#         print(row)
# operation = lambda x, y: x*y
# print_operation_table(operation)