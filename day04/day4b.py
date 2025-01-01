

f = open("data.txt", "r")
data = f.readlines()
f.close()


s = 0
print(f"{len(data) = } {len(data[0]) = }")

def calc_diag_1(data, i, j) -> str:
    return data[i][j]+data[i+1][j+1]+data[i+2][j+2]
def calc_diag_2(data, i, j) -> str:
    return data[i][j+2]+data[i+1][j+1]+data[i+2][j]

for i in range(len(data)-2):
    for j in range(len(data[0])-3):
        
        d1 = calc_diag_1(data, i, j)
        d2 = calc_diag_2(data, i, j)
        diag1 = (d1 == "MAS" or d1 == "SAM")
        diag2 = (d2 == "MAS" or d2 == "SAM")

        # print(i, j, d1,d2)
        if diag1 and diag2:
            s += 1

print(s)