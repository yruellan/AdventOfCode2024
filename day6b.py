from time import time

f = open("data6.txt", "r")
data = [list(x[:-1]) for x in f.readlines()]
f.close()

i0=0
j0=0
dir = 0

for i,line in enumerate(data):
    for j,letter in enumerate(line):
        if letter == '^':
            i0 = i
            j0 = j
            data[i][j] = '.'
            break

init = (i0,j0,dir)

def move(i0,j0,dir):
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
    return i0,j0,dir
def move2(i0,j0,dir,x,y):
    if data[i0][j0] == "#" or (i0,j0) == (x,y):
        i0 -= (dir == 2) - (dir == 0)
        j0 -= (dir == 1) - (dir == 3)
        dir = (dir + 1) % 4
        i0 += (dir == 2) - (dir == 0)
        j0 += (dir == 1) - (dir == 3)
    else:
        i0 += (dir == 2) - (dir == 0)
        j0 += (dir == 1) - (dir == 3)
    return i0,j0,dir

def show(data,path):
    for i,line in enumerate(data):
        for j,x in enumerate(line):
            if (i,j) == init[:2]: print("^",end='')
            elif x == 'O': print('O',end='')
            elif x == "#": print("#",end='')
            elif (i,j) in path: print(".",end='')
            else: print(" ",end='')
        print()
    return

path = []

while True:
    if i0 < 0 or i0 >= len(data) or j0 < 0 or j0 >= len(data[0]):
        break
    i0,j0,dir = move(i0,j0,dir)

print("Path found")

obstacles_for_loop = set()

t0 = time()
for index,(x,y) in enumerate(path[1:]):

    i0,j0,dir = init
    new_path = [[[False,False,False,False] for _ in data[0]] for _ in data]

    while new_path[i0][j0][dir] == False:
        new_path[i0][j0][dir] = True
        i0,j0,dir = move2(i0,j0,dir,x,y)
        if i0 < 0 or i0 >= len(data) or j0 < 0 or j0 >= len(data[0]):
            break
    else:
        # Loop found
        print(
            f"Done : ({x} {y}), {index:7} {len(path)} | ",
            f"{100.0*index/len(path):.2f}%",
            f" in {time()-t0:.2f}s -> approx ",
            f"{(time()-t0)*(len(path))/index if index > 0 else 0:.2f}s"
        )
        obstacles_for_loop.add((x,y))

    

print(len(obstacles_for_loop))