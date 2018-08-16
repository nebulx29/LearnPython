d = {"VIA": "Wien", "BER" : "Berlin" }
print(d)
print(d.get("VIA"))   # get value
print(d.keys())       # get all keys
print(d.values())     # get all values

d["SGN"] = "Saigon"   # add key/value
print(d)

d.update({"FRA": "Frankfurt"})   # add key/value
print(d)

d.update({"LAX": "Los Angeles", "LHR": "London Heathrow"})
print(d)

print(d.has_key("LAX"))
print("LAX" in d)


r = d.pop("LHR")     # removes 'idx' from dict and returns value
print(d)