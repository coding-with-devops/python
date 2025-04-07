a = { "key": "value",
	  "harry": "code", 
	  "marks": 100,
	  "list": [1, 2, 9] }
print(a)
for i in a.items():
	print(i)
print(a.keys())
print(a.values())

a.update({"marks": 200, "Renuka": 150})
print(a)

print(a.pop("marks"))
print(a.popitem())
print(a)
print(a.popitem())
print(a)

