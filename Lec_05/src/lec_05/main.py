from funk_test import (
    Book,
    Groups,
    add_contact,
    ask,
    find_contact,
    list_contacts,
    show_group,
)


def main() -> None:
    book: Book = {}
    groups: Groups = {"friends": set(), "work": set(), "family": set()}

    while True:
        cmd = ask("Command: ").lower()
        if cmd == "quit":
            break
        elif cmd == "add":
            add_contact(book, groups)
        elif cmd == "find":
            card = find_contact(book, ask("Name: "))
            print(card or "Not found")
        elif cmd == "groups":
            show_group(book, groups, ask("Group: "))
        elif cmd == "list":
            list_contacts(book)

main()

