import sys

f_name = sys.argv[1]

if len(sys.argv) > 2:
    params = sys.argv[2:]
    print(params)
else:
    params = []
    print(params)
print(f_name)

if len(params) > 0:
    globals()[f_name](*params)
    
else:
    abc = globals()[f_name]