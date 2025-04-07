list1 = [ 23, 45,56, 67, 12, 34, 89 , 78, 90 ]

for i in list1:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
print("-----------Tuple List------------------ ")
tup1 = ( 23, 45,56, 67, 12, 34, 89 , 78, 90 )
for i in tup1:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

string1 = "Hello World"
for i in string1:   
    print(i, end=" ")
print("\n")

for i in range(2,50,2 ): # range(7) can also be used. print(i)
    print("Even No : ", i)
