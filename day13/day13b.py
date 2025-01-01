f = open("data.txt", "r")
data = []
for x in f.read().split("\n\n"):
    a,b,c = x.split("\n")[:3]
    a = a.split("X+")[1].split(", Y+")
    b = b.split("X+")[1].split(", Y+")
    c = c.split("X=")[1].split(", Y=")
    data.append([
        int(a[0]), int(a[1]), int(b[0]), int(b[1]), int(c[0]), int(c[1])
    ])
f.close()

# print(data)

def get_cost(xa,ya,xb,yb,X,Y) -> int:
    # n*xA + m*xB = X
    # n*ya + m*yb = Y

    X += 10000000000000
    Y += 10000000000000

    det = xa*yb - xb*ya
    if det == 0:
        n = X // xa
        m = Y // ya
        if (n*xa, n*ya) != (X, Y) or (m*xb, m*yb) != (X, Y):
            return 0
        # return max(n, m)
        return min(3*n, 1*m)
    
    n = (X*yb - Y*xb) / det
    m = (Y*xa - X*ya) / det
    if n != int(n) or m != int(m):
        # print(f"Not integer {n = } {m = }")
        return 0
    # print(f"{n = } {m = }")
    # return max(n, m)
    return 3*abs(int(n)) + 1*abs(int(m))

l = []
for i in range(len(data)):
    c = get_cost(*data[i])
    l.append(c)
    print(f"{i = } : {c}")
print(f"{sum(l) = }")