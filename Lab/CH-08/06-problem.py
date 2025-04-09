#Write a python function to remove a given word from a list and strip it at the same time.

def remo(l, word):
    for item in l:
        l.remove(word)
        return l

def remo1(l, word):
    n = []
    for item in l:
       if not (item == word):
            n.append(item.strip(word))
       return n
           
        

l = [ "Alice", "Rohan", "Subham", "Jordan" ]

#print(remo(l, "Jordan"))
print(remo1(l, "am"))