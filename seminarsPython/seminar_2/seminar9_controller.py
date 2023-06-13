import seminar9_view
import seminar9_model
import seminar9_test

def start():
    while True:
        choice = seminar9_view.main_manu()

        match choice:
            case 1:
                seminar9_model.open_pb()
                seminar9_view.print_message(seminar9_test.load_successful)
            case 2:
                seminar9_model.save_pb()
                seminar9_view.print_message(seminar9_test.save_successful)
            case 3:
                pb = seminar9_model.get_pb()
                seminar9_view.print_contacts(pb, seminar9_test.pb_empty)
            case 4:
                contact = seminar9_view.input_contact(seminar9_test.input_new_contact)
                name = seminar9_model.add_contact(contact)
                seminar9_view.print_message(seminar9_test.new_contact_successful(name))
            case 5:
                key_word = seminar9_view.input_search(seminar9_test.input_search)
                result = seminar9_model.search_contact(key_word)
                seminar9_view.print_contacts(result, seminar9_test.empty_search(key_word))
            case 6:
                key_word = seminar9_view.input_search(seminar9_test.input_change)
                result = seminar9_model.search_contact(key_word)
                if result:
                    if len(result) != 1:
                        seminar9_view.print_contacts(result, '')
                        current_id = seminar9_view.input_search(seminar9_test.input_index)

                    else:
                        current_id = result[0].get('id')
                    new_contact = seminar9_view.input_contact(seminar9_test.change_contact)
                    name = seminar9_model.change_contact(new_contact, current_id)
                    seminar9_view.print_message(seminar9_test.change_successfull(name))
                else:
                    seminar9_view.print_message(seminar9_test.empty_search(key_word))
            case 7:
                pass
            case 8:
                break

