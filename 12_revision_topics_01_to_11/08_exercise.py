# Create a list of words ["apple", "banana", "kiwi", "strawberry", "fig"]
# Use a loop to find the longest and shortest word
# Print both (no len() inside min/max allowed, use a loop)

l = ["apple", "banana", "kiwi", "strawberry", "fig"]

long = l[0]

short = l[0]

for lo_sh in l:

    if len(lo_sh) > len(long):
        long = lo_sh

    if len(lo_sh) < len(short):
        short = lo_sh

print(f"Longest  = {long}")
print(f"Shortest = {short}")