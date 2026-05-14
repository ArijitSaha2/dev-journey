# validate user input exercise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

username = input("Enter username: ")

if len(username) > 12:
    print("Your username should not be more then 12 characters")

elif  not username.find(" ") == -1:
    print("Username cannot contain spaces")

elif username.isalpha() == False:
    print("Username cannot contain digits")

else:
    print(f"Welcome! {username}")