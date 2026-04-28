import time


def ch_time(func):
    def wrapper(*args, **kwargs):
        '''измеряет скорость'''
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"функ {func.__name__} за {end - start} сек")
        return res

    return wrapper


@ch_time
def sumn(n):
    return sum(n)


res = sumn(range(1000))
print(res)
