# A set is a collection which is unordered, unchangeable, and unindexed.
# it allows heterogeneous items to be added to it.
# it is mutable and iterable. it doesn't allow duplicates . it is defined using {}
_set = {21, 4, 68}
# len function gives size of the set
print(type(_set))
print(_set.__sizeof__())
print(_set.__len__())
print(_set.__class__)
print(len(_set))
print(_set)
# add is used to add an item to the set
_set.add(23)
# set doesn't allow duplicate values
_set.add(23)
_set.add(7)
_set.add(7)

print(len(_set))
print(_set)

# remove method removes an item in the set
_set.remove(23)
print(_set)

# in and not in are used to find existence or non-existence of an item in the set
print(22 in _set)
print(22 not in _set)

# pop method is used to remove and return an item from the set
_pop_value = _set.pop()
print(_pop_value)
print(_set)

# cpy is used to create a shallow copy of the set
_copy_set = _set.copy()
print(_copy_set)

# to add any iterable to a set
_set.update((2, 10, 5))
print(_set)

# to get difference between sts as a set
print(_set.difference(_copy_set))
print(_set)
# to remove intersection of items from two sets
_set.difference_update(_copy_set)
print(_set)

# to remove a specific item from set. if item to be removed is not found it does not throw exception
_set.discard(10)
print(_set)

for item in _set:
    print(item)
# clear method removes all the items from set
_set.clear()
print(len(_set))
print(_set)


