# from www.youtube.com/@indently

# lru_cache
from functools import lru_cache
import time

# execution time track
start = time.time()


# fibonacci function
@lru_cache
def fib(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for i in range(0, 40):
    print(f'{i}: {fib(i)}')


# execution time track
end = time.time()
print(end - start)
