

f = open("data.txt", "r")
data = f.readlines()
f.close()


s = 0
print(f"{len(data) = } {len(data[0]) = }")

# Horizontal
for i in range(len(data)):
    for j in range(len(data[0])-3):
        # print(i,j, data[i][j]+data[i][j+1]+data[i][j+2]+data[i][j+3])
        if data[i][j] == "X" and data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S":
            s += 1
            # print(i, j, 1)
        if data[i][j] == "S" and data[i][j+1] == "A" and data[i][j+2] == "M" and data[i][j+3] == "X":
            s += 1
            # print(i, j, 2)

# Vertical
for i in range(len(data)-3):
    for j in range(len(data[0])):
        # print(i,j, data[i][j]+data[i+1][j]+data[i+2][j]+data[i+3][j])
        if data[i][j] == "X" and data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
            s += 1
            # print(i, j, 3)
        if data[i][j] == "S" and data[i+1][j] == "A" and data[i+2][j] == "M" and data[i+3][j] == "X":
            s += 1
            # print(i, j, 4)

# Diagonal
for i in range(len(data)-3):
    for j in range(len(data[0])-3):
        # print(i,j, data[i][j]+data[i+1][j+1]+data[i+2][j+2]+data[i+3][j+3])
        if data[i][j] == "X" and data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
            s += 1
            # print(i, j, 5)
        if data[i][j] == "S" and data[i+1][j+1] == "A" and data[i+2][j+2] == "M" and data[i+3][j+3] == "X":
            s += 1
            # print(i, j, 6)

        if data[i][j+3] == "X" and data[i+1][j+2] == "M" and data[i+2][j+1] == "A" and data[i+3][j] == "S":
            s += 1
            # print(i, j, 7)
        if data[i][j+3] == "S" and data[i+1][j+2] == "A" and data[i+2][j+1] == "M" and data[i+3][j] == "X":
            s += 1
            # print(i, j, 8)

print(s)