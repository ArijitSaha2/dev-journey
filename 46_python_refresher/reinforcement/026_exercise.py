# Exercise 026 — Exclusive Creation with "x"
# Your task:
#     Create a new file named lock.txt using exclusive creation mode ("x").
#     Write a short status message into it inside a with block.
#     Handle the case where lock.txt already exists so it doesn't crash with an unhandled error.

# Expected output (when lock.txt does not exist):
# Created lock.txt successfully.

file_path = "lock.txt"

try:  
    with open(file_path, "x") as file:
        file.write("Created lock.txt successfully")
        print(f"Status: Created {file_path} successfully")

except FileExistsError:
    print(f"File already Exists")
    print(f"Either change the code or make a new file through code!!!")