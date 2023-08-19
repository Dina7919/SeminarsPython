print(5, 8, 6)
n = 5
print(n)
l = None
print(l)
m = 1.89
print(m)
n = 'fddf'
n2 = "vfjfkf"
print(n)
print(n2)

n = 'hygkgb'
print(type(n))

n = 'fd\'df'
print(n)

print(5)
print(5)
print(5)

# print(5, 8)
print(5)
print(5, 9)

"""
cascascas
aqscascasc
qcdaccacac
"""
# print(5)
# print(5)
# print(5)  
#ctrlk + ctrlc - комментировать
# ctrlk + ctrlu - раскоментировать

print(5)
print(5)
print(5)

a = 5
b = 5.89
c = 'hello'
print(a, b, c) #выводим сразу несколько строк
print(a, ' - ', b, ' - ', c) #вывод переменных чере- дефис
print(f"{a} - {b} - {c}") #мы берем значения переменной
print("{} - {} - {}".format(a,b,c))

print('Введите первое число: ')
input() #ввод данных
a = input()
print(a) #вывод введенного числа

b = input('Введите второе число: ')
print(a, ' + ', b, ' = ', a + b) #выводит склеивание двух переменных

# приведение переменных
c = 5.89
print(c)
print(type(c))
n = int(c)
print(n)
print(type(n))
# изменили тип переменной

#исправление вышенаписанного кода
print('Введите первое число: ')
a = int(input())
b = int(input('Введите второе число: '))
print(a, ' + ', b, ' = ', a + b) #выводит склеивание двух переменных

# округление чисел 
a = 5.89956
b = 6.484964
print(round(a*b, 3))

iter = 2
iter += 3 # iter = iter - 3
iter -= 4
iter *= 5
iter /= 6
iter //= 7
iter %= 8
iter **= 9

# логические операциии
a = 1 < 4 and 5 > 2 #логическое и 
print(a)

a = 1 == 2 # == - оператор равенства
print(a)

a = 1 != 2 # логическое не
print(a)

a = 'qwe'
b = 'wer'
print(a == b) #логическое равно

a = 1 < 3 < 5 < 10 #сравнение чисел
print(a)

# сложные условия + табуляция
username = input ('Введите имя: ')
if username == 'Маша':
    print('Ура, это же Маша!')
elif username == 'Марина':
    print('Я так ждала Вас Марина!')
elif username == 'Паша':
    print('Паша - топ')
else:
    print('Привет, ', username)

# программа с while
i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит')
print(i)

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: #если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1

# циклы for и range
a = 'qwerty'
print(a[2])
for i in a:
    print(i) #выведется слово построчно

line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)

text = 'Съушь еще Этих МяГкИх французских булочек'
print ('еще' in text) #ищет элементы в строке
print(text.upper()) #выводит все в верхнем решистре
print(text.lower()) #выводит все в нижнем решистре
print(text.replace('еще', 'ЕЩЁ')) # замена одного слова на другое
print(text[0])
print(text[1])
print(text[len(text)-1])
print(text[-1]) #индексация будет начинаться с обратной стороны
print(text[:]) #выводим все символы
print(text[:2]) #выводим элементы с 0 по 2
print(text[len(text)-2:]) # со такого то элемента до конца
print(text[2:9]) # от 2 до 9 не включая
print(text[6:-18]) #идём в обратную сторону
print(text[0:len(text):6]) #идём от 0 до конца строки с шагом 6
print(text[::6]) # тоже самое, что и наверху
text = text[2:9] + text[-5] + text[:2] 
print(text)







