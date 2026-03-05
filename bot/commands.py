from typing import List, Dict
from bot.errors import input_error

@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    name, phone = args
    contacts[name]
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    name = args[0]
    return contacts[name]

@input_error
def show_all(args: List[str], contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


