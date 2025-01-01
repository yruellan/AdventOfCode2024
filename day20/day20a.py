from typing import List, Tuple
from heapq import heappush, heappop

f = open("data.txt")
data = f.read().splitlines()
f.close()


def get_init() -> Tuple[int,int]:
    for i,line in enumerate(data):
        for j,c in enumerate(line):
            if c == 'S':
                return i,j
    raise ValueError("No start position found")
            
def get_path(pos = get_init()) -> List[Tuple[int,int]]:

    visited = set()
    to_visit = [(0, pos, (pos,))]

    while to_visit:
        steps, (i,j), path = heappop(to_visit)
        
        if data[i][j] == 'E': return list(path)
        if (i,j) in visited:  continue
        visited.add((i,j))

        for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if 0 <= x < len(data) and 0 <= y < len(data[0]) and data[x][y] != '#':
                heappush(to_visit, (steps+1, (x,y), path+((x,y),)))

    raise ValueError("No path found")
    return []

def show_path(path: List[Tuple[int,int]]) -> None:
    for i,line in enumerate(data):
        for j,c in enumerate(line):
            if (i,j) in path and c == "#":
                print("O", end="")
            elif (i,j) in path:
                print(".", end="")
            elif c == "#":
                print("#", end="")
            else:
                print(" ", end="")
        print()
    return

def main() -> None:
    path = get_path()

    deltas = []
    for i,p1 in enumerate(path):
        for j,p2 in enumerate(path):
            if j <= i: continue
            if abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) <= 2:
                # if j>10+i:
                #     print(f"{p1} {p2} -> {i} {j} = {j-i-2}")
                if j-i-2 >= 100:
                    deltas.append(j-i-2)


    # show_path(path)
    print(f"{len(deltas) = }")

if __name__ == "__main__":
    main()