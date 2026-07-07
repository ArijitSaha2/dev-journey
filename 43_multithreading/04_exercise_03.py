# Exercise 3
# Import threading and time.
# Create a function called backup_files() that:
# - prints "Backup started"
# - waits 5 seconds
# - prints "Backup completed"
#
# Create a function called check_updates() that:
# - prints "Checking for updates"
# - waits 2 seconds
# - prints "Update check completed"
#
# Create a function called sync_data() that:
# - prints "Syncing data"
# - waits 3 seconds
# - prints "Data synced"
#
# Create and start a separate thread for each function.
# Wait for all three threads to finish.
# Print "System tasks completed" at the end.

import threading 
import time 

def backup_files():
    print("Backup started...")
    time.sleep(5)
    print("Backup completed")

def check_updates():
    print("checking for updates...")
    time.sleep(2)
    print("Update check completed")

def sync_data():
    print("Syncing data...")
    time.sleep(3)
    print("Data synced")

backup = threading.Thread(target=backup_files)
backup.start()

update = threading.Thread(target=check_updates)
update.start()

sync = threading.Thread(target=sync_data)
sync.start()

backup.join()
update.join()
sync.join()

print("System tasks completed")