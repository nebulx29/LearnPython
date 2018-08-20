l = ["Maximilian", "Anna", "Joe"]
l.sort()                                 # in-place sort, d.h. die liste sortiert sich selbst
l_sorted = sorted(l)                     # gibt eine sortierte lsite zurück
print(l)
l.sort(reverse=True)
print(l)

def get_length(item):
    return len(item)

l.sort(key=get_length)     # sort based on function
print(l)