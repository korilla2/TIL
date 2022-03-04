import time
import sys
from joblib import delayed, Parallel
import multiprocessing
sys.setrecursionlimit(10 ** 6)

start = time.time()


def fibo(n):
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)


print([fibo(i) for i in range(1, 40)])
print(time.time() - start)
