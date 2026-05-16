# Create a function that takes a string
# Count how many uppercase letters it has
# Count how many lowercase letters it has
# Count how many digits it has
# Print all three counts

def st(strin):
    count = 0
    for char in strin:
        if char.isupper():
            count += 1
    print("Uppercase letters =", count)
    
    num = 0
    for char in strin:
        if char.islower():
            num += 1
    print("Lowercase letters =", num)

    cont = 0
    for char in strin:
        if char.isdigit():
            cont += 1
    print("Number of digits =", cont)
       
st("There are Alot of Places TO visit123")