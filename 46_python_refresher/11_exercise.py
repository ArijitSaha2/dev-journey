# Exercise 11 — Word Counter
# Count how many times each word appears in a list and return the counts in a dictionary.
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# Expected output:
# {"apple": 3, "banana": 2, "orange": 1}

def counter(fruits):
	total_count = {}
	for fruit in fruits:
	   		if fruit not in total_count:
	   			total_count[fruit] = 1
	   		else:
 		   		total_count[fruit] += 1
	return total_count
	

print(counter(["apple", "banana", "apple", "orange", "banana", "apple"]))
