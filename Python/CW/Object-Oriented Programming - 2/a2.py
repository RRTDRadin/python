class Library:
    def __init__(self, list, name):
        self.bookList = list
        self.name = name
        self.lendDict = {}


    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)


    def lendBook(self, user, book):
        if book not in self.lendDict.key():
            self.lendDict.update({book:user})
            print("Lender book data base hase been updated You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def __init__(self, list, name):
        self.bookList.append(book)
        print("Book has been added to the book list.")

    def returnBook(self, Book):
        self.lendDict.pop(book)

if __name__=='__name__':
    
    book = Library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Let's Upskill")

    while(True):
        print(f"Welcome to the {book.name} Library. Enter your choice to continue.")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Books")
        print("4. Return a Books")
        if user_Choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option.")
            continue

        else:
            user_Choice = int(user_Choice)
        
        if user_Choice == 1:
            books.displayBooks()

        elif user_Choice ==2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name:")
            book.lendBook(user, book)

        elif user_Choice == 3:
            book = input("Enter the name of the book you want to add:")
            book.addBook(book)

        elif user_Choice == 4:
            book = input("Enter the name of the book you want to return:")
            book.addBook(book)

        print("Press q to quit ant c to continue.")
        user_Choice2 = ""
        while(user_Choice2!="c" and user_Choice2!="q"):
            user_Choice2 == "q":
            exit()

            user_Choice2 == "c":
            continue