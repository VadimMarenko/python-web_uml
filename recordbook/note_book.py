from note_classes import NoteRecord, Note, Tag, n_book
from decorator import input_error
from datetime import datetime
from cl_interface import ConsoleInterface

cli = ConsoleInterface()


@input_error
def func_exit(*args):
    # save_noteDB(path_note)
    return "Good bye!"


# =========================================================
# Блок функцій для роботи з нотатками
# =========================================================
# >> note add <текст нотатки будь-якої довжини> <teg-ключове слово>
# example >> note add My first note in this bot. Note
# =========================================================
@input_error
def note_add(*args):
    key = str(datetime.now().replace(microsecond=0).timestamp())
    note = Note(" ".join(args[:]))
    arg_tag = input("Tag input >>> ")
    tag = Tag(arg_tag)
    record = NoteRecord(key, note if note else "", tag if note else "")
    return n_book.add_record(record)


# =========================================================
# num record to key
# =========================================================
def note_key(*args):
    for i, key in enumerate(n_book.keys(), 0):
        if i == int(args[0]):
            return key


# =========================================================
# >> note del <номер запису>
# example >> note del 16
# =========================================================
@input_error
def note_del(*args):
    """note del <Num-record>

    example >> note del 16"""
    key = note_key(args[0])
    rec: NoteRecord = n_book.get(key)
    try:
        return n_book.del_record(rec)
    except KeyError:
        return f"Record {key} does not exist."


# =========================================================
# >> note change <Num>
# example >> note change 16
# =========================================================
@input_error
def note_change(*args):
    """note change <Num-record>

    example >> note change 16"""
    key = note_key(args[0])
    rec: NoteRecord = n_book.get(key)

    if rec:
        note = Note(input(" ".join(args[1:]) + ">>> "))
        tag = Tag(input("Enter tag >>> "))

        return rec.change_note(
            rec.note.value,
            note if note else rec.note.value,
            tag if tag else rec.tag.value,
        )
    else:
        return f"Record does not exist"


# =========================================================
# >> note find <fragment>
# Фрагмент має бути однією фразою без пробілів
# example >> note find word
# =========================================================
@input_error
def note_find(*args):
    return n_book.find_note(args[0])


# =========================================================
# >> note show <int: необов'язковий аргумент кількості рядків>
# Передається необов'язковий аргумент кількості рядків
# example >> note show /15
# =========================================================
@input_error
def note_show(*args):
    cli.display_notes(n_book)
    return ""


# =========================================================
# >> note sort
# Сортування нотаток по тегу
# example >> note sort
# =========================================================
@input_error
def note_sort(args):
    cli.sort_notes(args, n_book)
    return ""


# =========================================================
# Функція читає базу даних з файлу - ОК
# =========================================================
@input_error
def load_noteDB(path):
    return n_book.load_data(path)


# =========================================================
# Функція читає базу даних з файлу - ОК
# =========================================================
@input_error
def save_noteDB(path):
    return n_book.save_data(path)
