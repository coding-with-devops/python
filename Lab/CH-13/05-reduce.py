from functools import reduce
numbers = [10, 25, 3, 99, 56, 77]
def large_old():
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print("Largest number is:", largest)


large = lambda a, b: a if a > b else b
ln = reduce(large, numbers)
print(ln)