# Functions as parameter/return value
print("*** FUNCTION AS PARAMTER/VALUE ***")

def f1():
    return "f1"

def f2():
    return "f2"

def main(i):
    if i == 1:
        return f1
    elif i == 2:
        return f2
    else:
        print("ERROR: invalid parameter. expected: {1,2}")
        
r = main(2)
x = r()
print(x)


# Functions as parameter/return value 2
print("*** FUNCTION AS PARAMTER/VALUE 2 ***")
import math

def table(func):
    for x in range(0,10):
        print(str(x) + "\t" + str(func(x)))

print(table(math.sin))
print(table(math.cos))


# Decorators (to count method invocations)
print("*** DECORATOR 1 ***")

def outer(func):
    counter = 0
    def inner():
        nonlocal counter
        print("inner() wurde " + str(counter) + " Mal ausgefuehrt")
        counter = counter + 1
        func()                                # hier wird die uebergebene function ausgefuehrt
    return inner
        
@outer
def do_something():
    print("do_something() wurde ausgefuehrt")
    
do_something()
do_something()
do_something()
do_something()




# Decorators (to return cached results)
print("*** DECORATOR 2 ***")
def outer2(func):
    cached = {}                     # create a cache for results
    def inner(x):
        if x in cached:
            print("value " + str(x) + " already in cache")
            return cached[x]
        result = func(x)
        cached[x] = result
        return result
    
    return inner
        
@outer2
def calc_something(x):
    print("calc_something(" + str(x) + ") wurde ausgefuehrt")
    return x * x
    
print(calc_something(5))
print(calc_something(5))
