squares = ['red','blue','green','yellow','white']

for (index,value) in enumerate(squares):
    print(index,value)


def names(*args):
    for i in args:
        print(i)
    print(args)
    print(type(args))
    return args
name = names("xyz","abc","123")
print(name)

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

print(myList)