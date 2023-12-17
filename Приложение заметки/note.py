import note_controller


def main():
    while True:
        print()
        print("Введите команду (add, read, edit, delete, list, exit): ")
        command = input().lower()
        if command == "add":
            print("Введите заголовок заметки:")
            title = input()
            print("Введите тело заметки:")
            body = input()
            note_controller.add_note(title, body)
            print("Заметка успешно сохранена.")

        elif command == "read":
            print("Введите идентификатор заметки:")
            note_id = int(input())
            note_controller.read_note(note_id)

        elif command == "edit":
            print("Введите идентификатор заметки:")
            note_id = int(input())
            print("Введите новый заголовок заметки:")
            new_title = input()
            print("Введите новое тело заметки:")
            new_body = input()
            note_controller.edit_note(note_id, new_title, new_body)

        elif command == "delete":
            print("Введите идентификатор заметки:")
            note_id = int(input())
            note_controller.delete_note(note_id)

        elif command == "list":
            note_controller.list_notes()

        elif command == "exit":
            break

        else:
            print("Неверная команда. Пожалуйста, повторите ввод.")


if __name__ == "__main__":
    main()