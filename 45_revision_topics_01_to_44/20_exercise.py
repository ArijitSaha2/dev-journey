# Create a decorator called message().
# Before a function runs, print "Starting...".
# After the function finishes, print "Finished!".
# Decorate a function that prints "Hello World".
# Call the decorated function.

def hello(func):
    def wrapper(*args, **kwargs):
        print("Starting")
        func(*args, **kwargs)
        print("Finished!")
    return wrapper

@hello 
def run_function(say):
    print(say)

run_function("Hello World")