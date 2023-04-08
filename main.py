import input
import csv
from encodings import utf_8



def note_creator():
    note = input("Создание заметки в формате -> ID Тело заметки: ")
    note = note.split()
    return note

def new_note():
    note = note_creator()
    input.notepad_fill(note)
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
        id_note = input.note_id().split()

        for line in read_data:
            if line == []:
                continue
            if id_note in (line[0:1]):
                result += str(line[0:]) + '\n'

    return result
