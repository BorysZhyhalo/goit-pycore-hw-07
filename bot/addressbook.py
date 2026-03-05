from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        value = str(value).strip()
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class Phone(Field):
    @Field.value.setter
    def value(self, new_value):
        new_value = str(new_value)
        if not new_value.isdigit():
            raise ValueError("Phone must contain only digits")
        if len(new_value) != 10:
            raise ValueError("Phone must be 10 digits")
        self._value = new_value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, value):
        phone = Phone(value)
        self.phones.append(phone)

    def find_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                return item

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if found_phone is not None:
            self.phones.remove(found_phone)

    def edit_phone(self, old_phone, new_phone):
        found_phone = self.find_phone(old_phone)
        if found_phone:
            found_phone.value = new_phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)