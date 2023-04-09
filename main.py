import input_data
import csv
from encodings import utf_8



def note_creator():
    note = input('Создание заметки в формате -> ID Тело заметки: ')
    note = note.split()
    return note

def new_note():
    note = note_creator()
    input_data.notepad_fill(note)
    return note


def notepad_redact():
    redact = input('Выберите действие: \
                    1. Создать новую заметку\
                    2. Назад ')
    if not redact.isdigit() and int(redact)<1 or int(redact)>2:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        redact = notepad_redact()
    print()
    return int(redact)



def search():
    result = ''
    with open('notepad.csv', encoding='utf_8') as pd:
        read_data = csv.reader(pd, delimiter="|")
        id_note = input_data.note_id()

        for line in read_data:
            if line == []:
                continue
            if id_note in line:
                result += str(line[0:]) + '\n'

    return result


def notepad_read():
    with open('notepad.csv', 'r', encoding='utf_8') as pd:
        csv.register_dialect('my_dialect', delimiter='|', lineterminator="\r\n")
        reader = csv.reader(pd, 'my_dialect')
        for row in reader:
            print(row)



def function_select():
    func_select = input('Выберите режим работы:\
                    1. Поиск заметки\
                    2. Редактор списка заметок\
                    3. Открыть список заметок\
                    4. Выход ')
    if not func_select.isdigit() and int(func_select)<1 or int(func_select)>4:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        func_select = function_select()
    else:
        print()
    return int(func_select)

def search_select():
    srch_select = input('Выберите режим поиска:\
        1. Поиск по ID\
        2. Назад ')
    if not srch_select.isdigit() and int(srch_select)<1 or int(srch_select)>3:
        print('Вы ввели недопустимое значение, попробуйте снова ')
        srch_select = search_select()
    print()
    return int(srch_select)