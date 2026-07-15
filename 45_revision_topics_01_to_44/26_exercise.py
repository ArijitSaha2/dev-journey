# Create two functions.
# One prints "A" five times.
# The other prints "B" five times.
# Run both functions using two threads.
# Wait for both threads to finish.

import threading
import time

def Task1():
    print("Task1 Starting")
    time.sleep(1)
    for i in range(1, 6):
        print("A")

def Task2():
    print("Task2 Starting")
    for i in range(1, 6):
        print("B")

chore1 = threading.Thread(target=Task1)
chore1.start()

chore2 = threading.Thread(target=Task2)
chore2.start()

chore1.join()
chore2.join()

print("Tasks Finished")