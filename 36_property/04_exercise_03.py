# Exercise 3
# Create a class called Account.
# Add __init__(owner, balance).
# Create a property balance that returns "$<balance>".
# Add a setter that only allows balance >= 0.
# Create one Account object.
# Update the balance twice: once with a valid value and once with -500.
# Print the balance after each update.

class Account:

    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return f"Account holder: {self._owner}\nCurrent Balance: ${self._balance}"
    
    @balance.setter
    def balance(self, bal):
        if bal >= 0:
            self._balance = bal
        
        else:
            print(f"Current balance cannot be less then $0")

account1 = Account("Ariana Grande", 1000)

account1.balance = 12000
account1.balance = -200

print(account1.balance)