
from record_classes import AddressBook, Record, Name, Phone, Email, Birthday, Address, book
from decorator import input_error
# from rich import box
# from rich.table import Table
# from rich.console import Console
import re
from record_classes import PhoneException, BirthdayException, EmailException
from cl_interface import ConsoleInterface

cli = ConsoleInterface()
#=========================================================
# >> add ...  DONE
# По этой команде бот сохраняет в памяти (в словаре например) новый контакт. 
# Вместо ... пользователь вводит ИМЯ и НОМЕР телефона, обязательно через пробел.
# example >> add Mike 02.10.1990 +380504995876
#=========================================================
@input_error
def func_add_rec(*args):    
    if not args[0].capitalize() in book.keys():
        name = Name(args[0].capitalize())
        phone = Phone(args[1] if len(args) >= 2 else "None")
        email = Email(args[2] if len(args) >= 3 else "None")
        birthday = Birthday(args[3] if len(args) >= 4 else "None")
        address = Address(' '.join(args[4:]) if len(args) >= 5 else "None")
        rec = Record(name, phone, email, birthday, address) 
        return book.add_record(rec)
    else: return "The person is already in database"


#=========================================================
# >> add phone    Done
# функція розширює новим телефоном існуючий запис особи Mike   
# >> add phone Mike +380509998877
#=========================================================
@input_error
def add_phone(*args):        
    if args and (len(args) >= 2):
        if args[0].capitalize() in book.keys():
            rec = book[args[0].capitalize()]
            if book[args[0].capitalize()].phones[0].value == "None": 
                book[args[0].capitalize()].phones.clear()
            return rec.add_phone(Phone(args[2]))
        else: return f"The person [bold red]{args[0].capitalize()}[/bold red] isn't in a database"
    else: return f"Expected 2 arguments, but {len(args)} was given.\nHer's an example >> add phone Mike +380509998877"


#=========================================================
# >> add ...  DONE
# По этой команде бот сохраняет в памяти контакта Email. 
# Вместо ... пользователь вводит ИМЯ и Email, обязательно через пробел.
# example >> add email Mike mike.djonsen@gmail.com
#=========================================================
@input_error 
def add_email(*args) -> str:    
    rec = book[args[0].capitalize()]
    email = Email(args[1])
    rec.add_email(email)
    return f'The contact "{args[0].capitalize()}" was updated with new email: {rec.email}'


#=========================================================
# >> add ...  DONE
# По этой команде бот сохраняет в памяти контакта Address. 
# Вместо ... пользователь вводит ИМЯ и address, адресу можна вводити як завгодно.
# example >> add address Mike Stepan Banderi Avenue, 11A
#=========================================================
@input_error 
def add_address(*args) -> str:    
    rec = book[args[0].capitalize()]
    rec.add_address(args[1:])
    return f'The contact "{args[0].capitalize()}" was updated with new address: {rec.address}'


#=========================================================
# >> add ...  DONE
# По этой команде бот сохраняет в памяти контакта birthday. 
# Вместо ... пользователь вводит ИМЯ и birthday, обязательно через пробел.
# example >> add birthday 31.12.2000
#=========================================================
@input_error
def add_birthday(*args) -> str:    
    rec = book[args[0].capitalize()]
    rec.add_to_birthday(Birthday(args[1])) 
    return f"Date of birth {args[0].capitalize()}, recorded"


#=========================================================
# >> show all         Done
# По этой команде бот выводит все сохраненные контакты 
# с номерами телефонов в консоль. 
#=========================================================
@input_error
def func_show_all(_)->str:
    cli.display_contacts(book)
    return ""
        

#=========================================================
# >> show book /N
# Команда "show book" друкує книгу контактів по N записів
# де N - це кількість записів на одній сторінці
#=========================================================
@input_error
def func_book_pages(*args):
    # Итерируемся по адресной книге и выводим представление для каждой записи
    n = int(re.sub("\D", "", args[0]))
    n_page = 0
    for batch in book._record_generator(N=n):
        n_page += 1
        print(f"{'='*14} Page # [bold red]{n_page}[/bold red] {'='*16}")
        for record in batch:
            print("\n".join([f"{record.name.value}|{record.birthday.value}|{', '.join(map(lambda phone: phone.value, record.phones))}"]))
        print("="*40)    
        print("Press [bold red]Enter [/bold red]", end="")
        input("to continue next page...")
    return f"End of the book" 


#=========================================================
# >> hello
# Отвечает в консоль "How can I help you?"
#=========================================================
@input_error
def func_greeting(_):
    return "How can I help you?"


#=========================================================
# >> phone ... Done
# По этой команде бот выводит в консоль номер телефона для указанного контакта.
# Вместо ... пользователь вводит Имя контакта, чей номер нужно показать.
# >> phone Ben
#=========================================================
@input_error
def func_phone(*args):    
    if args[0] == "": return f'Missed "Name" of the person'
    name = args[0].lower().capitalize()
    if name in book.keys():   
        if args: 
            res = ", ".join([phone.value for phone in book[name].phones]) 
            return f"Person {name} doesn't have phone" if res == "None" else res
        else: return f"Expected 1 argument, but 0 was given.\nHer's an example >> phone Name"
    else:
        return f"The {name} isn't in the database"  


