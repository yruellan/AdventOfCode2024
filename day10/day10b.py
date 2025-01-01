from time import time
from heapq import heappop,heappush

f = open("data.txt", "r")
data = [list(map(int,x[:-1])) for x in f.readlines()]
f.close()

# for line in data:
#     print("".join(map(str,line)))

zeros = [(i,j) for i,line in enumerate(data) for j,x in enumerate(line) if x == 0]

# print(zeros)

def calc_path(i0,j0):
    finals = set()
    finals_path = []

    visited = set()
    to_visit = [(0,i0,j0,((i0,j0),))]
    while to_visit:
        h,x,y,path = heappop(to_visit)

        if (x,y,path) in visited: continue
        visited.add((x,y,path))
        if data[x][y] == 9:
            finals.add((x,y))
            finals_path.append(path)
            continue

        for dir in range(4):
            dx = (dir == 2) - (dir == 0)
            dy = (dir == 1) - (dir == 3)
            if dx == 0 and dy == 0: continue
            if x+dx < 0 or x+dx >= len(data): continue
            if y+dy < 0 or y+dy >= len(data[0]): continue
            new_path = path + ((x+dx,y+dy),)
            if (x+dx,y+dy,new_path) in visited: continue
            if data[x+dx][y+dy] == h+1:
                heappush(to_visit,(h+1,x+dx,y+dy,new_path))

    return finals, finals_path

s = 0
for i0,j0 in zeros:
    finals,finals_path = calc_path(i0,j0)
    # print(len(finals),len(finals_path))
    # for path in finals_path:
    #     print(path)
    s += len(finals_path)
print(f"Total: {s}")