
l = []

f = open("data.txt", "r")
for line in f.readlines():
    x = list(map(int, line.split()))
    l.append(x)

f.close()

nb_valid = 0
for x in l:
    is_inc = True
    is_dec = True

    delta = [x[i+1] - x[i] for i in range(len(x)-1)]
    for e in delta:
        if e < 0:
            is_inc = False
        if e > 0:
            is_dec = False
        if e == 0:
            is_inc = False
            is_dec = False
        if e < -3 or e > 3:
            is_inc = False
            is_dec = False
    if is_inc or is_dec:
        nb_valid += 1
    print(x, is_inc, is_dec)

print(nb_valid)