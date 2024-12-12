from typing import List, Tuple, Set
from dataclasses import dataclass
from enum import Enum

f = open("data12.txt", "r")
# data = list(map(list,f.read().split("\n")))
data = [list(x[:-1]) for x in f.readlines()]
f.close()
N = len(data)
M = len(data[0])

global_visited = set()

class Dir(Enum):
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

@dataclass(frozen=False)
class Side:
    elements: List[Tuple[int, int]]
    direction: int
    
    def __repr__(self) -> str:
        return f"Side({self.elements}, {self.direction})"

    @classmethod
    def from_points(cls, p1: Tuple[int, int], p2: Tuple[int, int]) -> 'Side':
        """Create a Side object from two points"""
        i1, j1 = p1
        i2, j2 = p2
        
        if i1 == i2:  # horizontal side
            direction = Dir.LEFT_RIGHT
        else:  # vertical side
            direction = Dir.UP_DOWN
            
        return cls(i1, j1, i2, j2, direction)

def side(shape: List[Tuple[int, int]]) -> int:
    """Returns the number of sides of the shape by counting unique edges"""
    sides: Set[Side] = set()
    
    # Convert shape points list to sorted list to ensure consistent ordering
    points = sorted(shape)
    
    # Create sides between adjacent points
    for i in range(len(points)):
        p1 = points[i]
        # Connect to next point (wrapping around to first point)
        p2 = points[(i + 1) % len(points)]
        
        # Create side with points in consistent order (smaller coordinates first)
        if p1 < p2:
            sides.add(Side.from_points(p1, p2))
        else:
            sides.add(Side.from_points(p2, p1))
            
    return len(sides)

def dist(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """Returns the Manhattan distance between two points"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def dist_set(l1: List[Tuple[int, int]], l2: List[Tuple[int, int]]) -> int:
    """Returns the minimum Manhattan distance between two sets of points"""
    return min(dist(p1, p2) for p1 in l1 for p2 in l2)

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
            if i2 < 0 or i2 >= N or j2 < 0 or j2 >= M:
                perimeter.append((i2, j2))
                # dir = Dir.LEFT_RIGHT if dir in [0,1] else Dir.UP_DOWN
                sides.append(Side([(i2, j2)], dir))
            elif data[i2][j2] == data[x[0]][x[1]]:
                to_visit.append((i2,j2))
            else :
                perimeter.append((i2, j2))
                # dir = Dir.LEFT_RIGHT if dir in [0,1] else Dir.UP_DOWN
                sides.append(Side([(i2, j2)], dir))
    # print(f"{perimeter = }")
    # print(f"{visited = }")
    # print(sides)
    fusion_side(sides)
    # for s in sides:
    #     print(s)
    print(f"{data[x[0]][x[1]]} : {len(sides)} * {len(visited)} = {len(sides)*len(visited)}")
    return len(sides) * len(visited)

# print(data)
print(N, M)
s = 0
for i in range(N):
    for j in range(M):

        if (i,j) in global_visited: continue
        global_visited.add((i,j))
        # print(f"{id = } {data[i][j] = }")
        s += get_score((i,j))
        # break
    # break

print(s)