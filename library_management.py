import random

class Book:
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.is_available = True

  def check_out(self):
    if self.is_available:
      self.is_available = False

  def check_in(self):
    if not self.is_available:
      self.is_available = True

  def display_info(self):
    if self.is_available:
      print("-----------------------")
      book_info = f"Book name: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"
      print(book_info)
    else:
      print("Sorry! This book is currently unavailable.")

class Member:
  def __init__(self, name, member_id):
    self.name = name
    self.member_id = member_id
    self.borrowed_books = []

  def borrow_book(self, book_object):
    self.borrowed_books.append(book_object)

  def return_book(self, book_object):
    self.borrowed_books.remove(book_object)

  def display_borrowed_books(self):
    print("\nThe list of borrowed books:")
    print("---------------------------")

    if not self.borrowed_books:
        print("No books currently borrowed.")
        return

    for book_title in self.borrowed_books:
        print(f"- {book_title}")


class Library:
  def __init__(self):
    self.books = {}
    self.members = {}

  def add_book(self, book_object):
    self.books[book_object.isbn] = book_object
    print(f"Your book '{book_object.title}' has been added successfully!")

  def add_member(self, member_name):
    key = str(f"{member_name.split()[0].upper()}{random.randint(0,9999):04d}")
    self.members[key] = {
            "name": member_name,
            "borrowed_books": []
    }
    print(f"Hello {member_name}, your details have been recorded successfully!")
    print(f"Your Member ID is: {key}")

    return key

  def lend_book(self, member_id, book_isbn):
    member_data = self.members.get(member_id)
    if not member_data:
      print(f"Error: Member with ID '{member_id}' not found.")
      return

    book_object = self.books.get(book_isbn)

    if not book_object:
      print(f"Error: Book with ISBN '{book_isbn}' not found.")
      return

    if book_object.is_available:
      book_object.check_out()

      member_data["borrowed_books"].append(book_object.title)
      print(f"Success: '{book_object.title}' borrowed by {member_data['name']}.")
    else:
        print(f"Sorry, the book '{book_object.title}' is currently unavailable.")

  def receive_book(self, member_id, book_isbn):
    member_data = self.members.get(member_id)

    if not member_data:
      print(f"Error: Member with ID '{member_id}' not found.")
      return

    book_object = self.books.get(book_isbn)

    if not book_object:
      print(f"Error: Book with ISBN '{book_isbn}' not found.")
      return

    if book_object.title in member_data["borrowed_books"]:
      book_object.check_in()

      member_data["borrowed_books"].remove(book_object.title)
      print(f"Success: '{book_object.title}' returned by {member_data['name']}.")
    else:
      print(f"Error: '{member_data['name']}' did not borrow the book '{book_object.title}'.")


  def display_all_books(self):

    if not self.books:
        print("The library is currently empty.")
        return

    print("\n--- Unavailable Books ---")
    for book in self.books.values():
        if not book.is_available:
            print(f"Book title: '{book.title}'")
            print("-------------------------")

    print("\n--- Available Books ---")
    for book in self.books.values():
        if book.is_available:
            book.display_info()

    print("-----------------------------------")

  def display_all_members(self):
    print("\n--- All Library Members ---\n")
    if not self.members:
        print("There are no registered members yet.")
        return
    for member_id, member_data in self.members.items():
      print(f"Member Name: {member_data['name']}")
      print(f"Member ID: {member_id}")
      if member_data["borrowed_books"]:
            print("Borrowed books: ")
            for title in member_data["borrowed_books"]:
                print(f"  - {title}")
      print("-------------------------")

def main():
    my_library = Library()

    print("\n--- Library Management System ---")

    while True:
        print("\n--- Menu ---")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Display all books")
        print("6. Display all members")
        print("7. Show a member's borrowed books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            new_book = Book(title, author, isbn)
            my_library.add_book(new_book)


            prompt_return = input("\nPress Enter to return to the main menu or type 'exit' to quit: ")
            if prompt_return.lower() == 'exit':
                print("Happy Reading!")
                break

        elif choice == "2":
            member_name = input("Enter Member Name: ")
            my_library.add_member(member_name)

            prompt_return = input("\nPress Enter to return to the main menu or type 'exit' to quit: ")
            if prompt_return.lower() == 'exit':
                print("Happy Reading!")
                break

        elif choice == "3":
            member_id = input("Enter Member ID: ")
            book_isbn = input("Enter Book ISBN: ")
            my_library.lend_book(member_id, book_isbn)

            prompt_return = input("\nPress Enter to return to the main menu or type 'exit' to quit: ")
            if prompt_return.lower() == 'exit':
                print("Happy Reading!")
                break

        elif choice == "4":
            member_id = input("Enter Member ID: ")
            book_isbn = input("Enter Book ISBN: ")
            my_library.receive_book(member_id, book_isbn)

            prompt_return = input("\nPress Enter to return to the main menu or type 'exit' to quit: ")
            if prompt_return.lower() == 'exit':
                print("Happy Reading!")
                break

        elif choice == "5":
            my_library.display_all_books()

            prompt = input("\nPress Enter to return to the main menu or type 'exit' to quit: ")
            if prompt.lower() == 'exit':
                print("Happy Reading!")
                break

        elif choice == "6":
            my_library.display_all_members()

            prompt = input("\nPress Enter to return to the main menu or type 'exit' to quit: ")
            if prompt.lower() == 'exit':
                print("Happy Reading!")
                break

        elif choice == "7":
            member_id = input("Enter Member ID to see their borrowed books: ")
            member_data = my_library.members.get(member_id)
            if member_data:
                member = Member(member_data["name"], member_id)
                member.borrowed_books = member_data["borrowed_books"]
                member.display_borrowed_books()
            else:
                print(f"Error: Member with ID '{member_id}' not found.")

            prompt_return = input("\nPress Enter to return to the main menu or type 'exit' to quit: ")
            if prompt_return.lower() == 'exit':
                print("Happy Reading!")
                break

        elif choice == "8":
            print("Happy Reading")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()