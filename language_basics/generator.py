def f1(a,b):
    for i in range(a,b):
        print("f1: " + str(i))
        yield i**2

def f2(a,b):
    l = []
    for i in range(a,b):
        print("f2: " + str(i))
        l.append(i**2)
    return l

for y in f1(0,10):
    print("y=" + str(y))