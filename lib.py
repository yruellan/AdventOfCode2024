"""
A collection of useful functions
that can be used for any problem
"""

from time import time
# from dict_hash import dict_hash

if __name__ == "__main__":
    from time import sleep
    from functools import cache
    from bisect import insort as bisect_insort

def timeit(func):
    is_rec = False
    def function_wrapper(*args,**kwargs):
        nonlocal is_rec
        if is_rec:
            return func(*args,**kwargs)
        t0 = time()
        is_rec = True
        r = func(*args,**kwargs)
        is_rec = False
        t1 = time()
        print("run ",func.__name__,f"in {t1-t0:.2f}s (",args,kwargs,")")
        return r
    function_wrapper.__name__ = func.__name__
    return function_wrapper


def memoize(func):
    cache = dict()
    def function_wrapper(*args):
        key = args
        if key in cache.keys():
            return cache[key]
        res = func(*args)
        cache[key] = res
        return res
    return function_wrapper

def insort(l,element,key=lambda x:x):
    
    i = 0
    j = len(l)
    val = key(element)
    m = j
    
    while i != j:
        
        m = (i+j)//2
        if i==m: break
        
        x = key(l[m])
        if x == val :
            i,j=m,m
            break
        elif x > val: j = m
        else : i = m
        
    l.insert(i,element)

if __name__ == "__main__":
    @memoize
    #@cache
    @timeit
    def fib(n):
        if n == 0: return 0
        if n == 1: return 1
        sleep(0.01)
        return fib(n-1)+fib(n-2)

    fib(10)
    fib(11)
    fib(12)
    fib(13)

    @timeit
    def test(n,f_insort):
        s = n*n
        l = [*range(s)]
        f_insort(l,s//2)
        print(l[ s//2 - 3 : s//2+3 ])

    #test(100,insort)
    #test(100,bisect_insort)
    #print()
    #test(1000,insort)
    #test(1000,bisect_insort)
    #print()
    #test(10000,insort)
    #test(10000,bisect_insort)
    #print()

    
