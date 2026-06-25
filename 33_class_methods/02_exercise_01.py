# Class Methods Exercise 1
# Create a class Book
# Add a class variable called count
# Increment count whenever a new Book object is created
# Create a class method called get_count()
# Return the total number of books
# Create 3 Book objects
# Print the total number of books using the class method

class Book:

    count = 0

    def __init__(self, name, author):
        self.name = name
        self.author = author
        Book.count += 1

    @classmethod
    def get_count(cls):
        return f"Total Books = {cls.count}"

book1 = Book("Jack and Jill", "Nemy")
book2 = Book("Starving for Knowledge", "Stormy")
book3 = Book("Masha and the bear", "Rusta")

print(Book.get_count())