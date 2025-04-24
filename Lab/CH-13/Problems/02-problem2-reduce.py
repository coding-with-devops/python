from functools import reduce

l = [ 132,55,23,56,5455,100,1004,1007,7654]

def greater_no(a,b):
    if a>b:
        return a
    else:
        return b

greatest = reduce(greater_no, l)

print(greatest)