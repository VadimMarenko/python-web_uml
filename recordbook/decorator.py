from record_classes import PhoneException, BirthdayException, EmailException



# Декоратор для Обробки командної строки
def input_error(func):
    def inner(*args):
        try:
            result = func(*args) 
            # if not result == "Good bye!": 
            #     return result
            # else: 
            
        
        # Обробка виключних ситуацій
        except BirthdayException as e:
            result = e
        except PhoneException as e:
            result = e
        except EmailException as e:
            result = e
        except FileNotFoundError:    # Файл бази даних Відсутній
            result = "The database is not found"
        except ValueError:
            result = "Incorect data or unsupported format while writing to the file"
        except KeyError:
            result = "Record is not in the database"
        except TypeError:
            result = "Incorect data"
        except IndexError:           
            if "note_show" in str(func):
                result = "Enter the number of lines per page"
        return result   
    return inner
