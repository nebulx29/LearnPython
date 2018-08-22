# Primitive Datatypes are passed by value
a = 5

def f(x):           # arguments are passed by value (copy)
    x = x + 1
    print(x)        # prints 6
    
f(a)                # arguments are passed by value (copy)
print(a)            # prints 5    



# Datastructures/Objects are passed by reference
l = [3,7,5,9]

def f1(l):          # complex datatypes/objects are passed by reference
    l.append(0)
    print(l)

print(l)    
f1(l)
print(l)



# Objects are passed by references
class C1:
    def __init__(self, i):
        self.i = i
    def update(self, i):
        self.i = i
    def __str__(self):
        return "[C1] " + str(self.i)

c = C1(5)

def f2(c):
    c.update(9)
    print(c)
    
print(c)
f2(c)
print(c)