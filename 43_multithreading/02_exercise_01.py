# Exercise 1
# Import threading and time.
# Create a function called download_file() that waits 3 seconds,
# then prints "File downloaded".
# Create a function called send_email() that waits 2 seconds,
# then prints "Email sent".
# Create separate threads for both functions.
# Start both threads.
# Wait for both threads to finish using join().
# Print "All tasks completed" at the end.

import threading
import time

def download_file():
    print("Downloading...")
    time.sleep(3)
    print("File downloaded")

def send_email():
    print("Sending email...")
    time.sleep(2)
    print("Email sent")

download = threading.Thread(target=download_file)
download.start()

send = threading.Thread(target=send_email)
send.start()

download.join()
send.join()

print("All tasks completed")