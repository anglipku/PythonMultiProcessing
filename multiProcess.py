import multiprocessing
import time

def calc_square(numbers):
    for n in numbers:
        time.sleep(0.1)
        print(n ** 2)

def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.1)
        print(n ** 3)


if __name__ == '__main__':
    arr = [1, 2, 3, 4]

    # Run on two processes
    startTime1 = time.time()
    p1 = multiprocessing.Process(target = calc_square, args = (arr, ))
    p2 = multiprocessing.Process(target = calc_cube, args = (arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    endTime1 = time.time()

    print 'multiProcess time = ', endTime1 - startTime1
    print 'singleProcess time is approximately 0.8 sec, see output of multiThread.py'


### Output ###
'''
1
1
4
8
9
27
16
64
multiProcess time =  0.421972990036
singleProcess time is approximately 0.8 sec, see output of multiThread.py
'''