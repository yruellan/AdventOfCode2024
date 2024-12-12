from time import time

f = open("data11.txt", "r")
data = list(map(int,f.read().split(" ")))
f.close()

def sub_update(x):
    n = len(str(x)) // 2
    return [int(str(x)[:n]),int(str(x)[n:])]

def update(l):
    i = 0
    for _ in range(len(l)):
        x = l[i]
        if x == 0:
            l[i] = 1
        elif len(str(x)) % 2 == 0:
            n = len(str(x)) // 2
            l[i:i+1] = sub_update(x)
            i += 1
        else:
            l[i] *= 2024
        i += 1

def main():
    # print(data)
    t0 = time()
    for i in range(25):
        update(data)
        print(f"Step {i+1}: {len(data)} | {time()-t0:.2f}s")
        # if len(data) < 10:
        #     print(data)
    

if __name__ == "__main__":
    main()