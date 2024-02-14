class Library:
    def __init__(self, book_name=None, author=None, release_date=None, number_of_pages=None):
        self.book_name = book_name
        self.author = author
        self.release_date = release_date
        self.number_of_pages = number_of_pages
    
    def list_book(self):
        with open(r"LibraryManagementSystem\books.txt", "r") as file:
            lines=file.read().splitlines()
        print(lines)

    def add_book(self):
        book_name = input("Enter book name:")
        author = input("Enter author name:")
        release_date = input("Enter release date:")
        number_of_pages = input("Enter number of pages:")

        with open(r"C:LibraryManagementSystem\books.txt", "a+") as file:
            file.write(book_name + ", " + author + ", " + release_date + ", " + number_of_pages + "\n")

    def remove_book(self):
        removing_book = input("Enter a book name that you want to delete:")

        with open(r"C:LibraryManagementSystem\books.txt", "r") as i_file:
            with open(r"C:LibraryManagementSystem\books_temp.txt", "w") as o_file:
                for line in i_file:
                    if removing_book not in line:
                        o_file.write(line)

        import os
        os.remove(r"C:LibraryManagementSystem\books.txt")
        os.rename(r"C:LibraryManagementSystem\books_temp.txt", r"C:LibraryManagementSystem\books.txt")

lib = Library()

print("""
*** MENU***
1) List Books
2) Add Book
3) Remove Book
""")

user = int(input("Select the action you want to take:"))

if user == 1:
    lib.list_book()
elif user == 2:
    lib.add_book()
elif user == 3:
    lib.remove_book()
else:
    print("Please enter valid number!")