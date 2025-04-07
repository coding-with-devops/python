my_dict = {'a': 1, 'b': 2, 'c': 3}

print(my_dict.get('a'))           # 1
print(my_dict.get('z', 'N/A'))    # 'N/A'

my_dict['d'] = 4
my_dict.update({'e': 5})

print(my_dict.keys())             # dict_keys(['a', 'b', 'c', 'd', 'e'])
print(my_dict.values())           # dict_values([1, 2, 3, 4, 5])
print(my_dict.items())            # dict_items([('a', 1), ('b', 2), ...])

print(my_dict)

a = my_dict.copy()
a.update({'a': 10, 'f': 6})
print(a)                          # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}