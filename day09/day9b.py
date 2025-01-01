from typing import List, Tuple
from copy import deepcopy


f = open("data.txt", "r")
data = list(map(int, list(f.read())[:-1]))
f.close()

def show(data : List[int | None]) -> str:
    return ("".join([str(x) if x is not None else "." for x in data]))

def show2(data : List[List[int | None]]) -> str:
    return ("".join([str(x[0])*x[1] if x[0] is not None else "."*x[1] for x in data]))

def get_mem(data : List[int]) -> List[List[int | None]]:
    mem : List[List[int,int]] = []
    for i,x in enumerate(data):
        if i % 2 == 0:
            mem += [[i//2,x]]
        else :
            mem += [[None,x]]

    return mem

def sort_mem(data : List[List[int | None]]) -> List[List[int | None]]:

    n = max([x[0] for x in data if x[0] is not None])

    j = len(data) - 1

    while n >= 0:

        j = [x[0] for x in data].index(n)
        
        # print(n,data[j],show2(data))
        for i in range(j):
            if data[i][0] is None and data[i][1] >= data[j][1]:

                new_val = [data[j], [None,data[i][1] - data[j][1]]]
                data[j] = [None,data[j][1]]
                data[i:i+1] = new_val
                break

        n -= 1
        
    return data

def convert(data : List[List[int | None]]) -> List[int | None]:
    new_data = []
    for x,n in data:
        new_data += [x]*n
    return new_data

def checksum(data : List[int | None]) -> int:
    s = 0
    for i,x in enumerate(data):
        if x is None: continue
        else: s += i * int(x)
    return s

mem = get_mem(data)
sorted_mem = sort_mem(deepcopy(mem))
s_mem = convert(sorted_mem)
mem_sum = checksum(s_mem)
# print(f"{show(data) = }")
# print(f"{show2(mem) = }")
# print(f"{show2(sorted_mem) = }")
# print(f"{show(s_mem) = }")
print(f"{mem_sum = }")