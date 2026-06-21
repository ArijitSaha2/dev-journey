# Class Variables Exercise 2
# Create a class called BankAccount
# Class variable: bank_name = "PyBank", total_accounts = 0
# Instance variables: owner, balance
# Increment total_accounts every time a new account is created
# Create 2 accounts and print bank_name, total_accounts, and each owner's balance

class BankAccount:
    bank_name = "PyBank"
    total_accounts = 0 
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 
        BankAccount.total_accounts += 1

account1 = BankAccount("Elizabeth", 500)
account2 = BankAccount("Tanya", 10000)

print(f"Welcome to {BankAccount.bank_name}!!\nTotal Accounts = {BankAccount.total_accounts}")
print(f"Account1 Balance - {account1.balance}")
print(f"Account2 Balance - {account2.balance}")