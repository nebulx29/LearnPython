liste = [3, 6, 8, 2, 1]
print(liste)
le = liste.pop()  # removes from end
print(liste)
liste.append(11)  # add at end
print(liste)
liste.remove(6)   # removes with value
print(liste)
print(liste.index(8))  # returns index of value
liste.append(15)       # add at end
print(liste)   
liste.insert(0, 21)    # add at position 
print(liste)

liste = liste + [ 9, 99, 999]   # add liste to liste
print(liste)
del liste[0]      # delete item at position
print(liste)

print(liste[3:6])  # slice from index 3 to 6
print(liste[:])    # slice all
print(liste[0:-1]) # slice from first to one before last
print(liste[-1])   # get last
print(liste[-2])   # get one before last
print(liste[-3:-1])

print("abcdefghij"[0:5])    # print first 5 chars
print("abcdefghij"[-3:])    # print last three chars