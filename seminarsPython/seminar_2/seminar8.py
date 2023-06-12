# Задача_1. Написать программу, которая представляет собой телефонный справочник
# Поля - имя, телефон, комментарий (3 поля)
# добавление, удаление, изменение, считывание, сохранение
# 1 открыть файл (.txt)
# 2 сохранить файл
# 3 показать все контакты
# 4 добавить контакт
# 5 изменить контакт 
# 6 найти контакт
# 7 удалить контакт
# 8 выход

# path = 'seminar8.txt'
# data = open(path, ':')
# for line in data:
#     print(line)
# data.close()

def open_file_read(path):
    with open(path, 'r') as file:
        main_list = file.readlines()
        main_list_str = [x.rstrip().split(':') for x in main_list]
    return main_list_str

print(open_file_read('seminar8.txt'))

def open_file_write(path, list_file):
    with open(path, 'w') as file:
         file.writelines([':'.join(x) + '\n' for x in list_file])
list_file = [['lyglyuhgbl', 'yuhbliu', 'yvkijin'], ['lyglyuhgbl', 'yuhbliu', 'yvkijin']]
open_file_write('seminar8_1.txt', list_file)

list_for_look = [['Sergeyev', 'Sergey', '+998906453728', 'comment'], ['Ivanov', 'Ivan', '+998906485937', 'comment'], ['Aleksandrov', 'Aleksandr', '+998904658364', 'commentcd']]
def look_list(list_for_look):
    print([' '.join(x) for x in list_for_look], end = '\n')
look_list(list_for_look)

contacts = {}
def add_contact():
    name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    contacts[name] = phone_number
    print(f'Контакт {name} добавлен')

def edit_contact():
    name = input("Введите имя: ")
    if name in contacts:
        new_phone_number = input("Введите новый номер телефона: ")
        contacts[name] = new_phone_number
        print(f"Контакт {name} успешно изменен.")
    else:
        print("Контакт не найден.")

def find_contact():
    name = input("Введите имя контакта: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Контакт не найден.")

def delete_contact():
    name = input("Введите имя контакта: ")
    if name in contacts:
        del contacts[name]
        print(f"Контакт {name} успешно удален.")
    else:
        print("Контакт не найден.")

while True:
    print("""
Меню:
1. Открыть файл
2. Сохранить файл
3. Показать все контакты
4. Добавить контакт
5. Изменить контакт
6. Найти контакт
7. Удалить контакт
8. Выход
""")
    choice = input("Выберите действие: ")
    if choice == "1":
        open_file_read('seminar8.txt')
    elif choice == "2":
        open_file_write('seminar8.txt', 'seminar8_1.txt')
    elif choice == "3":
        look_list(list_for_look)
    elif choice == "4":
        add_contact()
    elif choice == "5":
        edit_contact()
    elif choice == "6":
        find_contact()
    elif choice == "7":
        delete_contact()
    elif choice == "8":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
