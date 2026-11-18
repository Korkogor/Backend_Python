contacts = []
N = 6
Z = 3


x = {}
while True:
    cmd = input("Enter command: quit, add, contacts, find or filter ").strip().lower()
    if cmd == "quit":
        break

    elif cmd == "add":
        name = input("Enter your name: ").strip()
        if not 2 <= len(name) <= 30:
            print("Name from 2 to 30 symbols")
            continue

        phone = input("Enter your phone number: ").strip()
        ok = phone.startswith("+7") and len(phone) == 12
        # string[1:]
        for ch in phone[2:]:
            if ch not in "0123456789":  # есть ещё isdigit
                ok = False
                break
        if not ok:
            print("Phone number is not valid, format +7XXXXXXXXXX")
            continue
        contacts.append([name, phone])
        print(f"Имя {name} добавлено в записную книжку")

    elif cmd == "contacts":
        print("Всего контактов:\n", len(contacts))
        for i, contact in enumerate(contacts, 1):
            start = contact[1][:N]
            end = contact[1][-Z:]
            stealth = len(contact[1][N:-Z]) * "*"
            masked_phone = start + stealth + end
            print(f"{i}. {contact[0]} - {masked_phone}")

    elif cmd == "find":
        query = input("Enter word: ").strip().lower()
        is_any_founded = False
        for name, phone in contacts:
            if query in name.lower() or query in phone:
                start = phone[:N]
                end = phone[-Z:]
                stealth = len(phone[N:-Z]) * "*"
                masked_phone = start + stealth + end
                print(name, "-", masked_phone)
                is_any_founded = True
        if not is_any_founded:
            print("Nothing found, try again.")

    elif cmd == "filter":
        print("Filters:: 1 - first letter")
        kind = input("Filter: ").strip()
        if kind == "1":
            letter = input("Enter your letter: ").strip().upper()[:1]
            count = 0
            for name, phone in contacts:
                if name[:1] == letter:
                    start = phone[:N]
                    end = phone[-Z:]
                    stealth = len(phone[N:-Z]) * "*"
                    masked_phone = start + stealth + end
                    print(name, "-", masked_phone)
                    count += 1
            print("Find:", count)
        else:
            print("Nothing found, try again.")

    else:
        print("Invalid command. Try again.")
