# Class Methods Exercise 2
# Create a class BankAccount
# Add a class variable called bank_name
# Create a class method called change_bank_name()
# The method should change the bank_name
# Print the bank name before changing it
# Change the bank name using the class method
# Print the bank name again

class BanKAccount:

    bank_name = "ABC Bank"
    
    @classmethod
    def change_bank_name(cls):
        BanKAccount.bank_name = input("Enter Bank Name: ")
        return f"{BanKAccount.bank_name}"

print(f"Old Bank Name: {BanKAccount.bank_name}")
print(f"New Bank Name: {BanKAccount.change_bank_name()}")