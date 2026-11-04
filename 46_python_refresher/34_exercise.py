# Revision Exercise 34 — Order Processing
# Write a function process_order(age, has_account, is_verified, items, balance).

# The function must:
# 1. Check whether the customer is at least 18.
# 2. Check whether they have an account.
# 3. Check whether their account is verified.
# 4. Check whether items contains at least one item.
# 5. Check whether their balance is sufficient to place the order (assume the order costs ₹500).
# 6. If all conditions pass, deduct ₹500 and return the updated balance. Otherwise, explain why the order was rejected.
# Use variables, data types, arithmetic, comparison operators, logical operators and conditional statements.

import time 

def process_order(age, has_account, is_verified, items, balance):

    if age >= 18:
        if has_account == True:
            print("Verifying")
            time.sleep(1)
            if is_verified == True:
                print("proceeding to next step")
                time.sleep(2)
                if items:
                    print("Checking items in bag")
                    print(f"{items}")
                    time.sleep(1)
                    if balance >= 500:
                        balance -= 500
                        print("order placed successfully")

                    elif  balance < 500:
                        print("Insufficient balance")
                elif not items:
                    print("No items to purchase")
            elif is_verified == False:
                print("Customer has to be verified to place an order")
        elif has_account == False:
            print("Create an account to place an order")
            
    else:
        print("Customer must be 18 or older to place an order")
                    
    return balance

print(process_order(25, True, True, items = ["Cereal", "Milk", "Hot Chocolate"], balance=10000))