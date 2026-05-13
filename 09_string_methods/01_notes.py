# name = input("Enter your name: ")
phone_number = input("Enter your phone number: ")
# result = len(name) # returns the length of a string including spaces
# result = name.find(" ") # .find(" ") returns the index of the first occurrence of the specified character/substring
#                            returns -1 if not found
# result = name.rfind("i") # .rfind(" ") returns the index of last occurrence of the specified character/substring                      
#                             returns -1 if not found
# name = name.capitalize() # capitalizes first letter only
# name = name.upper()      # converts entire string to uppercase
# name = name.lower()      # converts entire string to lowercase 
# result = name.isdigit()  # returns True if all characters are digits
# result = name.isalpha()  # returns True if all characters are letters
# result = phone_number.count("-") # counts how many times "-" appears
phone_number = phone_number.replace("-"," ") # replaces all "-" with " "
print(phone_number)

# print(help(str))  # prints all available string methods