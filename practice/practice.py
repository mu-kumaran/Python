
with open("practice.txt",'r+') as file1:
    file1.seek(0,0)
    print("File cursor position:",file1.tell())
    file1.write("Line 1"+"\n")
    file1.write("Line 2"+"\n")
    file1.write("Line 3"+"\n")
    file1.write("Line 4"+"\n")
    file1.write("Finished")
    file1.truncate()
    file1.seek(0,0)
    print(file1.read())




