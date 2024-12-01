
l1 = []
l2 = []

f = open("data1.txt", "r")
for line in f.readlines():
    x,y = map(int, line.split())
    l1.append(x)
    l2.append(y)

f.close()

s = 0
for x in l1:
    # print(x,x*l2.count(x))
    s += x*l2.count(x)

print(s)