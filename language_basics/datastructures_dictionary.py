# Dictionary
d = {"4711": "Joe", "4718": "Susi"}
print(d)

d["4999"] = "Max"
print(len(d))
print(d)

del(d["4711"])
print(d)

d["4711"] = "Joe"

print(d.keys())
print(d.values())
print(d.items())

print(d.get("4711"))

r = d.pop("4718")
print(r)
print(d)

a_key = "4711"
if a_key in d:
    print("key " + a_key + " contained")
    print(str(a_key) + "=" + d[a_key])
    
    
    