
f = open("data.txt", "r")
# data = list(map(list,f.read().split("\n")))
data = [list(x[:-1]) for x in f.readlines()]
f.close()
N = len(data)
M = len(data[0])

global_visited = set()

def get_score(x):
    perimeter = list()
    visited = set()
    to_visit = [x]
    
    while to_visit:
        y = to_visit.pop()
        if y in visited: continue
        visited.add(y)
        global_visited.add(y)
        i,j = y
        for dir in range(4):
            i2 = i + (dir == 0) - (dir == 1)
            j2 = j + (dir == 2) - (dir == 3)
            if i2 < 0 or i2 >= N or j2 < 0 or j2 >= M:
                perimeter.append((i2, j2))
            elif data[i2][j2] == data[x[0]][x[1]]:
                to_visit.append((i2,j2))
            else : perimeter.append((i2, j2))
    # print(f"{perimeter = }")
    # print(f"{visited = }")
    print(f"{len(perimeter)} * {len(visited)} = {len(perimeter) * len(visited)}")
    return len(perimeter) * len(visited)

# print(data)
print(N, M)
s = 0
for i in range(N):
    for j in range(M):

        if (i,j) in global_visited: continue
        global_visited.add((i,j))
        # print(f"{id = } {data[i][j] = }")
        s += get_score((i,j))

print(s)