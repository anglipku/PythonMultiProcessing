# In this example, multiThreading is faster than sequential operations,
# since in multiThreading, while calc_square sleeps, calc_cube works
# and in sequential operation, nothing else is done while calc_square or calc_cube sleeps

# So multiThreading is like adding more workers/more shifts to a streamline.

# Note: In multithreading, we can save the result in global containers, while this is not true for multiprocessing


import threading
import time

sqrResult = []
cbResult = []

def calc_square(numbers):
    '''declare result as a global var,
    ow result will be created as a local var'''
    global sqrResult
    for n in numbers:
        time.sleep(0.1)
        sqrResult.append(n ** 2)

def calc_cube(numbers):
    '''declare result as a global var,
    ow result will be created as a local var'''
    global cbResult
    for n in numbers:
        time.sleep(0.1)
        cbResult.append(n ** 3)


if __name__ == '__main__':
    arr = [1, 2, 3, 4]

    # Run on two threads
    startTime1 = time.time()
    t1 = threading.Thread(target = calc_square, args = (arr, ))
    t2 = threading.Thread(target = calc_cube, args=(arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    endTime1 = time.time()

    print 'Square results = ', sqrResult
    print 'Cube results = ', cbResult

    # Run on one thread
    startTime2 = time.time()
    calc_square(arr)
    calc_cube(arr)
    endTime2 = time.time()

    print 'multiThread time = ', endTime1 - startTime1
    print 'single Thread time = ', endTime2 - startTime2


### Output ###
'''
Square results =  [1, 4, 9, 16]
Cube results =  [1, 8, 27, 64]
multiThread time =  0.411176919937
single Thread time =  0.81730389595
'''