# Create a simple login system
# Ask the user to enter a username and password
# If both are correct print "Login Successful"
# If username is correct but password is wrong print "Wrong Password"
# If username is wrong print "Invalid Username"

name = str(input('Enter your name: '))
password = input("Create a strong password: ")
credentials = [name, password]

print("Enter valid Username and password")

name = str(input("Username: "))
password = input("Password: ") 

if name == credentials[0] and password == credentials[1]:
    print('Login successful')

elif name == credentials[0] and password != credentials[1]:
    print('Wrong Password')

elif name != credentials[0] and password != credentials[1]:
    print('Invalid Username and You have Entered invalid Credentials!!')
