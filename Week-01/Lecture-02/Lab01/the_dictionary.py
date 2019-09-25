myList = ['ahmed', 'fatma', 'ibrahim']

myDict = {}

for key, value in sorted(enumerate(myList)):
    value = value.split()
    myDict[myList[key][0]] = value

print(myDict)
