# Exercise 2
# Import threading and time.
# Create a function called process_order() that accepts an order name and wait time.
# Print that the order is being processed.
# Wait for the given number of seconds.
# Print that the order is ready.
# Create three threads with different order names and wait times.
# Start all three threads.
# Wait for all three threads using join().
# Print "All orders completed" at the end.

import threading
import time 

def process_order(order_name, wait_time):
    print("order is being processed please wait...")
    time.sleep(wait_time)
    print(f"{order_name} is ready")

order1 = threading.Thread(target=process_order, args=("mobile", 4))
order1.start()

order2 = threading.Thread(target=process_order, args=("fruits", 3))
order2.start()

order3 = threading.Thread(target=process_order, args=("cereal", 2))
order3.start()

order1.join()
order2.join()
order3.join()

print("All orders completed")