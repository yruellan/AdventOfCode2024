

def calc(A,B=0,C=0):
    out = []

    while True:
        B = A % 8
        B = B ^ 1
        C = A // (2**B)
        B = B ^ C
        B = B ^ 4
        A = A // (2**3)
        out.append(B % 8)
        # if out[-1] != instructions[len(out)-1]:
        #     break
        if A == 0 :
            return out
        
def to_octal(n):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % 8))
        n //= 8
    return digits[::-1]
    
instructions = [2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0]

def to_int(l):
    n = 15
    x = 0
    for k in l:
        if n < 0: raise ValueError("Invalid length")
        x += k * 8 ** n
        n -= 1
    return x

def delta(r):
    for i in range(len(r)):
        if i >= 16 : return i
        if r[::-1][i] != instructions[::-1][i]:
            return i
    return len(r)

def c(l):
    return calc(to_int(l))

def find(l):

    if len(l) == 16:
        x = to_int(l)
        r = calc(x)
        print(f"Found : {r=} {r == instructions} {l=} ")
        return

    r = calc(to_int(l))
    # if r == instructions:
    #     print(f"Found : {l=} {to_int(l)=} {r=}")
    d = delta(r)
    # print(f"{d=:5} {l=} {to_int(l)=}")
    for i in range(8):
        l1 = l[:] + [i]
        x = to_int(l1)
        r = calc(x)
        dr = delta(r)
        # print(f"{dr=:5} {l1=}")
        if dr >= len(l1):
            find(l1)


# for i in range(8):
#     l = [5,6,0,0,6,4,4,6,7,4,0,2,4]
#     l.append(i)
#     x = to_int(l)
#     print(f"{i=} {calc(x)}")
print(f"Found : r={instructions}")
find([5])