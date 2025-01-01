from typing import List, Tuple, Set
from dataclasses import dataclass
from enum import Enum

f = open("data.txt", "r")
data = [list(x[:-1]) for x in f.readlines()]
f.close()
N = len(data)
M = len(data[0])

global_visited : Set[Tuple[int, int]] = set()

@dataclass
class Side:
    elements: List[Tuple[int, int]]
    direction: int
    
    def __repr__(self) -> str:
        return f"Side({self.elements}, {self.direction})"

def dist_set(l1: List[Tuple[int, int]], l2: List[Tuple[int, int]]) -> int:
    """Returns the minimum Manhattan distance between two sets of points"""
    return min(
        abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) 
        for p1 in l1 for p2 in l2
    )

def fusion_side(sides: List[Side]) -> None:

    for i in range(len(sides)):
        j = i+1
        while j < len(sides):
            if sides[i].direction != sides[j].direction:
                j += 1
            elif dist_set(sides[i].elements, sides[j].elements) == 1:
                sides[i].elements += sides[j].elements
                sides[j: j+1] = []
                j = i+1
            else:
                j += 1

def get_score(x):
    perimeter = list()
    visited = set()
    to_visit = [x] 
    sides = []
    
    while to_visit:
        y = to_visit.pop()
        if y in visited: continue
        visited.add(y)
        global_visited.add(y)
        i,j = y
        for dir in range(4):
            i2 = i + (dir == 0) - (dir == 1)
            j2 = j + (dir == 2) - (dir == 3)
            if (i2 >= 0 and i2 < N and j2 >= 0 and j2 < M and
                data[i2][j2] == data[x[0]][x[1]]):
                to_visit.append((i2,j2))
            else :
                perimeter.append((i2, j2))
                sides.append(Side([(i2, j2)], dir))
    fusion_side(sides)
    print(f"{data[x[0]][x[1]]} : {len(sides)} * {len(visited)} = {len(sides)*len(visited)}")
    return len(sides) * len(visited)

def main():
    s = 0
    for i in range(N):
        for j in range(M):

            if (i,j) in global_visited: continue
            global_visited.add((i,j))
            s += get_score((i,j))
    
    print(s)

if __name__ == "__main__":
    main()