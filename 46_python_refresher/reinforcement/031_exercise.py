# Exercise 031 — Clean Version Tag

# raw_tag = "  Release-v2.4-Beta  "

# Requirements:
# Strip outer whitespace and convert to lowercase into a new variable.
# Replace "beta" with "rc" without changing raw_tag.
# Print the updated tag and verify raw_tag stayed unchanged.

raw_tag = "  Release-v2.4-Beta  "

spaces_low = raw_tag.strip().lower()

updated = spaces_low.replace("beta", "rc")

print("Old: ",raw_tag)
print("New:",updated)