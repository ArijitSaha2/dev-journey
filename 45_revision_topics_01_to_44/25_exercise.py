# Import datetime.
# Print:
# - Today's date.
# - Current time.
# - Current year.

import datetime

now = datetime.datetime.now()

print(f"Today's Date: {now.date()}")
print(f"Current time: {now.time()}")
print(f"Current year: {now.year}")