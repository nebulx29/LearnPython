import csv

csv.register_dialect('myformat', delimiter=';', quoting=csv.QUOTE_NONNUMERIC, skipinitialspace=True, quotechar='"')
print(csv.list_dialects())

x = []
y = []

with open("network_inputs_draft4.csv") as f:
    reader = csv.reader(f, 'myformat')
    for row in reader:
        x.append(row[0])
        y.append(row[6])
        
print(x)
print(y)