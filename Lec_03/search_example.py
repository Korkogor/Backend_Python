from logging import addLevelName

book = {'Иван': {'email': 'test@mtuci.ru', 'phone': '7900'},
        'Oleg': {'email': 'test1@mtuci.ru', 'phone': '7800'},
        'Pavel': {'phone': '7800'}}
groups = {"friends": set(), "work": {'Иван', 'Oleg', 'Pavel'}, "family": set()}

domen = input("Enter domen: ").strip().lower()
names = [k for k, v in book.items() if v.get('email', '@').split('@')[1] == domen]
print(names)

g = input("Enter Group: ").strip().lower()
count = sum(1 for n in groups.get(g, set()) if book[n].get('email'))
print(count)

if any((not book[c].get('email') for c in group) for group in groups.values()):
    print("We have contacts without email")