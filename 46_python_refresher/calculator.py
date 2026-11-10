def add(a, b):
    return f"Add: {a + b}"

def sub(a, b):
    return f"Sub: {a - b}"

def Multiply(a, b):
    return f"Multiply: {a * b}"

def Divide(a, b):
    try: 
        return f"Divide: {a / b}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."