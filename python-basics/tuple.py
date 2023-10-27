# Tuple items are ordered, unchangeable, and allow duplicate values.
# its immutable version of list. it can store heterogeneous data.
# add, remove, append, pop, insert these operations are not allowed on tuple
_tuple = (23, 13, 78, 33, 16, 33)
print(_tuple)
print(_tuple[2])

print(_tuple.index(23, 0, 2))
print(_tuple.count(33))

for item in _tuple:
    print(item)

for i in range(len(_tuple)):
    print(_tuple[i])
