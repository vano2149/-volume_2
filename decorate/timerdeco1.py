"""
timerdeco1.py file!
"""

import time, sys

force = list if sys.version_info[0] == 3 else (lambda X: X)

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    
    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        elapsed = time.time() - start
        self.alltime += elapsed
        print(f"{self.func.__name__}: {elapsed}, {self.alltime}")
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return force(map((lambda x: x * 2), range(N)))
result = listcomp(5)

listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print(f'AllTime = {listcomp.alltime}')
print(' ')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print(f'AllTime = {mapcall.alltime}')

print('\n**map/comp = %s' % mapcall.alltime)