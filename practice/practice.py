with open('practice.txt','r+') as file:
    # readFile = file.readlines()
    rdFile = file.read()
    
# print(readFile)
print(rdFile.split("\n"))