# Exercise 018 — Duck Typing
# Your task:
# - Create two classes: PDF and WordDocument.
# - Both should have a method called open().
# - Each method should print a different message.
# - Create one object of each class.
# - Call open() on both objects.
# Expected output:
# Opening PDF document...
# Opening Word document...

class PDF:
    def open(self):
        print("Opening PDF document...")

class WordDocument:
    def open(self):
        print("Opening Word document...")

pd = PDF()
wod = WordDocument()

pd.open()
wod.open()