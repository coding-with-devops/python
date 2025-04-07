n = int(input("Enter the number of rows: "))
    
for i in range(n):
   print(" " * (n - i - 1) + "*" * (2 * i + 1))
print("-" * n)
for i in range(n):
    print("*" * (i  ))
for i in range(1, n + 1):
    print("*" * ( n -i))

print("-" * n)

for i in range(1,n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
print("-" * n)
    