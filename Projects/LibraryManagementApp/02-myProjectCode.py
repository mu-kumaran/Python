# Library management app

class Library:
    def __init__(self,bookslist):
        self.bookslist = bookslist
        self.booksBorrowed = {}
    
    def displayBooks(self):
        print("Books in the library:")
        for i in self.bookslist:
            print(i)

    def displayBooksBorrowed(self):
        print("Books Borrowed from library:")
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

if __name__ == "__main__":
    booksDBase = input("Enter the books database filename: ")
    booksDB = open(booksDBase,'r')
    books = booksDB.read()
    bookslist = books.split("\n")

    lib = Library(bookslist)
    lib.displayBooks()
    # lib.addBooks()
    # lib.displayBooks()
    # lib.removeBooks()
    # lib.displayBooks()
    # lib.displayBooksBorrowed()
    lib.lendBooks()
    lib.displayBooksBorrowed()
    lib.returnBooks()
    lib.displayBooksBorrowed()
    pass

