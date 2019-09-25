text = input('Text: ')
letter = input('Letter: ')

letters = [l for l in text]
myList = []
for count, item in enumerate(letters):
    if item == letter:
        myList.append(count)

print(myList)
