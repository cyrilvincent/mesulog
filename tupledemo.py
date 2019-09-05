def stat(l):
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        elif i > max:
            max = i
        sum += i
    return min, max, sum/len(l)

t = stat(range(10))
print(t[2])