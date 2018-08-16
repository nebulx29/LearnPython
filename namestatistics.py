import matplotlib.pyplot as plt


name = "Britney"
sex = "F"
state = "CA"
xs = []
xy = []

with open("names.csv","r") as f:
    for line in f:
        e = line.strip().split(",")
        if e[1]==name and e[3]==sex and e[4]==state:
            #print(e)
            xs.append(int(e[2]))
            xy.append(int(e[5]))
      
print "name=" + name
print "state=" + state                  
print(xs)
print(xy)

plt.plot(xs,xy)
plt.show()