set1 = { "Give", "ab", 1, 54 }
set2 = { 1, 222, 343, "ab", 5, }

print(set1.union(set2))  # {'GIve', 1, 5, 100, 9822, True, 'ab', 54, 55.09}
print(set1.intersection(set2))  # {'ab', 1}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.difference(b))  # {1, 2}
print(a.intersection(b))  # {5, 6}
print(a.symmetric_difference(b))

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)              # {1, 2, 3, 4, 5, 6}
print("Intersection:", a & b)       # {3, 4}
print("Difference (a - b):", a - b) # {1, 2}
print("Symmetric Difference:", a ^ b)  # {1, 2, 5, 6}

print("Is a subset of b:", a <= b)  # False 
print("Is a superset of b:", a >= b)  # False

print("Is a subset of b:", a.issubset(b))  # False
print("Is a superset of b:", a.issuperset(b))  # False  
print("Is disjoint:", a.isdisjoint(b))  # False
