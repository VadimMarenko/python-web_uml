import os
import platform
from record_book import (
    func_add_rec,
    func_show_all,
    func_book_pages,
    add_phone,
    add_email,
    add_address,
    add_birthday,
    func_greeting,
    func_phone,
    save_phoneDB,
    load_phoneDB,
    func_get_day_birthday,
    delete,
    change,
    func_search,
    func_sort,
)

from note_book import (
    note_add,
    note_change,
    note_del,
    note_find,
    note_show,
    note_sort,
    func_exit,
    load_noteDB,
    save_noteDB,
)

from clean import sort_main
from rich import print

from cl_interface import ConsoleInterface

cli = ConsoleInterface()

path_book = "data_12.bin"
path_note = "n_book.json"


def func_help(*args):
    return cli.display_help(args[0])


# =========================================================
# >> "good bye", "close", "exit"
# По любой из этих команд бот завершает свою роботу
# после того, как выведет в консоль "Good bye!".
# =========================================================


def clear_screen(_):
    os_name = platform.system().lower()

    if os_name == "windows":
        os.system("cls")
    elif os_name == "linux" or os_name == "darwin":
        os.system("clear")
    return ""


def no_command(*args):
    return f"Unknown command. {help(all)}"


COMMANDS = {
    func_exit: ("close", "exit", "good bye"),
    func_greeting: ("hello",),
    func_phone: ("phone",),
    func_show_all: ("show all",),
    save_phoneDB: ("save",),
    load_phoneDB: ("load",),
    clear_screen: ("cls",),
    func_book_pages: ("show book",),
    func_get_day_birthday: ("birthday",),
    func_help: ("help",),
    add_phone: ("add phone",),
    add_email: ("add email",),
    add_address: ("add address",),
    add_birthday: ("add birthday",),
    func_add_rec: ("add",),
    delete: ("delete",),
    change: ("change",),
    func_search: ("search",),
    note_add: ("note add",),
    note_del: ("note del",),
    note_change: ("note change",),
    note_find: ("note find",),
    note_show: ("note show",),
    note_sort: ("note sort",),
    func_sort: ("sort dir",),
}


def parser(text: str):
    for key, value in COMMANDS.items():
        for val in value:
            if text.startswith(val):
                return key, text[len(val) :].strip().split()

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
