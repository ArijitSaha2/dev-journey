# create a variable for your age, your name, a list of your hobbies. Then check if a hobby is in the list, compare your age to something, do some math. Real stuff, not textbook problems.

age = 21
print("Your age = ", age)

name = "Allison"
print("Your name =", name)

hobbies = ["gaming","reading","sleeping","adventuring/exploring"] 
print("Your hobbies are - ", hobbies)

print("Is Football one of your Hobby? Answer:","football" in hobbies)
lost = ["marbles"]
print("is lost item in your hobbies =",lost is hobbies)

number = 1000
print("Number is", number)

print(f"Is age greater than number = {age > number}")

age += 10

print(age)