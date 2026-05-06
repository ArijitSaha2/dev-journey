# Ask the user to enter a score (0-100)
# Print the grade based on the score
# 90 and above = A
# 80 to 89 = B
# 70 to 79 = C
# 60 to 69 = D
# Below 60 = F
# Handle scores below 0 or above 100 as invalid

score = int(input('Enter a score from 0 to 100: '))

if score < 0 or score > 100:
    print('Invalid')

elif score >= 90:
    print("A")

elif score >= 80 and score <= 89:
    print("B")

elif score >= 70 and score <= 79:
    print("C")

elif score >= 60 and score <= 69:
    print('D')

else:
    print("F")