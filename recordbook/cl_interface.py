from user_interface import AbstractUserInterface
from record_classes import AddressBook, Record, Name, Phone, Email, Birthday, Address, book
from note_classes import NoteBook, n_book
from datetime import datetime
from rich import box
from rich.table import Table
from rich.console import Console

class ConsoleInterface(AbstractUserInterface):
    def display_contacts(self, book: AddressBook):
        if len(book.data) == 0: 
            return "The database is empty"
        else: 
            table = Table(box=box.DOUBLE)
            table.add_column("Name", justify="center", style="cyan", no_wrap=True)
            table.add_column("Phone number", justify="center", style="green", no_wrap=True)
            table.add_column("Email", justify="center", style="red", no_wrap=True)
            table.add_column("Birthday", justify="center", style="yellow", no_wrap=True)
            table.add_column("Address", justify="center", style="red", no_wrap=True)

            console = Console()
            _ = [table.add_row(str(record.name), str(', '.join(map(lambda phone: phone.value, record.phones))), str(record.email.value), str(record.birthday.value), str(record.address.value)) for record in book.data.values()]
            console.print(table)

    
    def display_notes(self, n_book: NoteBook):
        if len(n_book.data) == 0: 
            return f"The database is empty"
        # if args[0].startswith("/") and args[0][1:].isdigit():
        #     args = int(args[0][1:])
        # else:
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
        
    
    def sort_notes(self, arg, n_book: NoteBook):
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


    def display_help(self, commands):
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
        
        if commands == "contact":
            return contact
        if commands == "note":
            return note
        if commands == "sort":
            return sort
        if commands == "all":
            return help_navigation + contact + note + sort

        return help_navigation



if __name__ == "__main__":
    ci = ConsoleInterface()
    print(ci.display_contacts(book))
