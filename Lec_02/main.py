'''
phone = input("Enter your phone number: ").strip()
#ok = phone.startswith("+7") # проверяет, чтобы строка начиналась с +7

ok = phone.startswith("+7") and len(phone) == 12

# string[1:]
for ch in phone[2:]:
    if ch not in "0123456789":
        ok = False
        break
if ok:
    print("Phone number is valid")
else:
    print("Phone number is not valid, format +7XXXXXXXXXX")

'''
# ЦИКЛ while

count = 0
book = ""
while True:
    name = input("Enter your name or \"stop\" for end the cycle: ").strip()
    if name.lower() == "stop":
        break

    if not 2 <= len(name) <= 30:
        print("Name from 2 to 30 symbols")
        continue

    phone = input("Enter your phone number: ").strip()
    ok = phone.startswith("+7") and len(phone) == 12
    # string[1:]
    for ch in phone[2:]:
        if ch not in "0123456789": #есть ещё isdigit
            ok = False
            break
    if not ok:
        print("Phone number is not valid, format +7XXXXXXXXXX")
        continue

    count += 1
    book += f"{count}. {name} - {phone}\n"
    # f - форматированная строка
    print(f"Имя {name} добавлено в записную книжку")
print("Всего контактов:", book)
