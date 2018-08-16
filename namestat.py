# CSV: 0   1     2     3    4      5
# CSV: ID, Name, Jahr, Sex, State, Count
name = "Max"
sex = "M"
state = "NY"
year_from = 1950
year_to = 2000
count = 0

with open("names.csv","r") as f:
    for line in f:
        e = line.strip().split(",")
        if e[1]==name and e[3]==sex and e[4]==state and int(e[2])>=year_from and int(e[2])<=year_to:
            count = count + int(e[5])

print("Name '" + name + "' has been given " + str(count) + " times between " + str(year_from) + " and " + str(year_to) + " in state of " + state)