#=========================================================
# >> birthday    Done
# функція повертає кількість днів до Дня Народження особи    
# Example >> birthday Mike
# Example >> birthday /365
#=========================================================
@input_error
def func_get_day_birthday(*args):
    # порахуємо кількість параметрів
    count_prm = get_count_prm(*args)    
    if args[0] == "": return f'Missed [bold red]Name[/bold red] of the person'
        
    if args and (count_prm >= 1):
        if "/" in args[0]:   # Example >> birthday /365
            count_day = int(re.sub("\/", "",args[0]))
            if not count_day > 0: return f"Enter the number of days greater than zero"
            return book.get_list_birthday(count_day)
            
        else: # Example >> birthday Mike
            name = args[0].lower().capitalize()
            if name in book.keys():
                if book[name].birthday.value == "None": return f"No [bold red]Birthday[/bold red] for {name}"
                return book[name].days_to_birthday() 
            else: return f"The [bold red]{name}[/bold red] isn't in a database"
    else: return f"Expected 1 arguments, but {count_prm} was given.\nHer's an example >> birthday Mike"

# ======================================================================================================
# =========================================[ remove ]===================================================
# ======================================================================================================

@input_error
def delete(*args):    
    rec = book[args[1].capitalize()]
    if args[0].lower() == "name":
        if book[args[1].capitalize()].name.value == args[1].capitalize():
            del book[args[1].capitalize()]
            return f"{args[1].capitalize()} is deleted from the contact book"
        
    elif args[0].lower() == "phone":
        num = rec.remove_phone(Phone(args[2]))
        if num == "This contact has no phone numbers saved": 
            return num
        return f"Phone number {args[1].capitalize()} : {num} - Deleted"

    elif args[0].lower() == "email":
        rec.remove_email()
        return f"{args[1].capitalize()}'s email has been removed from the contact list"

    elif args[0].lower() == "birthday":
        rec.remove_birthday()
        return f"{args[1].capitalize()}'s birthday has been removed from the contact list"

    elif args[0].lower() == "address":
        rec.remove_address()
        return f'address removed from {args[1].capitalize()}\'s profile'
    else:
        return "якийсь Error remove"
    
# ======================================================================================================
# =========================================[ change ]===================================================
# ======================================================================================================

@input_error
def change(*args):    
    if args[1].capitalize() in book.keys():
        rec = book[args[1].capitalize()]
        if args[0].lower() == "name":
            if not args[2].capitalize() is book.data.keys():
                rec = book[args[1].capitalize()]
                rec.change_name(Name(args[1].capitalize()), Name(args[2].capitalize()))
                book.data.pop(args[1].capitalize())
                book[args[2].capitalize()] = rec
                return f"Contact name {args[1].capitalize()}`s changed to {args[2].capitalize()}'s"
            else: 
                return f"Contact with the name {args[2].capitalize()}'s already exists"

        elif args[0].lower() == "phone":
            if len(args) >= 4 and rec: 
                rec.change_phone(Phone(args[2]), Phone(args[3]))
                return ""
            else:                                                 
                raise PhoneException(f"Check parameters for command >> change pnone")
                #return f"Contact wit name {args[1].capitalize()} doesn`t exist."
            

        elif args[0].lower() == "email":
            rec.change_email(Email(args[2]))
            return f"Email is profile {args[1].capitalize()}'s has been changed"

        elif args[0].lower() == "birthday":
            rec.change_birthday(Birthday(args[2]))
            return f"Birthday profile {args[1].capitalize()}'s has been changed"

        elif args[0].lower() == "address":
            rec.change_address(Address(args[2:]))
            return f'The contact "{args[1].capitalize()}" was updated with new address: {rec.address}'
        else:
            return "якийсь Error change"
    else: raise BirthdayException(f"Name {args[1].capitalize()} isn't in datebase")

#=========================================================
# >> search    Done
# функція виконує пошук інформації у довідковій книзі
#              example >> search Mike
#                      >> search 38073
#                      >> search none
#=========================================================
@input_error
def func_search(*args):
    count_prm = get_count_prm(args)   
    
    if args[0] == "": return f"[bold yellow]Enter search information[/bold yellow]"
    lst_result = []
    rec_str = ""
    if args and (count_prm >= 1):
        for rec in book.values():
            rec_str = str(rec)
            if args[0].lower() in rec_str.lower():
                lst_result.append(rec_str)
                
        s = "\n".join([rec for rec in lst_result])
        if lst_result: 
            return f"[bold green]Search results:[/bold green]\n{s}"
        else: 
            return f"No matches found for {args[0]}"
    else: 
        return f"Expected 1 arguments, but {count_prm} was given.\nHer's an example >> search Mike"
    
    
# =========================================================
# >> sort    Done
# функція викликає модул cleanfolder виконує сортування файлів у вказаній папці
#              example >> sort Testfolder
#                      >> sort C://Testfolder/testfolder
#                      >> sort .Testfolder/testfolder
# =========================================================
@input_error
def func_sort(*args):
    if args[0] == "":
        return f"[bold yellow]Enter path[/bold yellow]"
    return sort_main(*args)
    
    
#=========================================================
# Функція читає базу даних з файлу - ОК
#========================================================= 
@input_error
def load_phoneDB(path):
    return book.load_database(path)


#=========================================================
# Функція виконує збереження бази даних у файл *.csv - OK
#========================================================= 
@input_error
def save_phoneDB(path):
    return book.save_database(path)


# Рахує та повертає кількість параметрів
def get_count_prm(*args: list):
    if len(args) > 0: 
        count_prm = args.count(" ", 0, -1) + 1
    else: count_prm = 0
    return count_prm
