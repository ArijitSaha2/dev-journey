# Create a function that takes a list of student names and their scores
# Skip any student with score below 50 using continue
# Print each passing student's name in uppercase
# Print their score formatted to 2 decimal places
# Count and print how many students passed

def fun (stud, mark):
    count = 0
    for i in range(len(stud)):
        if mark[i] < 50:
                continue
        print(f"Name is {stud[i].upper()}, marks obtained {mark[i]:.2f}")
        count += 1
    print(f"Total Passed: {count}")

l1 = ["Jamesgun", "Harry", "Jessica"]
l2 = [70, 49, 80]
fun(l1, l2)