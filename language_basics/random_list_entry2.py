import random

part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombre,"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]

output = []
output.append(part1[random.randint(0,len(part1)-1)])
output.append(part2[random.randint(0,len(part2)-1)])
output.append(part3[random.randint(0,len(part3)-1)])
output.append(part4[random.randint(0,len(part4)-1)])

print (" ".join(output))