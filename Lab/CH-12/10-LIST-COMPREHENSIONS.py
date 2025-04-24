list1 = [1,7,10,22]

squaredlist = []
for item in list1:
    squaredlist.append(item*item)
print(squaredlist)

squaredlist2 = [ item*item for item in list1]
print(squaredlist2)

