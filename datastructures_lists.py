# List
liste = ["abc", "def"]

print(liste[1])
print(liste.append("ghi"))
print(len(liste))
print(liste)

print(liste.pop(-1))   # removes last element
print(liste)

liste.remove("abc")
print(liste)

liste.insert(1, "ghi")
print(liste)
liste.insert(0, "abc")
print(liste)

liste.reverse()
print(liste)
liste.sort()
print(liste)

liste.extend(["jkl", "mno", "abc"])
print(liste)

print(liste.count("abc"))

if "jkl" in liste:
    print("jkl in liste")

