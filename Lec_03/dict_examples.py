book = {}
groups = {"friends": set(), "work": set(), "family": set()}

while True:
    command_or_name = input("Enter 'stop', 'groups', 'add to group' or Name: ").strip()
    if command_or_name == "stop":
        break
    if command_or_name == "groups":
        g = input("Enter group name: ").strip().lower()
        names = groups.get(g, None)
        if names in None:
            print("Group", g, "not found")
            continue
        for name in names:
            print(name, " - " ,book[name]['phone'])
        continue

    if command_or_name == "add to group":
        name = input("Enter name: ").strip()
        contact = book.get(name)
        if contact:
            for g in input("Groups: ").split(", "):
                g = g.strip().lower()
                if g in groups:
                    groups[g].add(name)
                else:
                    print("Group", name, "not found")
        else:
            print("Contact not found")
        continue
    phone = input("Enter phone number: ").strip().lower()
    email = input("Enter email address: ").strip().lower()
    book[command_or_name] = {"phone": phone, "email": email}