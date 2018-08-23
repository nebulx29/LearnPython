from Crawler import Crawler
import csv

URL = "http://python.beispiel.programmierenlernen.io/index.php"
SEP = ";"

cr = Crawler(URL)
#articles = cr.fetch_generator()

print("=== RESULTS BEGIN ===")
i = 0
for a in cr.fetch_generator():
    print (a)
    i = i + 1
    if (i>=14):
        break
print("=== RESULTS END ===")




#liste = []
#for a in articles:
#    liste.append(a.get_as_list())

#csv.register_dialect('mystyle', delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

#with open("articles.csv", "w", newline='') as f:
#    writer = csv.writer(f, 'mystyle')
#    writer.writerows(liste)
