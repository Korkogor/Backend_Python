import operator

counter = {}
sorted_words = []

text = input("Please enter a text: ").strip().lower()

for char in ",.!?-—«»":
    text = text.replace(char, " ")
words = text.split()
for word in words:
    counter[word] = counter.get(word, 0) + 1
print(f"Unique words: {len(counter)}")


sort = input("Sorting method: 1 - descending, 2 - ascending: ").strip().lower()

if sort == "1":
    print("descending")
    sorted_words = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
elif sort == "2":
    print("ascending")
    sorted_words = sorted(counter.items(), key=operator.itemgetter(1))
else:
    print("Not a sorting method")

for word, count in sorted_words[:5]:
    print(f"{word}: {count}")
