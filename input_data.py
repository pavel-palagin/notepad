import csv
from encodings import utf_8

def note_id():
    id_note = input("Введите id заметки: ")
    while True:
        for char in id_note:
            if char.isdigit():
                return id_note
            else:
                print("Вы ввели недопустимый символ, попробуйте снова")


def note_body():
    body_note = input("Новая заметка: ")
    while True:
        return body_note

def notepad_fill(note):
    with open('notepad.csv', 'a', encoding='utf_8') as np:
        csv.register_dialect('my_dialect', delimiter='|', lineterminator="\r\n")
        writer = csv.writer(np, 'my_dialect')
        writer.writerow(note)




