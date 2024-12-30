
f = open("data6.txt", "r")
data = [list(x[:-1]) for x in f.readlines()]
f.close()

# print(data)

i0=0
j0=0
dir = 0
for i,line in enumerate(data):
    for j,letter in enumerate(line):
        if letter == '^':
            i0 = i
            j0 = j
            data[i][j] = '.'
            break

path = []

while True:
    if i0 < 0 or i0 >= len(data) or j0 < 0 or j0 >= len(data[0]):
        break
    if data[i0][j0] == '.':
        path.append((i0,j0))
        i0 += (dir == 2) - (dir == 0)
        j0 += (dir == 1) - (dir == 3)
    elif data[i0][j0] == '#':
        i0 -= (dir == 2) - (dir == 0)
        j0 -= (dir == 1) - (dir == 3)
        dir = (dir + 1) % 4
        i0 += (dir == 2) - (dir == 0)
        j0 += (dir == 1) - (dir == 3)

for i,line in enumerate(data):
    print("".join([
        "#" if x == '#' else ("." if (i,j) in path else " ")
        for j,x in enumerate(line)
    ]))
# print(len(path))
print(len(set(path)))