from Cython.Shadow import inline
def f(a,b,c):
    print(a)
    print(b)
    print(c)
    

f(1,2,3)

l = [1,2,3]
f(l[0],l[1],l[2])

f(*l)                # '*' vor variablen name, löst eine liste auf eine menge von parametern auf





def calc_max(*params):        # variable parameter anzahl
    print(params)
    
calc_max(2,4,6,8,2,6)

    
    
    
def f2(**args):          # übergabe der parameter als dictionary
    print(args)
    
f2(a="b", c="d", e="f")




def f3(a = 3, b = 2, c = 1):    # anstelle von parametern kann auch ein dictionary übergeben werden
    print(a)
    print(b)
    print(c)
    
d1 = {'a': 10, 'c': 20}         # anstelle von parametern kann auch ein dictionary übergeben werden
f3(**d1)    

    
    
    
    
    
#%matplotlib inline
import matplotlib.pyplot as plt

def create_plot(list_x, list_y, **plot_params):
    plt.plot(list_x,list_y, **plot_params)
    plt.xlabel("x")
    plt.ylabel("y = f(x) = x^2")
    plt.axis([-10,10,0,100])
    plt.show()
    
def f4(x):
    y = []
    for xi in x:
        y.append(xi ** 2)
    return y
    
x = range(-10,11)
y = f4(x)
print(x)
print(y)
create_plot(x, y, color="r", linewidth=2, linestyle="dashed")



