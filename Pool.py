# Parallel processing. 'Map-Reduce'
# Here we use the recursive (clumsy) way of calculating fibonacci series to demo the difference
# in efficiency between Pool and Series processing

from multiprocessing import Pool
import time
from numpy import zeros

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    m = 42

    t1 = time.time()
    # Create a Pool object
    p = Pool(processes = 4)
    fibSeries = p.map(fibonacci, range(m))
    p.close()
    p.join()

    print("Pool takes:", time.time() - t1)

    t2 = time.time()
    fibSeries = zeros((m))
    for i in range(m):
        fibSeries[i] = fibonacci(i)

    print("Serial takes:", time.time() - t2)

### Output ###
'''
('Pool takes:', 179.84690594673157)
('Serial takes:', 245.81541204452515)
'''