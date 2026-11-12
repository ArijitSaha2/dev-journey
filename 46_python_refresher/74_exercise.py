# Exercise 74 — Multithreading
# What this tests: Creating and running threads using Python's threading module.

# Task: Create two independent tasks that run using separate threads.

# Requirements:
# 1. Import threading and time.
# 2. Create a function called task_one() that prints numbers 1–5, with a one-second delay between prints.
# 3. Create another function called task_two() that prints letters A–E, also with a one-second delay.
# 4. Create two threads targeting those functions.
# 5. Start both threads.
# 6. Use .join() to wait for both threads to finish.
# 7. Print "Both tasks completed!" after they finish.
# Rules:
# - Use threading.Thread().
# - Don't use classes.
# - No additional libraries.

import threading
import time

def task_one(num):
    for x in num:
        print(x)
        time.sleep(1)
        
n = [1, 2, 3, 4, 5]


def task_two(letter):
    for x in letter:
        print(x)
        time.sleep(1)

let = ["A", "B", "C", "D", "E"]


work1 = threading.Thread(target = task_one, args = (n, ))
work1.start()

work2 = threading.Thread(target = task_two, args = (let, ))
work2.start()

work1.join()
work2.join()

print("Both tasks completed!")