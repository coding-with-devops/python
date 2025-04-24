l = [ 1,2,3,4,5]

def evenfind(n):
    if n%2 == 0:
        return True
    return False
evennum = filter(evenfind,l)
print(list(evennum))