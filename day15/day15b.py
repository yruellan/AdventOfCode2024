from typing import List, Tuple

def get_line(line : str) -> List[str]:
    l = []
    for x in line:
        if x == "#":
            l.append("#")
            l.append("#")
        elif x == "O":
            l.append("[")
            l.append("]")
        elif x == "@":
            l.append("@")
            l.append(".")
        else:
            l.append(".")
            l.append(".")
    return l

f = open("data.txt")
data_, moves = f.read().split("\n\n")
data = [
    get_line(line)
    for line in data_.split("\n")
]
moves = list(moves.replace("\n",""))[:-1]
f.close()

fun_rec_call = []

def get_list_rec(fun):
    global fun_rec_call
    def wrapper(*args):
        fun_rec_call.append(args)
        return fun(*args)
    return wrapper

def get_start_pos(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@":
                return (i, j)
    return None

@get_list_rec
def move(data, x,y, mv, is_update=False) -> bool:
    dx = (mv == "v") - (mv == "^")
    dy = (mv == ">") - (mv == "<")
    # print(f"Pos : {x}, {y} ; {mv = } ; {dx = } ; {dy = } | {is_update = }")

    if data[x+dx][y+dy] == "#":
        return False
    
    if data[x+dx][y+dy] == ".":
        if is_update:
            data[x+dx][y+dy] = data[x][y]
            data[x][y] = "."
        return True
    
    if dx == 0 and data[x+dx][y+dy] in ["[", "]"]:
        if move(data, x+dx, y+dy, mv,is_update):
            if is_update:
                data[x+dx][y+dy] = data[x][y]
                data[x][y] = "."
            return True
        return False
    
    if data[x+dx][y+dy] == "[":
        if move(data, x+dx, y+dy, mv,is_update) and move(data, x+dx, y+dy+1, mv,is_update):
            if is_update:
                data[x+dx][y+dy] = data[x][y]
                data[x+dx][y+dy+1] = data[x][y+1]
                data[x][y] = "."
                data[x][y+1] = "."
            return True
        return False
    if data[x+dx][y+dy] == "]":
        if move(data, x+dx, y+dy, mv,is_update) and move(data, x+dx, y+dy-1, mv,is_update):
            if is_update:
                data[x+dx][y+dy] = data[x][y]
                data[x+dx][y+dy+1] = data[x][y+1]
                data[x][y] = "."
                data[x][y+1] = "."
            return True
    return False

def update(data, x,y, mv) -> bool:
    dx = (mv == "v") - (mv == "^")
    dy = (mv == ">") - (mv == "<")

    if data[x+dx][y+dy] == "#":
        return True
    
    if data[x+dx][y+dy] == ".":
        # print("swapping",x,y,data[x+dx][y+dy], data[x][y])
        data[x+dx][y+dy], data[x][y] = data[x][y], "."
        return True
    
    if dx == 0 and data[x+dx][y+dy] in ["[", "]"]:
        update(data, x+dx, y+dy, mv)
        # print("swapping",x,y,data[x+dx][y+dy], data[x][y])
        data[x+dx][y+dy], data[x][y] = data[x][y], data[x+dx][y+dy]

        return True
    
    if data[x+dx][y+dy] == "[":
        update(data, x+dx, y+dy, mv)
        update(data, x+dx, y+dy+1, mv)
        # print("swapping1",x,y,data[x+dx][y+dy], data[x][y])
        # print("swapping2",x,y,data[x+dx][y+dy+1], data[x][y+1])
        data[x+dx][y+dy], data[x][y] = data[x][y], data[x+dx][y+dy]
        data[x+dx][y+dy+1], data[x][y+1] = data[x][y+1], data[x+dx][y+dy+1]
        return True
    
    if data[x+dx][y+dy] == "]":
        update(data, x+dx, y+dy, mv)
        update(data, x+dx, y+dy-1, mv)
        # print("swapping1",x,y,data[x+dx][y+dy], data[x][y])
        # print("swapping2",x,y,data[x+dx][y+dy-1], data[x][y-1])
        data[x+dx][y+dy], data[x][y] = data[x][y], data[x+dx][y+dy]
        data[x+dx][y+dy-1], data[x][y-1] = data[x][y-1], data[x+dx][y+dy-1]
        return True

    return True

def update2(data, fun_rec_call):
    swapped = set()
    for args in fun_rec_call[::-1]:
        x,y,mv = args[1:4]
        if (x,y) in swapped: continue
        swapped.add((x,y))
        dx = (mv == "v") - (mv == "^")
        dy = (mv == ">") - (mv == "<")

        data[x+dx][y+dy], data[x][y] = data[x][y], data[x+dx][y+dy]

def get_score(data) -> int:
    score = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "[":
                score += i*100 + 1*j
    return score
        
for line in data:
    print("".join(line))
x, y = get_start_pos(data)
for mv in moves:
    fun_rec_call = []
    if move(data, x, y, mv):
        # print([X[1:] for X in fun_rec_call])
        # update(data, x, y, mv)
        update2(data,fun_rec_call)
        # move(data, x, y, mv, True)
        x += (mv == "v") - (mv == "^")
        y += (mv == ">") - (mv == "<")
    print(f"Pos : {x}, {y} ; {mv = }")
    # need_to_raise = False
    # for line in data:
    #     s = "".join(line)
    #     print(s)
    #     if "[." in s: need_to_raise = True
    # if need_to_raise: raise Exception("Found it")
print(get_score(data))