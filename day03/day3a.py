import re

f = open("data3.txt", "r")

data = f.read()
f.close()

pattern = r"mul\((\d+),(\d+)\)"
l = re.findall(pattern, data)
print(l)

print( sum([int(a) * int(b) for a, b in l]) )