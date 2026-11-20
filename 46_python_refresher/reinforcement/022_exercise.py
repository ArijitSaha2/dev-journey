# Exercise 022 — Multithreading
# Create two independent functions:
# - One prints the numbers 1–5.
# - The other prints the letters A–E.
# Run both functions using separate threads.

# Requirements:
# - Both functions should execute concurrently.
# - Each function should pause briefly between iterations.
# - Ensure both threads finish before the main program exits.

import threading 
import time

def task1():
    for x in range(1, 6):
        print(x)
        time.sleep(1)
    
def task2():
    y = ["A", "B", "C", "D", "E"]
    for x in y:
        print(x)
        time.sleep(1)
        
work1 = threading.Thread(target = task1)
work1.start()

work2 = threading.Thread(target = task2)
work2.start()

work1.join()
work2.join()

print("Done!")