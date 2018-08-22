# test01

import random

def lentry(i, liste1, liste2):
	x1 = random.randint(0, len(liste1)-1)
	x2 = random.randint(0, len(liste2)-1)
	print(str(i) + ": " + liste1[x1] + str(liste2[x2]))

liste1 = ["a", "b", "d", "f"]
liste2 = [4, 3, 8, 6]

for i in range(0,9): 
	lentry(i, liste1, liste2)
	