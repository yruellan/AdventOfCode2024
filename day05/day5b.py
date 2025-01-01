
f = open("data.txt", "r")
data = f.read().split("\n\n")
f.close()

# print(data)

orders = [tuple(map(int,x.split("|")[:2])) for x in data[0].split("\n") ]
updates = [list(map(int,x.split(","))) for x in data[1].split("\n")[:-1]]

def is_valid(update):
    for i,x in enumerate(update):
        for j,y in enumerate(update[i+1:]):
            if (y,x) in orders:
                return False
    return True

def median(l):
    """Return the median of the list l"""
    if len(l) % 2 == 0:
        print("mod 2 : 0")
        return (l[len(l)//2] + l[len(l)//2-1]) / 2
    else:
        return l[len(l)//2]

def my_sort(l):
    """Sort the list l"""
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if (l[j],l[i]) in orders:
                l[i], l[j] = l[j], l[i]

s = 0
for update in updates:

    if not is_valid(update):
        my_sort(update)

        m = median(update)
        s += m
        print(update, m)

print(s)