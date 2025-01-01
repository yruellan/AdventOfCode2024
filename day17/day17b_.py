from time import time
from lib import memoize
from math import log2



instructions = [2,4,1,1,7,5,4,6,1,4,0,3,5,5,3,0]
# instructions = [0,3,5,4,3,0]
# instructions = [0,2,1,9]

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

@memoize
def calc2(A, k=0):
    
    B = A % 8
    B = B ^ 1
    C = (A // (2**B)) % 8
    print(f"{A=} {2**B=} | C\'={A // (2**B)},{C=},->,{B=},{B^C=}")
    B = B ^ C
    B = B ^ 4
    A = A // 8
    # out.append(B % 8)
    if A == 0 : return [B % 8]
    # elif B % 8 != instructions[k]:
    #     return []
    else:
        return [B % 8] + calc2(A, k+1)
    

i = 60
t0 = time()
while True:

    A = i
    # out = calc(A,0,0)
    out = calc2(A)

    if out == instructions:
        print(f"Found : {i=}  { out = }")
        break

    if i % 1_000_000 == 0:
        print(f"i = { format(i, '_d') } {time()-t0:.2f}  { log2(i+1) = :.1f}")

    # if abs(i-117440) < 4:
    #     print(f"{i=} {out=}")

    if i <= 70:
        print(f"{i=} {out=}")
    else:
        break

    i += 1