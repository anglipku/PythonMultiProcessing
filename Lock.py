# Whenever two processes or threads are trying to access the same resource (memory, file, database),
# it can create a problem. So we need to protect the access with a lock.

import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # protected region
        lock.acquire()
        balance.value += 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        # protected region
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == '__main__':
    balance = multiprocessing.Value('i', 300)
    lock    = multiprocessing.Lock()
    p1      = multiprocessing.Process(target = deposit, args = (balance, lock))
    p2      = multiprocessing.Process(target = withdraw, args = (balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print (balance.value)

### Output ###
'''
300
'''

# Note: Without lock, we will get inconsistent results each time we run the program
# e.g. 305, 301 etc