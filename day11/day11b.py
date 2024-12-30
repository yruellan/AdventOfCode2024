from time import time
from lib import memoize

f = open("data11.txt", "r")
data = list(map(int,f.read().split(" ")))
f.close()

    
@memoize
def update(x,n):

    if n == 0: return 1
    
    if x == 0: return update(1,n-1)
    elif len(str(x)) % 2 == 0:
        k = len(str(x)) // 2
        x1 = int(str(x)[:k])
        x2 = int(str(x)[k:])
        return update(x1,n-1) + update(x2,n-1)

    else:
        return update(2024*x,n-1)

def main():
    # print(data)
    N = 30
    t0 = time()
    print(sum([update(x,N) for x in data]))
    print(f"Run for {N = } in {time()-t0:.2f}s")
        
    

if __name__ == "__main__":
    main()