# Write a program that remove all vowels from the input word and generate a brief version of it.

vowels = ['a', 'e', 'i', 'o', 'u']

data = input("Enter some data: ")

myList = [c for c in data if c not in vowels]

print(''.join(myList))
