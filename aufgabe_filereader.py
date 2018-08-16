class FileReader():
    def __init__(self, filename):
        self.filename = filename
        
    def lines(self):
        datafile = open(self.filename, "r")
        r = []
        for l in datafile:
            r.append(l)
        return r
    
class CSVFileReader(FileReader):
    def __init__(self, filename, seperator):
        super().__init__(filename)
        self.seperator = seperator
        
    def lines(self):
        # langform
        #ls = super().lines()
        #r = []
        #for l in ls:
        #    r.append(l.strip().split(self.seperator))
        #return r
        # kurzform als list comprehension
        
        return [line.strip().split(self.seperator) for line in super().lines()]
    



f1 = CSVFileReader("data.csv", ";")
f2 = FileReader("data.csv")
#print(f.lines())

print(type(f1))
print(type(f2))

if (type(f1) == CSVFileReader):
    print("f1 is of type CSVFileReader")    # keine Vererbung, nur exakter Typ
    
if (isinstance(f1), CSVFileReader):
    print("f1 is instance of FileReader")   # berücksichtigt Vererbung
 



