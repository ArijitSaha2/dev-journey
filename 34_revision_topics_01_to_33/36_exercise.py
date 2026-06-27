# Revision Exercise 36
# Create a class Bank. Add a class variable bank_name = "ABC Bank".
# Create a class method change_bank_name(name) that changes bank_name.
# Print the old bank name, change it to "XYZ Bank", then print the new bank name.

class Bank:

    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls):
        Bank.bank_name = "XYZ Bank"
        return Bank.bank_name

print(f"Old: {Bank.bank_name}")
print(f"New: {Bank.change_bank_name()}")