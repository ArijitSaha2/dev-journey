# Loops

"""
There are 2 types of loops in python:
while loop — keeps running as long as a condition is True
for loop — runs a set number of times or iterates over a collection
"""

# break — exits the loop immediately
# continue — skips the current iteration and moves to the next one

""" 
Example:

for loop

name = Rose

name = ("Rose","Natalie", "Jessika", "Mary")

for words in name:
    if words == "Natalie":
        continue # It is used when we want the loop to move forward and don't want a certain value to be printed
    print(words)

    
while loop

i = 1

while i < 10:
    print(i)
    i += 1
    if i == 8:
        break # Used when we wanna stop the loop before its completely executed.

print('the end')


"""