# Write a function class_scores(scores) that:
# 1. Takes a list of student scores.
# 2. Keeps only scores 60 or higher.
# 3. Sorts the qualifying scores in descending order (highest to lowest).
# 4. Does not use Python's built-in sort() or sorted().

# Example input = [45, 72, 91, 38, 64, 55, 83, 29]

def class_scores(scores):
    qualifying_scores = []
    result = []
    large = 0 
    for score in scores:
        if score >= 60:
            qualifying_scores.append(score)

    while qualifying_scores:
        large = qualifying_scores[0]

        for score in qualifying_scores:
            if large < score:
                large = score

        result.append(large)
        qualifying_scores.remove(large)
    return result
print(class_scores([45, 72, 91, 38, 64, 55, 83, 29]))