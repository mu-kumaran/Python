# Library Management Application

# Library class and its method begins
class Library:
    def __init__(self,booksList,name): #Here name is the library name
        self.booksList = booksList
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f'We have the following books in our library {self.name}:')
        for book in self.booksList:
            print(book)
        print(self.booksList)

    def addBook(self,book):
        if book in self.booksList:
            print("Book already exists")
        else:
            self.booksList.append(book)
            bookDatabase = open(databaseName,'a')
            bookDatabase.write('\n') # Get to the newline in the text file
            bookDatabase.write(book)
            print('Book added')

    def lendBook(self,book,user):
        if book in self.booksList:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print(f"Book `{book}` has been lended. Database updated")
            else:
                print(f"Book is already being used by {self.lendDict[book]}")
        else:
            print(f"Apologies! We don't have this book `{book}`in our library")

    def returnBook(self,book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print(f"Book `{book}` returned successfully")
        else:
            print(f'The book `{book}` does not exist in the Book Lending Database')
            print("You have not lended such book")

# Main function - Accepting the user input - Begins        
def main():
    while(True):
        print(f"Welcome to the {library.name} library. Following are the options,")
        choice = """
        1.Display Books
        2.Lend a Book
        3.Add a book
        4.Return a book 
        """
        print(choice)

        userInput = input("Press 'Q' to quit or 'C' to continue: ")
        if userInput == 'C':
            userChoice = int(input('Select an option to continue: '))
            if userChoice == 1:
                library.displayBooks()
            elif userChoice == 2:
                book = input("Enter the name of the book you want to lend: ")
                user = input("Enter the name of the user: ")
                library.lendBook(book,user)
            elif userChoice == 3:
                book = input("Enter the book name to add: ")
                library.addBook(book)
            elif userChoice == 4:
                book = input("Enter the book name to return: ")
                library.returnBook(book)
            else:
                print("Please choose a valid option")
        elif userInput == 'Q':
            break

        else:
            print("Please enter a valid option")
# Main function ends

# Program execution will begin from here using the __name__ condition
if __name__ == '__main__':
    
    databaseName = input("Enter the name of the database file with extension:")
    bookDBopen = open(databaseName,'r')
    bookDatabase = bookDBopen.read()
    booksList = bookDatabase.split("\n")
    library = Library(booksList,'PythonX')
    main() # Jump to main function to accept user input