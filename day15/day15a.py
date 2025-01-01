from typing import List, Tuple

f = open("data.txt")
data, moves = f.read().split("\n\n")
data = list(map(list, data.split("\n")))
moves = list(moves.replace("\n",""))[:-1]
f.close()

# print(data)
# print(moves)

def get_start_pos(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@":
                return (i, j)
    return None

def move(data, x,y, mv):
    dx = (mv == "v") - (mv == "^")
    dy = (mv == ">") - (mv == "<")

    if data[x+dx][y+dy] == "#": return None
    if data[x+dx][y+dy] == ".":
        
        data[x+dx][y+dy] = data[x][y]
        data[x][y] = "."
        return (x+dx, y+dy)
    if data[x+dx][y+dy] == "O":
        if move(data, x+dx, y+dy, mv) is not None:

            data[x+dx][y+dy] = data[x][y]
            data[x][y] = "."
            return (x+dx, y+dy)
        else:
            return None
        
def get_score(data) -> int:
    score = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "O":
                score += i*100 + 1*j
    return score
        
for line in data:
    print("".join(line))
x, y = get_start_pos(data)
for mv in moves:
    r = move(data, x, y, mv)
    if r is not None:
        x, y = r
print(f"Pos : {x}, {y} ; {mv = }")
for line in data:
    print("".join(line))
print(get_score(data))