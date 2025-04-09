#Write a recursive function to calculate the sum of first n natural numbers.

def rec_cal(n):
    if n == 1:
        return 1
    else:
        return n + rec_cal(n-1)

n = int(input("Enter The Value of N:"))
print (f" Recursive Calculation of {n} is : {rec_cal(n)}")