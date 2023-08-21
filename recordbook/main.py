import os
import platform 
from record_book import func_add_rec, func_show_all, func_book_pages, add_phone, add_email, add_address, add_birthday, \
    func_greeting, func_phone, save_phoneDB, load_phoneDB, func_get_day_birthday, delete, change, func_search, func_sort

from note_book import note_add, note_change, note_del, note_find, note_show, note_sort, func_exit, load_noteDB, save_noteDB

from clean import sort_main
from rich import print

path_book = "data_12.bin"
path_note = "n_book.json"

  
def func_help(*args):
    help_navigation = """[bold red]help all[/bold red] - виводить всю довідку на екран
[bold red]help contact[/bold red] - довідка по командам адресної книги
[bold red]help note[/bold red] - довідка по командам нотаток
[bold red]help sort[/bold red] - довідка по командам сортувальника
[bold red]hello[/bold red] - вітання
[bold red]good bye, close, exit[/bold red] - завершення програми
[bold red]load[/bold red] - завантаження інформації про користувачів із файлу
[bold red]save[/bold red] - збереження інформації про користувачів у файл
[bold red]cls[/bold red] - очищення екрану від інформації"""
    contact = """[bold red]show all[/bold red] - друкування всієї наявної інформації про користувачів
[bold red]show book /N[/bold red]  - друкування інформації посторінково, де [bold red]N[/bold red] - кількість записів на 1 сторінку
[bold red]add[/bold red] - додавання користувача до бази даних. 
      example >> [bold blue]add Mike[/bold blue]
              >> [bold blue]add Mike <phone> <email> <birthday> <address>[/bold blue]
              >> [bold blue]add Mike 380504995876 mike@mail.com 12.12.1970 Poltava,Soborna.str,1[/bold blue]              
[bold red]phone[/bold red] - повертає перелік телефонів для особи
      example >> [bold blue]phone Mike[/bold blue]
[bold red]add phone[/bold red] - додавання телефону для користувача
      example >> [bold blue]add phone Mike +380504995876[/bold blue]
[bold red]change phone[/bold red] - зміна номеру телефону для користувача
      Формат запису телефону: [bold green]+38ХХХ ХХХ ХХ ХХ[/bold green]
      example >> [bold blue]change phone Mike +380504995876 +380665554433[/bold blue]
[bold red]del phone[/bold red] - видаляє телефон для особи. 
      example >> [bold blue]del phone Mike +380509998877[/bold blue]
[bold red]birthday[/bold red] - повертає кількість днів до Дня народження, або список людей, чей день народження очікується.
      example >> [bold blue]birthday Mike[/bold blue]
      example >> [bold blue]birthday /<число днів>[/bold blue]
[bold red]change birthday[/bold red] - змінює/додає Дату народження для особи
      example >> [bold blue]change birthday Mike 02.03.1990[/bold blue]
[bold red]search[/bold red] - виконує пошук інформації по довідковій книзі
      example >> [bold blue]search Mike[/bold blue]"""
    note = """[bold red]note add[/bold red] - додає нотатку з тегом у записник нотаток
      example >> [bold blue]note add My first note #Tag[/bold blue]
[bold red]note del[/bold red] - видаляє нотатку за ключем із записника нотаток
      example >> [bold blue]note del 1691245959.0[/bold blue]
[bold red]note change[/bold red] - змінює нотатку з тегом за ключем у записнику нотаток
      example >> [bold blue]note change 1691245959.0 My first note #Tag[/bold blue]
[bold red]note find[/bold red] - здійснює пошук за фрагментом у записнику нотаток
      example >> [bold blue]note find <fragment>[/bold blue]
[bold red]note show[/bold red] - здійснює посторінковий вивід всіх нотаток
      example >> [bold blue]note show /10[/bold blue]
[bold red]note sort[/bold red] - здійснює сортування записів нотаток за тегами
      example >> [bold blue]note sort /10[/bold blue]"""
    sort = """[bold red]sort dir[/bold red] - виконує сортування файлів в указаній папці
      example >> [bold blue]sort dir <Path_to_folder>[/bold blue]"""
    
    if args[0] == "contact":
        return contact
    if args[0] == "note":
        return note
    if args[0] == "sort":
        return sort
    if args[0] == "all":
        return help_navigation + contact + note + sort

    return help_navigation

#=========================================================
# >> "good bye", "close", "exit"
# По любой из этих команд бот завершает свою роботу 
# после того, как выведет в консоль "Good bye!".
#=========================================================

def clear_screen(_):
    os_name = platform.system().lower()
    
    if os_name == 'windows':
        os.system('cls')
    elif os_name == 'linux' or os_name == 'darwin':
        os.system('clear')
    return ""


def no_command(*args):
    return f"Unknown command. {help(all)}"


COMMANDS = {
    func_exit: ("close", "exit", "good bye"),
    func_greeting: ("hello",),
    func_add_rec: ("add",),
    func_phone: ("phone",),
    func_show_all: ("show all",),
    save_phoneDB: ("save",), 
    load_phoneDB: ("load",),
    clear_screen: ("cls"), 
    func_book_pages: ("show book",),
    func_get_day_birthday: ("birthday",),
    func_help: ("help",), 
    add_phone: ("add phone",),
    add_email: ("add email"),
    add_address: ("add address",),
    add_birthday: ("add birthday",),
    delete: ("del",),
    change: ("change",),
    func_search: ("search",),
    note_add: ("note add",),
    note_del: ("note del",),
    note_change: ("note change",),
    note_find: ("note find",),
    note_show: ("note show",),
    note_sort: ("note sort",),
    func_sort: ("sort dir",)
}



def parser(text: str):
    for key, value in COMMANDS.items():
        for val in value:
            if text.startswith(val):
                return key, text[len(val):].strip().split()
        
    return no_command, ""
            
            
def main():
    load_phoneDB(path_book)
    load_noteDB(path_note)
    while True:
        user_input = input(">>>").lower()
        command, data = parser(user_input)
        result = command(*data)
        print(result)

        save_phoneDB(path_book)
        save_noteDB(path_note)            
        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()
  

