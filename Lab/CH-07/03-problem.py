#Write a program to find whether a given number is prime or not.

number = int(input("Enter a number: "))

for i in range(2, number):
    print( "Value:", number % i )
    if (number % i) == 0:
       # is_prime = False
        print(f"{number} is not a prime number.")
        break
    else:       
        #is_prime = True
        #print(is_prime)
        print(f"{number} is a prime number.")
        break
