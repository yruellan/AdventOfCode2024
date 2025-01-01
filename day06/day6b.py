from time import time
from typing import List, Tuple


def get_init(data) -> Tuple[int,int]:

    for i,line in enumerate(data):
        for j,letter in enumerate(line):
            if letter == '^':
                data[i][j] = '.'
                return i,j
    return -1,-1

def show(data,path,i0,j0) -> None:
    for i,line in enumerate(data):
        for j,x in enumerate(line):
            if (i,j) == (i0,j0): print("^",end='')
            elif x == 'O': print('O',end='')
            elif x == "#": print("#",end='')
            elif (i,j) in path: print(".",end='')
            else: print(" ",end='')
        print()
    return

def is_valid_obstacle(x,y,i0,j0,data) -> bool:
    dir = 0
    new_path = [[[False,False,False,False] for _ in data[0]] for _ in data]

    while new_path[i0][j0][dir] == False:
        new_path[i0][j0][dir] = True
        if data[i0][j0] == "#" or (i0,j0) == (x,y):
            i0 -= (dir == 2) - (dir == 0)
            j0 -= (dir == 1) - (dir == 3)
            dir = (dir + 1) % 4
            i0 += (dir == 2) - (dir == 0)
            j0 += (dir == 1) - (dir == 3)
        else:
            i0 += (dir == 2) - (dir == 0)
            j0 += (dir == 1) - (dir == 3)
        if i0 < 0 or i0 >= len(data) or j0 < 0 or j0 >= len(data[0]):
            return False
    return True

def get_path(i0,j0,data) -> List[Tuple[int,int]]:
    path = []
    dir = 0

    while True:
        if i0 < 0 or i0 >= len(data) or j0 < 0 or j0 >= len(data[0]):
            break
        if data[i0][j0] == '.':
            path.append((i0,j0))
            i0 += (dir == 2) - (dir == 0)
            j0 += (dir == 1) - (dir == 3)
        elif data[i0][j0] == '#' or data[i0][j0] == 'O':
            i0 -= (dir == 2) - (dir == 0)
            j0 -= (dir == 1) - (dir == 3)
            dir = (dir + 1) % 4
            i0 += (dir == 2) - (dir == 0)
            j0 += (dir == 1) - (dir == 3)

    print("Path found")
    return path

def main() -> None:

    f = open("data.txt", "r")
    data = [list(x[:-1]) for x in f.readlines()]
    f.close()

    I0,J0 = get_init(data)
    path = get_path(I0,J0,data)

    obstacles_for_loop = set()

    t0 = time()

    for index,(x,y) in enumerate(path[1:]):
        
        if is_valid_obstacle(x,y,I0,J0,data):
            obstacles_for_loop.add((x,y))

        if index % 500 == 0:
            print(f"{100.0*index/len(path):.2f}%")

        
    print(f"end in {time()-t0:.2f}s")
    print(len(obstacles_for_loop))
    # 1836 in 14.41s (vs 23.84s)

if __name__ == "__main__":
    main()