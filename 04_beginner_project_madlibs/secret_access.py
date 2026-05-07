logincount = 0

username = input("Enter a name to create username: ")
password = input("Create Password: ")

credentials = [username, password]

print("Time to login!!, Please use valid credentials or you will be denied access + you have 3 attempts only!!!")

while logincount < 3:
    logincount += 1

    nam = input("Enter your Username: ")
    pas = input("Enter your Password: ")
    
    if nam != username and pas != password:
        print("Bruh both are invalid values -_-")

    elif nam == username and pas == password:
        print("Access Granted!!!")
        break

    elif nam != username:
        print("Invalid username, Have u entered the correct username without typos???")

    elif pas != password:
        print("Wrong Password!!, Enter correct password to move forward.")

    print(f"You are running out of attempts {logincount} / 3")

else:
    print("You ran out of attempts for this Session, Better luck next time")
    print("Attempting to inject viruses and malware...")
    print("successful")
    print("Got access to multiple gmail acc, including spotify and epic games accounts")