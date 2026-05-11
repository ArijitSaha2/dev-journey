# Create a function that takes a list of numbers as argument
# Return the largest number in the list
# No built-in max() function allowed

# Simpler and more accurate method using loops
def new(L):
    largest = L[0]
    for num in L:
        if num > largest:
            largest = num
    return largest

print(new([2,3,1,6,8,9]))


# Hardcoded approach not Recommended
# def l_of_n(L = [7, 2, 3, 4]):

#     if L[0] > L[1] and L[0] > L[2] and L[0] > L[3]:
#         return f"{L[0]} is the largest number in the list"
    
#     elif L[1] > L[0] and L[1] > L[2] and L[1] > L[3]:
#         return f"{L[1]} is the largest number in the list"
    
#     elif L[2] > L[0] and L[2] > L[1] and L[2] > L[3]:
#         return f"{L[2]} is the largest number in the list"
    
#     else:
#         return f"{L[3]} is the largest number in the list"
    
# result = l_of_n()
# print(result)