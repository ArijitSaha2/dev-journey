# OOP Exercise 2
# Create a class called Book
# Attributes: title, author, pages, is_read (boolean)
# Add a method called read_book() that sets is_read to True and prints "{title} has been marked as read"
# Create two book objects
# Call read_book on one of them, then print is_read for both to confirm only one changed

class Book:
    def __init__(self, title, author, pages, is_read):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = is_read


    def read_book(self):
        self.is_read = True
        print(f"{self.title} has been marked as read")


book1 = Book("Mary in the wonderland", "Aria", 200, False)
book2 = Book("Masha and the bear", "Russy", 1000, False)

book1.read_book()

print(f"{book1.is_read}")
print(f"{book2.is_read}")