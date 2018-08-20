### QUEUE ###

import queue

q = queue.Queue()

q.put("abc")
q.put("def")
q.put("ghi")
q.put("jkl")
q.put("mno")

print(q.qsize())

while not q.empty():
    print(q.get())

print(q.qsize())    


### PRIORITY QUEUE ###

pq = queue.PriorityQueue()
pq.put((10, "Max"))
pq.put((15, "Anna"))
pq.put((5, "Joe"))
pq.put((20, "some VIP"))

while not pq.empty():
    print(pq.get())
    
    
    
    
    
    
#### Example

text = "A A A A A A B B C C C C C C C C D D D D E E E"
d = {}
for c in text.split(" "):
    if (c in d):
        d[c] = d[c] + 1
    else:
        d[c] = 1    
    
print(d)

pq1 = queue.PriorityQueue()
for c in d.keys():
    pq1.put((-d[c], c))
    
print(pq1)
while not pq1.empty():
    print(pq1.get())
    