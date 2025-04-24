l = [ 1,2,3,4,5]

squad = lambda l: l*l

print(list(map(squad,l)))


def func(i):
    return i + i  # Just double the single element

output = map(func, l)  # No need to convert to str
print(list(output))
