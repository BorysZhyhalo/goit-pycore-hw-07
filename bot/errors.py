'''
Decorator to convert common input/runtime errors into user-friendly messages.
'''
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except IndexError:
            return "Not enough arguments."

        except ValueError as e:
            # показуємо конкретну причину (телефон/дата/ім'я)
            return str(e) if str(e) else "Invalid value."

        except KeyError:
            return "Contact not found."

    return inner