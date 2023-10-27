# dictionary is a collection of key value pairs.
# it is mutable. Dictionary items are ordered, changeable, and does not allow duplicates.
# it can be created as {k1:v1, k2:v2....}
_dict = {'a': 120, 'b': 130, 'c': 90}
_capital_dict = {'India': 'New Delhi', 'Japan': 'Tokyo', 'Nepal': 'Kathmandu'}
print(_dict)
print(len(_dict))
print(_capital_dict)
print(len(_capital_dict))

# to add a key value pair or to update value of a key to dictionary
_dict['d'] = 130
print(_dict)
_dict['d'] = 131
_capital_dict['USA'] = 'Washington D.C'
print(_dict)
print(len(_dict))
print(_capital_dict)
print(len(_capital_dict))

# retrieve an item from dictionary using key
_value = _dict['b']
print(_value)
_capital = _capital_dict['Nepal']
print(_capital)

# to remove a key and return its value
_popped_value = _capital_dict.pop('USA')
print(_popped_value)
print(_capital_dict)

# remove an item using key
del _dict['c']
print(_dict)

# to get a key value pair in a set like structure
_dict_set = _dict.items()
print(_dict_set)
print(all(_dict))
# to check if iterable is empty. in case of empty it returns false
print(any(_dict))
# if a key is not found while trying to retrieve its value, we get a key error
#_key_not_present = _dict['c']

for key in _dict:
    print(key)
    print(_dict[key])

for key, value in _dict.items():
    print(f'{key}:{value}')
