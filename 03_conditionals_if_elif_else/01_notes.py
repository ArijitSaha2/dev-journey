# Conditionals (if, elif, else)

# if statements

""" if statements are used with conditions to print out the necessary output based on required specifications or true and false. Like if the statement is true it will run a code block. If False, it moves to elif or else. """

# Example

condition =  int(input("Enter your number: "))
if condition > 0:
    print("Will Execute or Worked!")
elif condition < 0:
    print("Typo or invalid value -_-, Values below 0 are not accepted")
else:  # condition == 0 falls here since it's neither > 0 nor < 0
    print("In Python 0 or [] is considered empty")
# else: 
#     print("Not words only numbers!!!!") # Note: if user enters a string, int() will throw an error before reaching else 
                                          # Solution is try/except - covered later in error handling