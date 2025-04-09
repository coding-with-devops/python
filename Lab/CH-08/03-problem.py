'''
Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''

def print_reverse_triangle(n):
    for i in range(n,0,-1):
        print(i * "*")

def print_triangle(n):
    for i in range(n):
        print(n * "*")
        n = n - 1

def patern(n):
    if n == 0:
        return
    print(n * "*")
    patern(n-1)

print_reverse_triangle(5)

print_triangle(3)

print("========================")
patern(6)