# Exercise 15 — Score Statistics
# Given:
# scores = [85, 42, 91, 58, 73, 35, 100]

# Write a function that returns a dictionary containing:
# - "passed" — number of scores 60 or above.
# - "failed" — number of scores below 60.
# Expected output:
# {"passed": 4, "failed": 3}

# Rules:
# - Use a function and a loop.
# - Use a dictionary to store the results.
# - No len() or sum().

def score_stats(scores):
    success_or_failed = {}
    passed = 0 
    failed = 0
    for score in scores:
        if score >= 60:
            passed += 1
        else: 
            failed += 1
    success_or_failed["passed"] = passed
    success_or_failed["failed"] = failed

    return success_or_failed

print(score_stats([85, 42, 91, 58, 73, 35, 100]))