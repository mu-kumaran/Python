# Library management app

class Library:
    def __init__(self,bookslist):
        self.bookslist = bookslist
    
    def displayBooks(self):
        print("Books in the library:")
        for i in bookslist:
            print(i)

    def displayBooksBorrowed(self):
        pass

    def addBooks(self):
        book = input("Enter the book name to add in the library: ")
        bookslist.append(book)
        booksDB = open(booksDBase,'a')
        booksDB.write("\n")
        booksDB.write(book)
        print("Book added")
    
    def removeBooks(self):
        book = input("Enter the book name to remove in the library: ")
        if book in bookslist:
            bookslist.remove(book)
            booksDB = open(booksDBase,'w')
            length = len(bookslist)
            j=1
            for i in bookslist:
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
        pass

    def returnBooks(self):
        pass

if __name__ == "__main__":
    booksDBase = input("Enter the books database filename: ")
    booksDB = open(booksDBase,'r')
    books = booksDB.read()
    bookslist = books.split("\n")

    lib = Library(bookslist)
    lib.displayBooks()
    lib.addBooks()
    lib.displayBooks()
    # lib.removeBooks()
    # lib.displayBooks()
    pass

