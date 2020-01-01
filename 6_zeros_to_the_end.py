import array, numpy as np
def move_zeros(y):
    z = y.count(0)
    y = list(filter(lambda a: type(a) is not bool or a != 0, y))
    for _ in range(z):
        y.append(0)
    return y
y = array.array('i', [0, 0, False, 5, 1, 7, 55, 0, 88, 90, 5, 0])
print(move_zeros(y))

# doesn't work for booleans, wtf

#    return sorted(array, key=lambda x: x==0 and type(x) is not bool) # one-liner