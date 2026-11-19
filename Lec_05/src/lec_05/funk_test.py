from collections.abc import Callable

Card = dict[str, str]
Book = dict[str, Card]
Groups = dict[str, set[str]]


def ask(prompt: str) -> str:
    return input(prompt).strip()


def add_contact(book: Book, groups: Groups) -> None:
    name = ask("Name: ")
    book[name] = {
        "phone": ask("Phone number: "),
        "email": ask("Email address: "),
    }
    for g in ask("groups: ").split(","):
        g = g.strip().lower()
        if g in groups:
            groups[g].add(name)
        else:
            print("Not a valid group", g)


def find_contact(book: Book, name: str) -> Card | None:
    return book.get(name)


def show_group(book: Book, groups: Groups, group: str) -> None:
    for n in groups.get(group, set()):
        if not book[n].get("phone"):
            continue
        print(n, "-", book[n]["phone"])


def list_contacts(book: Book) -> None:
    for name in sorted(book):
        print(name, "-", book[name]["phone"])


def count_if(book: Book, check: Callable[[Card], bool]) -> int:
    return sum(1 for c in book.values() if check(c))
