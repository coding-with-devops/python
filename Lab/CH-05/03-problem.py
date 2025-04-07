#Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add('18')
print(s)

#What will be the length of following set s:
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20')
print(s) # {20, '20', 20.0}
print(len(s)) # 2, because 20 and 20.0 are considered the same value in Python

#s = {}
#What is the type of 's'?
s = {} 
print(type(s)) # <class 'dict'>, because {} is an empty dictionary in Python