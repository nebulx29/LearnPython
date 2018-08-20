turm = 4

for i in range(2,9):
    print(str(i) + ": " + str(turm))
    turm = turm * i
for i in range(2,9):
    turm = int(turm / i)        
    print(str(i) + ": " + str(turm))
