def filter(fn, l):
    for i in l:
        if fn(i):
            yield i



def map(fn, l):
    for i in l:
        yield fn(i)

def reduce(fn, l):
    acc = 0
    for i in l:
        acc = fn(acc, i)
    return acc

l = range(1000000000)
res1 = filter(lambda x : x % 3 == 0, l)
res2 = map(lambda x : x ** 2, res1)

res3 = [x ** 2 for x in l if x % 3 == 0]

#for i in res2:
#    print(i)
print(reduce(lambda a, c : a + c, res2))

