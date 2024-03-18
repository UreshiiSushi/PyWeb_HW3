from pprint import pprint
from time import time
from multiprocessing import Process, cpu_count





def simple_factorize(*number):
    result = []
    for n in number:
        dividers = []
        divider = 1
        while divider <= n:
            if n % divider == 0:
                dividers.append(divider)
            divider += 1
        result.append(dividers)
    return result

def multiproc_factorize(number):
    dividers = []
    divider = 1
    while divider <= number:
        if number % divider == 0:
            dividers.append(divider)
        divider += 1
    return dividers


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    start = time()
    a, b, c, d  = simple_factorize(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    finish = time()
    print(f"Factorizing without multiprocessing took: {finish - start} sec")

    print(f"Number of CPU: {cpu_count()}")

    start = time()
    processes = []
    for i in (128, 255, 99999, 10651060):
        p = Process(target=multiproc_factorize, args=(i,))
        p.start()
        processes.append(p)
    finish = time()
    [p.join() for p in processes]
    # a, b, c, d = 
    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    
    print(f"Factorizing with multiprocessing took: {finish - start} sec")