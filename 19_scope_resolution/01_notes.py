# variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    # x = 1 # Local version 
    print(x)

def func2():
    # x = 2 # Local version 
    print(x)

x = 3 # Global Version Used only if Local & Enclosed don't Exist

func1()
func2()

from math import e # built-in e
def func3():
    print(e)

# e = 3 # global e
func3()