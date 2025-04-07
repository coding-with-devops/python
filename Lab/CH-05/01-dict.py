a = { "key": "value",
	  "harry": "code", 
	  "marks": "100", 
	  "list": [1, 2, 9] }
print(a)
print(a["key"])
print(a.get("key"))
#a.clear()
print(a.get("key", "default_value"))
print(a)

list = [ [1, 2, 3], [4, 5], [6, 7] ]
print(list[0])