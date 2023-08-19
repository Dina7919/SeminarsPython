import Model.function as f
import Controller.Menu as Menu
from Model import Notes

# здесь мы запускаем программу, где в зависимости от введенной команды пользователем произойдет той или иной метод
def run():
    command = ""
    
    while command != "EXIT":
        Menu.menu()
        command = input().strip().upper()
        #вывод всех заметок из файла
        if command == 'LIST':
            f.show('all')
            #добавление заметки
        if command == 'CREATE':
            f.add()
            #удаление заметки
        if command == 'DELETE':
            f.show('all')
            f.id_edit_del_show('del')
            #редактирование заметки
        if command == 'EDIT':
            f.show('all')
            f.id_edit_del_show('edit')
            #выборка заметок по дате
        if command == 'SORT':
            f.show('date')
            #показать заметку по id
        if command == 'ID':
            f.show('id')
            f.id_edit_del_show('show')
            #закрытие файла
        if command == 'EXIT':
            Menu.goodbuy()
            break

        notes = []
        def init(self, notes):
            self.notes = notes

        def testData(notes):
            if len(notes) > 0:
                return True
            else:
                return False
            
        def update(notes):
            notes.notes = Notes.Notes.map_note(notes)
            if testData(notes):
                Notes.Notes.map_note
            else:
                print("Список заметок пуст!")