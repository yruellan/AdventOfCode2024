from typing import List, Tuple
from heapq import heappush, heappop

f = open("data.txt", "r")
data : List[List[str]]= list(map(list,f.read().split("\n")))[:-1]
f.close()

# print(data)

def print_data(data):
    for line in data:
        print("".join(line))
    print()

def get_start_pos(data) -> int:
    for i,line in enumerate(data):
        for j,x in enumerate(line):
            if x == "S":
                return (i,j)
    return None

def get_path(data):


    i,j = get_start_pos(data)

    visited = dict()
    to_visit = [(0,i,j,0,tuple())]

    max_d = 0
    paths = []

    while to_visit:
        d,i,j,dir,path = heappop(to_visit)
        # print(f"({i},{j}, {dir}) -> {d}  | {len(to_visit)}")
        if max_d > 0 and d > max_d+100:
            return max_d, paths
        if data[i][j] == "E":
            if max_d == 0:
                max_d = d
                paths.append(path)
            elif d == max_d:
                paths.append(path)
        if (i,j,dir) in visited.keys():
            if visited[(i,j,dir)] < d:
                continue
        visited[(i,j,dir)] = d
        # data[i][j] = "X"

        # if (i,j) == (9,3) : continue

        x = i + (dir == 3) - (dir == 1)
        y = j + (dir == 0) - (dir == 2)
        if data[x][y] != "#":
            heappush(to_visit,(d+1,x,y,dir,path+((x,y),)))
        heappush(to_visit,(d+1000,i,j,(dir+1)%4,path))
        heappush(to_visit,(d+1000,i,j,(dir-1)%4,path))

    print("No path found")
    return max_d, paths
    # raise Exception("No path found")

def main():

    # print_data(data)

    d, paths = get_path(data)
    print(f"Shortest path: {d}")
    print(f"No of paths: {len(paths)}")

    tildes = set()
    for path in paths:
        for x,y in path:
            data[x][y] = "X"
            tildes.add((x,y))

    print(f"Unique tildes: {len(tildes)+1}")

    print_data(data)

if __name__ == "__main__":
    main()