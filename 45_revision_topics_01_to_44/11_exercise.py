# Create a recursive function that counts down from a number entered by the user.
# When it reaches 0, print "Done!".

def countdown(n):
    if n == 0:
        return "Done!"
    else:
        print(n)
        return countdown(n - 1)
    
print(countdown(5))