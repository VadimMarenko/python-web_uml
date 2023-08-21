from user_interface import AbstractUserInterface
from record_classes import AddressBook, Record, Name, Phone, Email, Birthday, Address, book
from note_classes import NoteBook, n_book
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
            _ = [table.add_row(str(record.name.value), str(', '.join(map(lambda phone: phone.value, record.phones))), str(record.email.value), str(record.birthday.value if record.birthday else None), str(record.address.value)) for record in book.data.values()]
            console.print(table)

    
    def display_notes(self, n_book: NoteBook):
        return super().display_notes(n_book)
    

    def display_help(self, commands):
        return super().display_help(commands)


if __name__ == "__main__":
    ci = ConsoleInterface()
    print(ci.display_contacts(book))
