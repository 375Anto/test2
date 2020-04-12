import time
from functools import reduce
from operator import mul


def mult(*args):
    res = 1
    res *= (a for a in args)
    return res


def decorator(func):
    import functools

    @functools.wraps(func)
    def wrapper(value):
        from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
        # if value < 3000:
        executor_class = ThreadPoolExecutor
        max_workers = 4
        # else:
        #     executor_class = ProcessPoolExecutor
        executor = executor_class(max_workers=max_workers)
        a = int(value / max_workers)
        params = [[a * x + 1 for x in range(0, max_workers)],
                  [a * (x + 1) for x in range(max_workers)]
                  ]
        return reduce(mul, executor.map(func, *params))
    return wrapper


@decorator
def fact(started=0, finished=0):
    res = 1
    if started == 0:
        started = 1
    while started != finished+1:
        res *= started
        started += 1
    return res


def fact1(started=1, finished=0):
    res = 1
    if started == 0:
        started = 1
    while started != finished+1:
        res *= started
        started += 1
    return res


def fact_by_process(value):
    from concurrent.futures import ProcessPoolExecutor
    executor_class = ProcessPoolExecutor
    max_workers = 4
    executor = executor_class(max_workers=max_workers)
    a = int(value / 4)
    params = [
        [a * x + 1 for x in range(0, max_workers)],
        [a * (x + 1) for x in range(max_workers)]
        ]
    return reduce(mul, executor.map(fact1, *params))


if __name__ == '__main__':
    val = 500000
    print('multithread----')
    start_time = time.time()
    result = fact(val)
    print(' it was during {:2f} sec.'.format(time.time() - start_time))
    print('multiprocessing----')
    start_time = time.time()
    result2 = fact_by_process(val)
    print(' it was during {:2f} sec.'.format(time.time() - start_time))
    print('result of multiThreads and multiprocessors is the same: ', result == result2)
    # print(result)
    print('just one thread-----')
    start_time = time.time()
    result1 = fact1(finished=val)
    print(' it was during {:2f} sec.'.format(time.time() - start_time))
    # print(result1)
    print(result == result1)