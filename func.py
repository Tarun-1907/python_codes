from functools import lru_cache

@lru_cache
def incr(n):
    print("Running 1000 lines of code")
    return n+1
    
print(incr(10))
print(incr(20))
print(incr(30))
print(incr(10))