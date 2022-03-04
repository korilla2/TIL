import sys
from joblib import delayed, Parallel
import multiprocessing
import time
sys.setrecursionlimit(10 ** 6)

start = time.time()


def fibo(n):
    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)


print(Parallel(n_jobs=multiprocessing.cpu_count())(delayed(fibo)(i)
                                                   for i in range(1, 40)))
print(time.time() - start)
