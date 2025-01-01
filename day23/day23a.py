
f = open("data.txt", "r")
data = [x.split("-") for x in f.read().splitlines()]
f.close()


table = dict()
for x,y in data:
    if x not in table: table[x] = []
    if y not in table: table[y] = []

    table[x].append(y)
    table[y].append(x)

triples = set()

for k,l in table.items():
    if not k.startswith("t"): continue

    for i,x in enumerate(l):
        for y in l[i+1:]:
            if y in table[x]:
                t = [k, x, y]
                triples.add(tuple(sorted(t)))
for t in sorted(triples):
    print(t)
print(len(triples))