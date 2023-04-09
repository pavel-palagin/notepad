import input_data
import main

power_on = True
while power_on:
    func_select = main.function_select()
    if func_select == 1:
        while True:
            search_select = main.search_select()
            if search_select == 1:
                name = main.search()
                print(name)
                search_select = main.search_select()
            if search_select == 2:
                break
    if func_select == 2:
            while True:
                redact = main.notepad_redact()
                if redact == 1:
                    note = main.new_note()
                    print(f'Новая заметка {note} добавлена в список ')
                    break
                if redact == 2:
                    func_select = main.function_select()
                    break
                else:
                    print('Вы ввели недопустимое значение, попробуйте снова!')
                    redact = main.notepad_redact()
    if func_select == 3:
       main.notepad_read()
       print()
    if func_select == 4:
            print()
            power_on = False