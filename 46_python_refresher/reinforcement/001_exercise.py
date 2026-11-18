# Exercise 01 — Countdown
# Write a recursive function that:
# - Accepts an integer n.
# - Prints numbers from n down to 1.
# - Prints "Done!" when it reaches the end.
# - Uses a base case to stop recursion.
# Example output for n = 5:
# 5
# 4
# 3
# 2
# 1
# Done!

def count_down(num):

    if num > 0:
        print(num)
        count_down(num - 1)
    else:
        print("Done!")
    
n = int(input("Enter number: "))
count_down(n)