f = open("data.txt", "r")
data = [
    list(x.strip())
    for x in f.readlines()
]
f.close()

antenna = [
    (i,j,c)
    for i,l in enumerate(data)
    for j,c in enumerate(l)
    if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
]

antinode = [
    [False for _ in x]
    for x in data
]

for (i,j,a) in antenna:
    for (x,y,b) in antenna:
        if a != b or (i == x and j == y):
            continue

        x2 = 2*x - i
        y2 = 2*y - j
        if 0 <= x2 < len(data) and 0 <= y2 < len(data[0]):
            antinode[x2][y2] = True

n = 0
for i in range(len(data)):
    # s = ""
    for j in range(len(data[0])):
        if antinode[i][j]:
            # s += "#"
            n += 1
    #     else:
    #         s += data[i][j]
    # print(s)
print(n)