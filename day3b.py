import re

f = open("data3.txt", "r")
data = f.read()
f.close()

pattern = r"(mul\((\d+),(\d+)\))|(do\(\))|(don\'t\(\))"
l = re.findall(pattern, data)
print(l)

s = 0
is_act = True
for string, a, b, do, dont in l:
    if a != "" and b != "":
        if is_act:
            s += int(a) * int(b)

    elif do != "":
        is_act = True
    elif dont != "":
        is_act = False

print( s )