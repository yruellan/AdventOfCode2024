
l1 = []
l2 = []

f = open("data1.txt", "r")
for line in f.readlines():
    x,y = map(int, line.split())
    l1.append(x)
    l2.append(y)

f.close()

s = 0
l1.sort()
l2.sort()
for i in range(len(l1)):
    s += abs(l1[i] - l2[i])

print(s)