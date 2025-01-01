
f = open("data.txt")
data = f.read().splitlines()
towels = data[0].split(", ")
patterns = data[2:]
f.close()

def is_possible(towels, pattern):
    # print(" is poss",pattern)
    if pattern == "": return True
    for towel in towels:
        if pattern.startswith(towel) and is_possible(towels,pattern[len(towel):]):
            return True
    return False

print(towels)
n = 0
for pattern in patterns:
    is_poss = is_possible(towels, pattern)
    print(pattern, is_poss)
    if is_poss: n += 1
print(n)