# Exercise 017 — Polymorphism
# Your task:
# - Create a class Dog with a method speak() that returns "Woof!".
# - Create a class Cat with a method speak() that returns "Meow!".
# - Create one object of each class.
# - Call speak() on both objects.
# Expected output:
# Woof!
# Meow!

class Dog:
    def speak(self):
        return "Woof!"

class Cat: 
    def speak(self):
        return "Meow!"

d = Dog()
c = Cat()

print(d.speak())
print(c.speak())