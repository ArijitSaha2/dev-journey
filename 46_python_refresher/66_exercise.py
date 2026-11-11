# Exercise 66 — Polymorphism
# Task: Create a simple payment system demonstrating polymorphism.

# Requirements:
# 1. Create three classes:
# - CreditCard
# - UPI
# - PayPal
# 2. Each class must have a method called pay(amount).
# 3. Each method should display a different payment message containing the amount.
# 4. Create one object from each class.
# 5. Store all three objects in a list.
# 6. Use a loop to call pay(1000) on every object.

# Rules:
# - Each class must implement its own pay() method.
# - No inheritance required.
# - Focus on how the same method call produces different behaviour depending on the object.

class CreditCard:

    def pay(self, amount):
        print(f"Credit Card payment: {amount}")


class UPI:

    def pay(self, amount):
        print(f"UPI payment: {amount}")

class PayPal:

    def pay(self, amount):
        print(f"Paypal payment: {amount}")


card = CreditCard()
unified1 = UPI()
payp1 = PayPal()

payments = [card, unified1, payp1]

for x in payments:
    x.pay(1000)