
class Person():
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return "" + self.fname + " " + self.lname
    

class Student(Person):
    
    def __init__(self, mnr, fname, lname):
        super().__init__(fname, lname)
        self.mnr = mnr
        
    def __str__(self):
        return super().__str__() + ", " + self.mnr


#s1 = Student("4711", "Max", "Mueller")
#print(s1)

l1 = [
    Student("4711", "Max", "Mueller"),
    Person("Joe", "Hann"),
    Student("3981", "Sue", "Sanna")
    ]
    
for x in l1:
    print(x)