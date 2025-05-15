# Library management app

class Library:
    def __init__(self,bookslist):
        self.bookslist = bookslist
        self.booksBorrowed = {}
    
    def displayBooks(self):
        print("Books in the library:")
        print("--------------------")
        for i in self.bookslist:
            print(i)

    def displayBooksBorrowed(self):
        print("Books Borrowed from library:")
        print("---------------------------")
        if(not self.booksBorrowed):
            print("No books have been borrowed yet")
        else:
            for (i,j) in self.booksBorrowed.items():
                print(i,": lended by ",j)

    def addBooks(self):
        book = input("Enter the book name to add in the library: ")
        self.bookslist.append(book)
        booksDB = open(booksDBase,'a')
        booksDB.write("\n")
        booksDB.write(book)
        print("Book added")
    
    def removeBooks(self):
        book = input("Enter the book name to remove in the library: ")
        if book in bookslist:
            self.bookslist.remove(book)
            booksDB = open(booksDBase,'w')
            length = len(self.bookslist)
            j=1
            for i in self.bookslist:
                if j == length:
                    booksDB.write(i)
                else:
                    booksDB.write(i)
                    booksDB.write("\n")
                    j += 1
            print("Book removed")
        else:
            print("No such book available in the library")

    def lendBooks(self):
        book = input("Enter the book name to lend from the library: ")
        if book not in self.bookslist:
            print("No such book available. Enter the correct book name")
        else:
            user = input("Enter the name of the user: ")

            if book in self.booksBorrowed.keys():
                print(f"Book already lended by {self.booksBorrowed.get(book)}")
            else:
                self.booksBorrowed.update({book:user})
                print("Book lended")

    def returnBooks(self):
        book = input("Enter the book name to return to the library: ")
        user = input("Enter the user who have lended the book:")
        if (book,user) in self.booksBorrowed.items():
            del self.booksBorrowed[book]
            print("Book returned")
        else:
            print("Book cannot be returned")

def main():
    print("Welcome to the Library: ")
    print("----------------------")
    while(True):
        print("""
                Options:
                -------- 
                1. Display books in the library
                2. Display books borrowed from library
                3. Add Books in the Library
                4. Remove Books in the Library
                5. Lend Book
                6. Return Book
                7. Exit
        """)
        try:
            option = int(input("Enter the option number:"))
            if(option == 1):
                lib.displayBooks()
            elif(option == 2):
                lib.displayBooksBorrowed()
            elif(option == 3):
                lib.addBooks()
            elif(option == 4):
                lib.removeBooks()
            elif(option == 5):
                lib.lendBooks()
            elif(option == 6):
                lib.returnBooks()
            elif(option == 7):
                break
            else:
                print("Wrong option. Try again")
        except Exception as err:
            print("Typo Error:",err)
            print("Enter correct option")
            


if __name__ == "__main__":
    while(True):
        booksDBase = input("Enter the books database filename: ")
        try:
            booksDB = open(booksDBase,'r')
            books = booksDB.read()      # returns a string datatype
            bookslist = books.split("\n")   # string datatype converted in to list
            lib = Library(bookslist)
            break
        except Exception as err:
            print("Error: ",err)
            print("Enter the correct filename")

    main()

