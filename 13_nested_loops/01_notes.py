# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

rows = int(input("Enter the Number of rows: "))
columns = int(input("Enter the Number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="") # end="" keeps output on the same line instead of new line
    print() # moves to the next line after each row is complete