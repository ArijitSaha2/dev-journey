# Exercise 14 — Student Names
# Given:
# scores = {"Alex": 85, "John": 42, "Sarah": 91, "Mike": 58, "Emma": 73}

# Write a function that returns a list of students who scored between 50 and 80 (inclusive).

# Expected output:
# ["Mike", "Emma"]

def student_name(scores):
    T50_and_80 = []
    for keys, values in scores.items():
        if values >= 50 and values <= 80:
            T50_and_80.append(keys)
            
    return T50_and_80
    
print(student_name({"Alex": 85, "John": 42, "Sarah": 91, "Mike": 58, "Emma": 73}))