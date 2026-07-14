# Create a BankAccount class.
# Store the owner's name and balance.
# Use a property for the balance.
# Create a __str__() method to display the account name and balance.
# Print the object directly.

class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
    
    @property
    def balance(self):
        return f"{self._balance}"
    
    def __str__(self):
        return f"Account: {self._name}\nBalance: {self._balance}"

account = BankAccount("Aria", 5000)

print(account)