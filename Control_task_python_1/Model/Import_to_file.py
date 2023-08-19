import Model.Notes as Notes

# данный метод записывает заметку в файл
def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Notes.Notes.to_string(notes))
        file.write('\n')
    file.close

# данный метод считывает заметку с файла
def read_file():
    try:
        note_in_file = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Notes.Notes(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            note_in_file.append(note)
    except Exception:
        print('Список заметок пуст...')
    finally:
        return note_in_file