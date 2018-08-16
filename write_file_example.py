#file = open("data.csv", "r")
#for line in file:
#    print(line)
    
with open("output.csv", "a") as fileout:
    fileout.write("Hello World")
    fileout.close()