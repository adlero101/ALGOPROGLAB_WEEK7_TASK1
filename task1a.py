class Member:
    def __init__(self, name, member_id):
        self.__name = name
        self.__member_id = member_id
        self.__borrowed_books = []  # private list

  
    def borrow_book(self, book_name):
        """Add a book to the borrowed list."""
        self.__borrowed_books.append(book_name)

    def return_book(self, book_name):
        """Remove a book from the borrowed list."""
        if book_name in self.__borrowed_books:
            self.__borrowed_books.remove(book_name)
        else:
            print(f"{book_name} not found in borrowed list")

    def show_info(self):
        """Display member info and borrowed books."""
        print(f"Member Name: {self.__name}")
        print(f"Member ID: {self.__member_id}")
        print("Borrowed Books:", ", ".join(self.__borrowed_books) if self.__borrowed_books else "None")

    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name.strip() != "":
            self.__name = new_name
        else:
            print("Don't you have a name?.")

    
    @property
    def borrowed_books(self):
        return self.__borrowed_books.copy()

Tesla = Member("Tesla", "19119199")
Tesla.borrow_book("Python for Dummies - 1st Edition")
Tesla.borrow_book("La Santa Biblia")
Tesla.show_info()
Tesla.return_book("The Brief History of Time")
Tesla.show_info()

print(Tesla.borrowed_books)
Tesla.name = ""
Tesla.name = "Nikola Tesla"
Tesla.show_info()

    





