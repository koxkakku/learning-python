# List items are ordered, changeable, and allow duplicate values.
# it allows heterogeneous items to be added to it.
# it is mutable and iterable. it is defined using []
_list = [21, 4, 68]
_str_list = ['karnataka', 'Mizoram', 'Arunachal Pradesh', 'Gujarat']
# len function gives size of the list
print(type(_list))
print(_list.__sizeof__())
print(len(_list))
print(_list)
print(len(_str_list))
print(_str_list)
# append is used to add an item to the end of the list
_list.append(23)
# list allows duplicate values
_list.append(23)
_list.append(23)
_list.append(23)

print(len(_list))
print(_list)

# value stored at a given index can be changed/ updated in a list
_list[3] = 31
print(_list)

# loop through the list using for
for item in _list:
    print(item)

for i in range(len(_list)):
    print(_list[i])

# retrieval of an item using index
print(_list[3])
# we can pass a range of index to get a list of items from start index till end index-1
sublist = _list[2:5]
print(sublist)
# if we don't pass the end index, we get a list from start index till last index of the list
sublist = _list[2:]
print(sublist)

# del statement can be used to remove/ delete item at any given index from the list
del _list[2]
print(_list)

# remove method removes first occurrence of the item in the list
_list.remove(23)
print(_list)

# count method gives total number of occurrences of an item in list
print(_list.count(23))

# index method gives the index of first index of an item in the list
print(_list.index(23))

# in and not in are used to find existence or non-existence of an item in the list
print(22 in _list)
print(22 not in _list)

# pop method is used to remove and return an item from given index of the list
_pop_value = _list.pop(2)
print(_pop_value)
print(_list)

# insert is used to insert an item at a desired index in the list
_list.insert(0, 61)
print(_list)

# cpy is used to create a shallow copy of the list
_copy_list = _list.copy()
print(_copy_list)

# reverse method is used to reverse the order of items present on the list
_copy_list.reverse()
print(_copy_list)

# negative index is used to traverse list from end of the list
# -1 is the last index
print(_list[-1])
print(_list[-4:-1])

# extend method is used to append any iterable object to the end of list
_list.extend(_copy_list)
print(_list)
print(_list[-4:-1])
print(_list[0:-1])
# sort method sorts in ascending order by default
_list.sort()
print(_list)
_str_list.sort()
print(_str_list)
# to sort in descending order reverse=True needs to be passes as argument
_list.sort(reverse=True)
print(_list)
_str_list.sort(reverse=True)
print(_str_list)

# we can write custom sorting logic and pass it as the key parameter


def my_fun(string):
    return len(string)


_str_list.sort(key=my_fun)
print(_str_list)

# clear method removes all items from the list
_list.clear()
print(len(_list))
print(_list)
