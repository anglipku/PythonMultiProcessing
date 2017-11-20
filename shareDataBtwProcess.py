# Two processes: main, and child (calc_square)
# To share value between two processes, use Shared Memory
# (shared memory lives outside the processes' hands.  It works like a placeholder)

import multiprocessing

def calc_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[ idx ] = n

if __name__ == '__main__':
    numbers  = [2, 3, 5]

    # Shared Memory 1: Create a multiprocessing array object. 'i' means data type is int, 3 is the size
    result = multiprocessing.Array('i', 3)
    # Shared Memory 2: Create a multiprocessing value object. 'd' means double
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target = calc_square, args = (numbers, result, v))

    p.start()
    p.join()

    print( result[ : ] )
    print(v.value)

### Output ###
'''
[2, 3, 5]
5.67
'''

# Note: we can also use multiprocessing.Queue() to achieve the same result