
l = []

f = open("data.txt", "r")
for line in f.readlines():
    x = list(map(int, line.split()))
    l.append(x)

f.close()

def is_safe(x):
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

        if not is_inc and not is_dec:
            return False

    return is_inc or is_dec

nb_valid = 0
for x in l:

    # print(x,end=" : ")
    
    for i in range(len(x)):
        x2 = [x[j] for j in range(len(x)) if j != i]

        if is_safe(x2):
            nb_valid += 1
            # print(x2,"s",end=" ; ")
            # print(x, "safe")
            break
    #     else:
    #         print(x2,"u",end=" ; ")
    # print()
    

print(nb_valid)