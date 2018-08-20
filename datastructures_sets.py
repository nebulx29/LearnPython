# Sets
# unsorted, unique values

s = {"Max", "Matt", "Elon"}
print(s)
s.add("Matt")   # double, ignored
print(s)

if "Matt" in s:
    print("yes")
    
s.remove("Elon")
print(s)
print(len(s))

s2 = set({'Eva', 'Anna'})
for x in s2:
    s.add(x)

print(s)