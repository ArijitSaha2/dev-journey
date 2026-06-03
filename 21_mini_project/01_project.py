# Requirements = credentials, authentication, balance, deposit, withdraw, 
# transaction limit / insufficient funds check, exit/logout.

import time 

def greet():
    print()
    g = "Welcome To the Banking Site"
    print(f"{g:>50}")
greet()

Navigation = "Where would you like to go: Banking ID creation(B), Login(L), Deposit(D), Withdraw(W), " \
"Balance(Bal), Exit(E) - Will also log you out"

user_input = ""

balance = 0

while user_input != "e":
    print()
    print(Navigation)
    print()
    user_input = input("Enter the navigation point\nAnswer: ").lower()
    if user_input == "b":
        credentials = ()
        def user_id_input():
            user = input("Create a username: ")
            password = input("Create a strong password: ")
            return user, password
        credentials = user_id_input()
        print(credentials)
        print("Login(L) to view balance and use futher features")


    elif user_input == "l":
        def verify():
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if credentials[0] == username and credentials[1] == password:
                print("Verify and authenticating information provided please wait......")
                time.sleep(5)
                print(f"Acess Granted {username}!!!")
            elif credentials[0] != username:
                print(f"Invalid username")
            elif credentials[0] == username or credentials[1] != password:
                print(f"Username Correct, Wrong password")
            if credentials[0] != username or credentials[1] != password:
                print("Did you forget credentials?"
                    "\nCONTACT US AT: 029281"
                    "\nEMAIL US AT:   xyz@gmail.com")
        verify()
    
    
    elif user_input == "d":
        def balance_dep():
            global balance
            deposit = int(input("Enter amount to deposit in account: "))
            print("Processing please wait....")
            time.sleep(1)
            balance += deposit
            print("Deposit Successful!!")
            to_check = input(f"IF you want to Check Balance Y/N\nAnwer: ").lower()
            if to_check == "y":
                print("Fetching balance....!")
                time.sleep(1)
                print(f"Current balance: {balance}")
            if to_check == "n":
                print("Okay!!")
            

        balance_dep()
    
    elif user_input == "w":
        def withdrawal():
            global balance
            print("TRANSACTION LIMITs"
                "SENDING = 1LAKH per Day"
                "\nRECEIVING = 1LAKH per Day"
                "\nExtra charges may apply for Transaction above the Limits")
            withdraw = int(input("Enter amount you want to withdraw: "))
            if withdraw > balance:
                print("Insufficient Funds")
            elif withdraw <= balance:
                balance = balance - withdraw
                print(f"Debitted: {withdraw}")
                print(f"Remaining balance {balance}")
        withdrawal()

    elif user_input == "bal":
        def view_balance():
            print(f"Current balance = {balance}")
        view_balance()

    elif user_input == "e":
        print("Thanks For using Our services! Until next Time.")