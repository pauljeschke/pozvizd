def filter_list(l):
    for x in l:
        if isinstance(x, int):
            newlist.append(x)
    return newlist
newlist = []

l = ['cat', 't', 2, 5, 'orange', 'bell', 99, 49876, 77 , 12345]
filter_list(l)
print(newlist)

#  return [i for i in l if not isinstance(i, str)]