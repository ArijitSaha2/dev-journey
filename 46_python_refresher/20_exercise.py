# Exercise 20 — Department Salary Report
# A company stores employees by department:
# company = {"IT": {"Alex": 45000, "John": 28000},  "HR": {"Sarah": 35000, "Mike": 25000},  "Sales": {"Emma": 50000, "David": 32000}}

# Write a function that returns a dictionary containing each department's total salary expenditure.

# Rules:
# - Use a function and loops.
# - Use dictionary access and accumulation.
# - No sum().

def salary_report(company):
    total_salary_ex = {}

    for department in company:
        total = 0

        employees = company[department]

        for employee in employees:
            total += employees[employee]

        total_salary_ex[department] = total

    return total_salary_ex


company = {
    "IT": {"Alex": 45000, "John": 28000},
    "HR": {"Sarah": 35000, "Mike": 25000},
    "Sales": {"Emma": 50000, "David": 32000}
}

print(salary_report(company))