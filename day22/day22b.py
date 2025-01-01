from typing import List, Tuple, Set, Dict
from heapq import heappush, heappop
from lib import memoize, timeit
from time import time
import cProfile
import re

f = open("data.txt")
data = list(map(int,f.readlines()))
f.close()


# @memoize
def get_next(n : int) -> int:
    n = (n*64) ^ n
    n %= 16_777_216

    n = (n//32) ^ n
    n %= 16_777_216

    n = (n*2048) ^ n
    n %= 16_777_216

    return n

values = dict()

def get_sequence(id,n,N):
    l = [n%10]
    secret = n
    for i in range(2_000):
        secret = get_next(secret)
        l.append(secret%10)
    
    for i in range(4,len(l)):
        seq = tuple(l[i-k]-l[i-k-1] for k in range(4))
        if seq not in values.keys():
            values[seq] = [None]*N
        # elif values[seq][id] != 0:
        #     print("change",values[seq][id],l[i]%10)
        if values[seq][id] is None:
            values[seq][id] = l[i]

def calc(val):
    return sum(filter(lambda x: x is not None,val))

def main(): 

    print("data",data[:10])

    t0 = time()

    N = len(data)
    print(f"{N = }")
    for i,x in enumerate(data):
        get_sequence(i,x,N)

    t1 = time()

    print(f"calc max in {t1-t0:.2f}s")
    max_key = max(values.keys(), key=lambda x: calc(values[x]))
    print(f"found max in {time()-t1:.2f}s")
    print(f"Took {time()-t0:.2f}s\n")
    
    # for k in [max_key,(3,-1,1,-2),(2,1,0,0)]:
    for k in [max_key]:
        print(f"{k = } : \t{calc(values.get(k,[None]*N))}")

    # 1891 ± -> if use last value
    # (2,1,0,0) : 1898
    # get_sequence(123)

if __name__ == "__main__": 
    main()