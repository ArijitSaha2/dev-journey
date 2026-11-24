# Exercise 030
# subject = "  python basics  "
# score = 92

# Requirement: 
# Strip outer spaces and capitalize subject (save to a new variable).
# Slice the first 3 letters as a short code.
# Print one formatted line with the code, cleaned subject, and score.
# Leave subject unchanged.

subject = "  python basics  "

score = 92

space = subject.strip().capitalize()

short_code = space[:3]

print(f"Code: {short_code} | Subject: {space} | Score: {score}")