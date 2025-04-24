from functools import reduce

l = [ 1,2,3,4,5]

def sum(a,b):
    return a+b
result = reduce(sum,l)

print(result)

result2 = lambda x, y : x*y
print(reduce(result2, l))