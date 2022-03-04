from base64 import encode
import sys
import multiprocessing
import time
import ray
import datetime

start = time.time()
sys.setrecursionlimit(10 ** 6)


num_cpus = multiprocessing.cpu_count()
ray.init(num_cpus=num_cpus)


@ray.remote
def fibo(n):

    if n < 3:
        return 1
    return fibo(n-1) + fibo(n-2)


@ray.remote
def print_current_datetime():
    time.sleep(0.3)
    current_datetime = datetime.datetime.now()
    print(current_datetime)
    return current_datetime


print(ray.get([fibo.remote(int(3)) for i in range(4)]))

print(time.time() - start)
