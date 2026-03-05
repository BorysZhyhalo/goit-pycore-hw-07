def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return "Enter user name and phone please."
        except KeyError:
            return "Contact not found."
    return inner