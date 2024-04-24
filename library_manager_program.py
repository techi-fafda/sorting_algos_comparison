class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def update_book(self, title, new_author):
        book = self.find_book(title)
        if book:
            book.author = new_author
            print(f"Book '{title}' author updated to '{new_author}'.")
        else:
            print(f"Book '{title}' not found.")

    def delete_book(self, title):
        book = self.find_book(title)
        if book:
            self.books.remove(book)
            print(f"Book '{title}' deleted.")
        else:
            print(f"Book '{title}' not found.")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book = Book(title, author)
            library.add_book(book)
            print("Book added successfully.")
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            title = input("Enter book title to update: ")
            new_author = input("Enter new author name: ")
            library.update_book(title, new_author)
        elif choice == '4':
            title = input("Enter book title to delete: ")
            library.delete_book(title)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
