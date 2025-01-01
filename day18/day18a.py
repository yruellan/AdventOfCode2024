from typing import List, Tuple
from heapq import heappush, heappop

f = open("data.txt")
data = [list(map(int, line.split(","))) for line in f.read().splitlines()]
f.close()


objective = (70,70)
# objective = (6,6)

is_corrupted = [
    [False for _ in range(objective[0]+1)] for _ in range(objective[1]+1)
]

for x,y in data[:1024]:
    is_corrupted[y][x] = True


def dist(a: List[int], b: List[int]) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def get_path(pos) -> Tuple[int, Tuple[Tuple[int]]]:


    visited = set()
    queue = [(0.0, 0, pos,(pos,))]

    while queue:
        _, steps, pos, path = heappop(queue)

        if pos in visited: continue
        visited.add(pos)
        if pos == objective: return steps,path

        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_pos = (pos[0]+dx, pos[1]+dy)
            if new_pos[0] < 0 or new_pos[0] > objective[0]: continue
            if new_pos[1] < 0 or new_pos[1] > objective[1]: continue
            if is_corrupted[new_pos[1]][new_pos[0]]: continue
            heappush(queue, (dist(new_pos, objective)+steps+1, steps+1, new_pos, path+(new_pos,)))
    return -1,()

steps, path = get_path((0,0))

# print(is_corrupted[0][0])
# for i,line in enumerate(is_corrupted):
#     print( "".join(
#         ["#" if x else ("." if (j,i) in path else " ")
#         for j,x in enumerate(line)]
#     ))
print(steps)