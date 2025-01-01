f = open("data.txt", "r")
data = []
for x in f.readlines():
    a = x[2:].split(" v=")[0].split(",")
    b = x[2:].split(" v=")[1].split(",")
    data.append([
        int(a[0]), int(a[1]), int(b[0]), int(b[1])
    ])
f.close()

N = 101
M = 103
# N = 11
# M = 7
# data = [[2,4,2,-3]]

def print_grid(N,M,data):
    positions = [[x[0],x[1]] for x in data]
    for i in range(M):
        for j in range(N):
            n = positions.count([j,i])
            if n == 0:
                print(" ", end="")
            else:
                print(n, end="")
        print()

def update(data):
    for i in range(len(data)):
        data[i][0] = (data[i][0] + data[i][2]) % N
        data[i][1] = (data[i][1] + data[i][3]) % M

def get_score(data):
    positions = [
        [x[0],x[1]]
        for x in data
        if x[0] != N // 2 and x[1] != M // 2
    ]
    quadrants = [[0,0],[0,0]]
    for x,y in positions:
        if x < N // 2:
            if y < M // 2:
                quadrants[0][0] += 1
            else:
                quadrants[0][1] += 1
        else:
            if y < M // 2:
                quadrants[1][0] += 1
            else:
                quadrants[1][1] += 1
    return quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1]

print_grid(N,M,data)
for laps in range(7_000):
    update(data)
    print(f"{laps = }")
    print_grid(N,M,data)
# print(get_score(data))