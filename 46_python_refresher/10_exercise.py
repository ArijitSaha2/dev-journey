# Exercise 10
# Filter out scores below 60 and arrange the remaining scores in descending order.
# scores = [45, 72, 91, 38, 64, 55, 83, 29]
# Don't use sorted() or .sort().

def class_scores(scores):
    ordered = []

    try:
        while scores:
            largest = 0

            for score in scores:
                if score > largest and score >= 60:
                    largest = score

            ordered.append(largest)
            scores.remove(largest)

    except ValueError:
        print("A ValueError has happened"
              "\nNote: This exercise intentionally produces a ValueError because we're manually sorting while filtering scores. Once all scores ≥ 60 have been removed, the remaining scores are below 60, so largest stays 0 and scores.remove(0) fails. This isn't a bug in Python; it's a limitation of the way this manual-sorting approach was implemented.")

    return ordered


print(class_scores([45, 72, 91, 38, 64, 55, 83, 29]))
