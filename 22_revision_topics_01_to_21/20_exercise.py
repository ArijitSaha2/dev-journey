# Extra - Scope
# x = "global"
# Create a function that creates a local x = "local"
# Print both local x inside the function and global x outside

x = "global"

def func():
    x = "local"
    print(x)

func()
print(x)

# Extra - Scope (Hard)
# Create a global counter = 0
# Create a function that increments counter by 1 each time it's called
# Call it 5 times and print the final counter value


counter = 0

def func():
    global counter
    counter += 1

func()
func()
func()
func()
func()
print(counter)