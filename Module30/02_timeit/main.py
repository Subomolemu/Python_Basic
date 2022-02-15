import timeit
import time


res_1: float = timeit.timeit('"-".join(str(n) for n in range(100))',
                             number=10000)
print(res_1)

start_2 = time.time()
res_2 = ['-'.join(str(n) for n in range(100)) for i in range(10000)]
print(time.time() - start_2)

start_3 = time.time()
res_3 = list(map(lambda x: '-'.join(str(x) for x in range(100)),
                 [i for i in range(10000)]))
print(time.time() - start_3)

