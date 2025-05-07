""" 
Task:
=====
Your local university's Raptors fan club maintains a register of its active members on a .txt document. Every month they update the file by removing the members who are not active. You have been tasked with automating this with your Python skills.
Given the file currentMem, Remove each member with a 'no' in their Active column. Keep track of each of the removed members and append them to the exMem file. Make sure that the format of the original files in preserved. (Hint: Do this by reading/writing whole lines and ensuring the header remains ). Write the test function for the program
"""
'''
The two arguments for the updateFile() function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
'''

from random import randint as rand

mem_status = ("Yes","No")
mem_format = "{:^13} {:<11} {:^10}"
header = mem_format.format("Membership no","Date Joined","Active?")+"\n"

# Generating member file using random function
def genFile(currentMem,exMem):
    
    with open(currentMem,"w+") as file1:
        file1.write(header)
        for i in range(20):
            date = str(rand(1,25))+"-"+str(rand(1,12))+"-"+str(rand(2020,2025))
            if i==19:
                file1.write(mem_format.format(rand(10000,99999),date,mem_status[rand(0,1)]))
            else:
                file1.write(mem_format.format(rand(10000,99999),date,mem_status[rand(0,1)])+"\n")

    with open(exMem,"w+") as file2:
        file2.write(header)
        for i in range(3):
            date = str(rand(1,25))+"-"+str(rand(1,12))+"-"+str(rand(2020,2025))
            if i==2:
                file2.write(mem_format.format(rand(10000,99999),date,mem_status[1]))
            else:
                file2.write(mem_format.format(rand(10000,99999),date,mem_status[1])+"\n")

# Updating current member file and ex-member file
def updateFile(currentMem,exMem):
    with open(currentMem,"r+") as file1:
        rdfile = file1.read().split("\n")
        rdfile.pop(0) # removing header content from the list
   
   # Updating ex-member file 
    writeFile = []
    for i in range(0,len(rdfile)):
            if "Yes" in rdfile[i]:
                continue
            else:
                writeFile.append(rdfile[i])

    with open(exMem,'a+') as file2:
        file2.write("\n")
        for i in range(0,len(writeFile)):
            if i==(len(writeFile)-1):
                file2.write(writeFile[i])
            else:
                file2.write(writeFile[i]+"\n")

    # Updating current member file
    writeFile.clear()
    for i in range(0,len(rdfile)):
            if "No" in rdfile[i]:
                continue
            else:
                writeFile.append(rdfile[i])

    with open(currentMem,"w+") as file3:
        file3.write(header)
        for i in range(0,len(writeFile)):
            if i==(len(writeFile)-1):
                file3.write(writeFile[i])
            else:
                file3.write(writeFile[i]+"\n")
    del writeFile

# test function for the program
def test(passed):
    print("Test Condition: \n")
    if passed:
        print("Test passed")
    else:
        print("Test failed")

def testCase(testCurrent,testEx):
    
    genFile(testCurrent,testEx)

    with open(testCurrent,'r') as file:
        t1_current = file.read().split("\n")

    with open(testEx,'r') as file:
        t1_ex = file.read().split("\n")

    try:
        passed = True
        updateFile(testCurrent,testEx)
        with open(testCurrent,'r') as file:
            t2_current = file.read().split("\n")
        with open(testEx,'r') as file:
            t2_ex = file.read().split("\n")

        # check conditions
        # checking whether no of rows equal
        if ((len(t1_current)+len(t1_ex)) != (len(t2_current)+len(t2_ex))):
            print("Total no of rows in current and ex members files do not match with original files.")
            passed = False

        # checking updated file with original file
        for line in t2_current:
            if "No" in line:
                print("Inactive members present in the updated current members file")
                passed = False
                
            if line not in t1_current:
                print("Data in updated current members file does not match with original file")
                passed = False

        test(passed)
    except:
        print("Error in programming")
        passed  = False
        test(passed)


if __name__ == "__main__":
    currentMem = "currentMem.txt"
    exMem = "exMem.txt"
    genFile(currentMem,exMem)
    updateFile(currentMem,exMem)

    print("Active members: \n\n")
    with open(currentMem,'r') as file1:
        print(file1.read())

    print("Inactive members: \n\n")
    with open(exMem,'r') as file2:
        print(file2.read())

    # Test case
    testCurrent = "testCurrent.txt"
    testEx = "testEx.txt"
    testCase(testCurrent,testEx)