# Exercise 032 - Employee Credentials

# First name and last name = John and Doe respectively.
# Age is 28
# Address = 123 Main Street,  then Apartment 4B
# Experience = 5, postion is data analyst, salary $75000
# employee_code = 'DEV-2026-JD-001'

# Requirements:
# Concatenate the given values from first name till address in employee_info with ' ' spaces.
# Concatenate the values such as experience, position and salary in a var called employee_card. format: experience | position | salary
# Take the employee_code and put them in department, year_code, initials, last_three respectively using string slicing.

first_name = 'John'
last_name = 'Doe'
age = 28

full_name = first_name + ' ' + last_name

employee_info = full_name
employee_info += ' is ' + str(age) + ' years old'
print(f"Employee Info: {employee_info}")

experience = 5
position = 'Data Analyst'
salary = 75000

employee_card = f"Experience: {experience} | Position: {position} | Salary: ${salary}"
print(employee_card)

employee_code = 'DEV-2026-JD-001'

department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]
last_three = employee_code[-3:]

print(f"Employee Code: {employee_code}\nDepartment: {department}\nYear_code: {year_code}\nInitials: {initials}\nLast_three: {last_three}")