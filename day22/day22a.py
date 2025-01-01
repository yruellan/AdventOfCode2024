from typing import List, Tuple, Set, Dict
from heapq import heappush, heappop
from lib import memoize, timeit
from time import time
import cProfile
import re

f = open("data.txt")
data = list(map(int,f.readlines()))
f.close()

print(data)

def get_next(n : int) -> int:
    n = mix(n*64,n)
    n = prune(n)

    n = mix(n//32,n)
    n = prune(n)

    n = mix(n*2048,n)
    n = prune(n)

    return n

def mix(n : int, secret : int) -> int:
    return n ^ secret

def prune(secret : int) -> int:
    return secret % 16777216

def main(): 

    l = data[:]
    for _ in range(2000):
        l = map(get_next,l)
    l = list(l)
    print(l)
    print(sum(l))


if __name__ == "__main__": 
    main()