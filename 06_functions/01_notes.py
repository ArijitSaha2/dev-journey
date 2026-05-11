# functions - It is used to create a block of code that will be executed only if the function is called. They also contain arguments but can work without arguments as well.

# Normal Function
def jessie(mood= "sad"): # "sad" is a default argument, used when no argument is passed
    # code here gets executed when we call the function
    print(mood)

    print("Dogo")

jessie('happy') # passing "happy" as argument, overrides default
print() # prints a blank line for spacing
jessie() # no argument passed, uses default value "sad"

# return - sends a value back from the function so it can be used or stored outside

# Functions with return 
def re(word = "Sun ", sentence = "is great!!"):
    return (word + sentence)

result = re() 
print(f"Uses value assigned in function = {result}")
print(re("Invincible ","Has bad animation"))