from typing import List, Tuple
from lib import memoize
from time import time

f = open("data.txt", "r")
data = [x.split("-") for x in f.read().splitlines()]
f.close()

"""
It takes 1 minute to execute this script.
"""

table = dict()
for x,y in data:
    if x not in table: table[x] = []
    if y not in table: table[y] = []

    table[x].append(y)
    table[y].append(x)

nodes = set()
for x,y in data:
    nodes.add(x)
    nodes.add(y)

connex_components = dict()

N = 0
t0 = time()

@memoize
def add_to_component(c : Tuple[str]) -> Tuple[str]:
    global N
    N += 1
    if N % 2_500 == 0: print(f"{N = :_} {time() - t0:.2f}")
    max_c = c
    max_len = len(c)
    for y in nodes:
        if y in c: continue
        if all(map(lambda x: y in table[x],c)):
            c2 = add_to_component(tuple(sorted(c + (y,))))
            if len(c2) > max_len:
                max_c = c2
                max_len = len(c2)
    return max_c

c = sorted(add_to_component( tuple() ))
print(c)
print(",".join(c))
print(len(c))
print(f"{N = }")