from note_classes import NoteRecord, Note, Tag, n_book
from decorator import input_error
from datetime import datetime
from rich import box
from rich.table import Table
from rich.console import Console

@input_error
def func_exit(*args):
    #save_noteDB(path_note)
    return "Good bye!"   


#=========================================================
# Блок функцій для роботи з нотатками
#=========================================================
# >> note add <текст нотатки будь-якої довжини> <teg-ключове слово> 
# example >> note add My first note in this bot. Note
#=========================================================
@input_error
def note_add(*args):    
    key = str(datetime.now().replace(microsecond=0).timestamp())
    note = Note(" ".join(args[:]))
    arg_tag = input("Tag input >>> ")
    tag = Tag(arg_tag) 
    record = NoteRecord(key, note if note else "", tag if note else "")
    return n_book.add_record(record)


#=========================================================
# >> note del <key-ідентифікатор запису>
# example >> note del 1691245959.0
#=========================================================
@input_error
def note_del(*args):
    key = args[0]
    rec : NoteRecord = n_book.get(key)
    try:
        return n_book.del_record(rec)
    except KeyError:
        return f"Record {key} does not exist."
            

#=========================================================
# >> note change <key-record> <New notes> <tag>
# example >> note change 1691245959.0 My new notes. Tag 
#=========================================================
@input_error
def note_change(*args):
    key = args[0]
    note = Note(" ".join(args[1:]))
    tag = Tag(input("Enter tag >>> "))
    rec : NoteRecord = n_book.get(key)
    if rec:
        return rec.change_note(rec.note.value, note if note else rec.note.value, tag if tag else rec.tag.value)
    else:
        return f"Record does not exist"
    

#=========================================================
# >> note find <fragment>
# Фрагмент має бути однією фразою без пробілів
# example >> note find word
#=========================================================
@input_error
def note_find(*args):
    return n_book.find_note(args[0])


#=========================================================
# >> note show <int: необов'язковий аргумент кількості рядків>
# Передається необов'язковий аргумент кількості рядків 
# example >> note show /15
#=========================================================
@input_error
def note_show(*args):
    if len(n_book.data) == 0: return f"The database is empty"
    if args[0].startswith("/") and args[0][1:].isdigit():
        args = int(args[0][1:])
    else:
        args = 5    
    for page, rec in enumerate(n_book.iterator(args), 1):
        print(f"Page {page}\n")
   
    table = Table(box=box.DOUBLE)
    table.add_column("Num", justify="center", style="green", no_wrap=True)
    table.add_column("Key", justify="center", style="green", no_wrap=True)
    table.add_column("Note", justify="center", style="yellow", no_wrap=True)
    table.add_column("Tag", justify="center", style="red", no_wrap=True)
    table.add_column("Date", justify="center", style="blue", no_wrap=True)

    console = Console()
    _ = [table.add_row(str(i), str(item.key), str(item.note), str(item.tag), str(datetime.fromtimestamp(float(item.key)))) for i, item in enumerate(rec, 1)]
    console.print(table)
    return ""
  

#=========================================================
# >> note sort
# Сортування нотаток по тегу
# example >> note sort
#=========================================================
@input_error
def note_sort(args):    
    result = []
    for rec in n_book.values():
        line = f"{rec.tag}  {rec.note}  {rec.key}"
        result.append(line)
    result.sort()
    count = 0
    
    table = Table(box=box.DOUBLE)
    table.add_column("Num", justify="center", style="green", no_wrap=True)
    table.add_column("Tag / Note", justify="left", style="green", no_wrap=True)
    table.add_column("Key", justify="center", style="green", no_wrap=True)
    table.add_column("Date", justify="center", style="blue", no_wrap=True)

    console = Console()
    _ = [table.add_row(str(i), str(item[:item.rfind(" ")]), str(item[item.rfind(" "):]), str(datetime.fromtimestamp(float(item[item.rfind(" "):])))) for i, item in enumerate(result, 1)]
    console.print(table)    
    return ""

#=========================================================
# Функція читає базу даних з файлу - ОК
#========================================================= 
@input_error
def load_noteDB(path):
    return n_book.load_data(path)


#=========================================================
# Функція читає базу даних з файлу - ОК
#========================================================= 
@input_error
def save_noteDB(path):
    return n_book.save_data(path)