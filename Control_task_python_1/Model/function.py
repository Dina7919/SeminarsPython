import Model.Import_to_file as Import_to_file
import Model.Notes as Notes
import Controller.Menu as Menu

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки

# данный метод добавляет заметку в файл
def add():
    note = Menu.create_note(number)
    note_in_file = Import_to_file.read_file()
    for notes in note_in_file:
        if Notes.Notes.get_id(note) == Notes.Notes.get_id(notes):
            Notes.Notes.set_id(note)
    note_in_file.append(note)
    Import_to_file.write_file(note_in_file, 'a')
    print('Заметка добавлена...')

# данный метод показывает определенную информацию в зависимости от выбора пользователя
def show(text):
    logic = True
    note_in_file = Import_to_file.read_file()
    # выборка заметок по дате
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
        # вывод всех заметок
    for notes in note_in_file:
        if text == 'all':
            logic = False
            print(Notes.Notes.map_note(notes))
            # вывод заметок по ID
        if text == 'id':
            logic = False
            print('ID: ' + Notes.Notes.get_id(notes))
    # сортировка заметок по дате
        if text == 'date':
            logic = False
            if date in Notes.Notes.get_date(notes):
                print(Notes.Notes.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')

#данный метод удаляет заметку либо же изменяет её в зависимости от того что ввел пользователь
def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    note_in_file = Import_to_file.read_file()
    logic = True
    for notes in note_in_file:
        if id == Notes.Notes.get_id(notes):
            logic = False
            # изменение заметки
            if text == 'edit':
                note = Menu.create_note(number)
                Notes.Notes.set_title(notes, note.get_title())
                Notes.Notes.set_body(notes, note.get_body())
                Notes.Notes.set_date(notes)
                print('Заметка изменена...')
                # удаление заметки
            if text == 'del':
                note_in_file.remove(notes)
                print('Заметка удалена...')
                # вывод всех заметок
            if text == 'show':
                print(Notes.Notes.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    Import_to_file.write_file(note_in_file, 'a')