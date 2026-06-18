# OOP Exercise 3
# Create a class called BankAccount
# Attributes: owner, balance
# Add a method called deposit(amount) that adds to balance and prints the new balance
# Add a method called withdraw(amount) that subtracts from balance if there's enough money, otherwise prints "Insufficient funds"
# Create one account object and test both methods

class BankAccount:  # CLASS - the blueprint
    def __init__(self, owner, balance, deposit, withdraw):  # CONSTRUCTOR - runs automatically when object is created
        self.owner = owner        # ATTRIBUTE - belongs to this specific object
        self.balance = balance    # ATTRIBUTE
        self.deposit = deposit    # ATTRIBUTE
        self.withdraw = withdraw  # ATTRIBUTE

    def credit(self):  # METHOD - an action this object can perform
        self.deposit = int(input("Enter the amount to deposit: "))
        self.balance += self.deposit
        print(f"Depositted = {self.deposit} \nTotal balance = {self.balance}")

    def debit(self):  # METHOD
        self.withdraw = int(input("Enter the amount to withdraw: "))
        if self.withdraw <= self.balance:
            self.balance -= self.withdraw
        else:
            print("Insufficient funds")
        print(f"Withdrawn = {self.withdraw} \nTotal balance = {self.balance}")

Account = BankAccount("Camilla", 0, 0, 0)  # OBJECT - actual instance built from the class, with real data
Account.credit()
Account.debit()