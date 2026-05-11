# Create a function that checks if a number is positive, negative, or zero
# Return the result
# Call it 3 times with different values

# As per the Question 

def check(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

result  = check(1)
result1 = check(-1)
result2 = check(0)

print(result)
print(result1)
print(result2)

# Can be done this way as well 

# def check(n):
#     if n > 0:
#         return "Positive"
#     elif n < 0:
#         return "Negative"
#     else:
#         return "Zero"

# result = check(int(input("Enter Number: ")))

# print(result)