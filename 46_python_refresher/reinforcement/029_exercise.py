# Exercise 029 — os.path.join()

# Task:
# Build a path from "data", "invoices", and "q3_report.csv" using os.path.join(), and print the resulting path.

# Expected output:
# data/invoices/q3_report.csv (on Windows, backslashes)

import os

result = os.path.join("data", "invoice", "q3_report.csv")
print(result)