print("Hello World!")

def isEven(i:int):
    return i % 2 == 0

print(isEven(8))
print(isEven(7))

isEven(i=2)

toto = isEven

print(toto(8))

def titi(fn):
    print(fn(8))

titi(isEven)

isEven = lambda x: x % 2 == 0 # f(x) = x % 2 == 0

l = [1,2,3,4,5,6]

def sum(l):
    total = 0
    for i in l:
        total += i
    return total

print(sum(l))
print(l[1:-1])

l = range(10000000000)

def fnFilter(l, predicatFn):
    res = []
    for i in l:
        if predicatFn(i):
            res.append(i)
    return res

def isPrime(i):
    if i < 2:
        return False
    else:
        for div in range(2,i):
            if i % div == 0:
                return False
        return True

#print(fnFilter(l, isEven))
#print(fnFilter(l, isPrime))

#print(fnFilter(fnFilter(l, isPrime), isEven))

#print(list(filter(isPrime,l)))
#for i in filter(isEven, filter(isPrime, l)):
#    print(i)

l = range(100)

def inc(x):
    return x + 1

import math

for i in map(lambda x:x*2, filter(isPrime, l)):
    print(i)

from functools import reduce
print(reduce(lambda acc, cur : acc + cur, map(lambda x:x*2, filter(isPrime, l))))
