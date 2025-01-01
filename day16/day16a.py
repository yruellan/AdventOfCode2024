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

    visited = set()
    to_visit = [(0,i,j,0,tuple())]

    while to_visit:
        d,i,j,dir,path = heappop(to_visit)
        # print(f"({i},{j}, {dir}) -> {d}")
        if data[i][j] == "E":
            for x,y in path:
                data[x][y] = "X"
            return d
        if (i,j,dir) in visited: continue
        visited.add((i,j,dir))
        # data[i][j] = str(dir)
        # if dir == 0: data[i][j] = ">"
        # elif dir == 1: data[i][j] = "^"
        # elif dir == 2: data[i][j] = "<"
        # elif dir == 3: data[i][j] = "v"

        x = i + (dir == 3) - (dir == 1)
        y = j + (dir == 0) - (dir == 2)
        if data[x][y] != "#":
            heappush(to_visit,(d+1,x,y,dir,path+((x,y),)))
        heappush(to_visit,(d+1000,i,j,(dir+1)%4,path))
        heappush(to_visit,(d+1000,i,j,(dir-1)%4,path))

    return None

def main():

    # print_data(data)

    print(get_path(data))

    # print_data(data)

if __name__ == "__main__":
    main()