import re


sentence = "ich habe 30 hunde mit 120 beinen und 60 augen"
print(re.findall("[0-9]+", sentence))
print(re.search("[0-9]+", sentence))


svnr = "4711 14082003"
print(re.findall("^[0-9]{4}", svnr))
print(re.findall(" [0-9]{2}", svnr))