#Write a program to filter a list of numbers which are divisible by 5.

l = [ 132,55,23,56,545,100,1004,1007,765]

def divby(number):
    if number%5 == 0:
        return True
    return False
division = filter(divby,l)
print(list(division))
