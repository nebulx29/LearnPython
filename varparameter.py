def multi_print(number = 3, word = "Hallo"):
    for i in range(0, number):
        print(str(i) + " " + word)
        
multi_print(1, "Hallo")
print("--")
multi_print()
print("--")
multi_print(2)
print("--")
multi_print(word = "Welt")
print("--")
multi_print(word = "Welt", number = 5)
print("--")

