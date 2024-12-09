from typing import List

f = open("data9.txt", "r")
data = list(map(int, list(f.read())[:-1]))
f.close()


def get_memory(data : List[int]) -> List[int | None]:
    mem : List[int] = []
    for i,x in enumerate(data):
        if i % 2 == 0:
            mem += [i//2]*x
        else :
            mem += [None]*x

    return mem

def sort_memory(data : List[int | None]) -> List[int | None]:
    last_i = len(data) - 1
    i = 0
    while i < last_i:
        if data[last_i] is None:
            last_i -= 1
        elif data[i] is None:
            data[i] = data[last_i]
            data[last_i] = None
            last_i -= 1
            i += 1
        else:
            i += 1
    return data

def checksum(data : List[int | None]) -> int:
    s = 0
    for i,x in enumerate(data):
        if x is None: continue
        else: s += i * int(x)
    return s

mem = get_memory(data)
sorted_mem = sort_memory(mem[:])
mem_sum = checksum(sorted_mem)
# print(data[:100])
# print("".join(map(str,data[:100])))
# print(mem[:200])
# print(sorted_mem[:100])
print(mem_sum)