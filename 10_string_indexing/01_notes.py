# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

# Positive indexing - starts from 0 (left to right)
# s[0] = first character, s[1] = second, and so on

# Negative indexing - starts from -1 (right to left)  
# s[-1] = last character, s[-2] = second from last, and so on

# Slicing syntax = [start : end : step]
# start = index to begin (inclusive), default is 0
# end   = index to stop (exclusive, not included), default is end of string
# step  = how many characters to skip, default is 1

# Examples:
# s[0:4]   = characters from index 0 up to but not including 4
# s[:4]    = same as above, start defaults to 0
# s[5:]    = from index 5 to end of string
# s[::2]   = every 2nd character from start to end
# s[::-1]  = reverses the string (step -1 goes backwards)

credit_number = "1234-5678-9012-3456"

last_digits = credit_number[-4:]
print(f"XXX-XXX-XXX-{last_digits}")
credit_number = credit_number[::-1]
print(credit_number)
# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::3])