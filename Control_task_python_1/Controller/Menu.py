import Model.Notes as Notes

# данный метод создает заметку и проверяет на минимальное количество символов
def create_note(number):
    id = (input('ID: '))
    title = (input('Заголовок: '))
    body = len_of_note_check(
        input('Описание: '), number)
    return Notes.Notes(title=title, body=body, id=id)

# метод главного меню
def menu():
    print("\n' <<<ЗАМЕТКИ>>> \n\n Введите команду:\n\n LIST \n CREATE \n DELETE \n EDIT \n SORT \n ID \n EXIT \n")

# данный метод проверяет длину заметки
def len_of_note_check(text, number):
    while len(text) <= number:
        print(f'Минимальное количество символов - {number} \n')
        text = input('Введите заметку: ')
    else:
        return text


def exit():
    print("Спасибо за пользование, хорошего дня!")