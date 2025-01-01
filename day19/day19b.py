from lib import memoize

f = open("data.txt")
data = f.read().splitlines()
towels = data[0].split(", ")
patterns = data[2:]
f.close()

@memoize
def nb_possible(pattern) -> int:
    # print(" is poss",pattern)
    if pattern == "": return 1
    n = 0
    for towel in towels:
        if pattern.startswith(towel):
            n += nb_possible(pattern[len(towel):])
    return n

# print(towels)
n = 0
for i,pattern in enumerate(patterns):
    k = nb_possible(pattern)
    print(pattern, k, f"({i+1}/{len(patterns)})%")
    n += k
print(n)