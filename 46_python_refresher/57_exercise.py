# Day 6 — Exercise 57: Variable Scope
# Write a function that:
# 1. Uses a local variable.
# 2. Accesses a global variable.
# 3. Modifies a global variable using global.

def scope():
    y = 22 # local var for modifying global var
    global x 
    x = y
    # x = 20 # local value, if we uncomment this value python will use this x instead of declared global x
    print(f"Global variable inside function: {x}")
    print(f"Local variable inside function: {y}")
    print()
    
x = 10
print(f"Global variable before function: {x}")
print()

scope()

print()
print(f"Global variable after function: {x}")