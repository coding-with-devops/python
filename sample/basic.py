# This is literal on Python Code

print ("Hello This is Literal On python")
no_of_cpu = 4
no_of_pod = 2
mem_size = 8
mem_size += 2
print ( "Total No of CPU = " + str(no_of_cpu * no_of_pod ))
print ( "Total No Of Memory = " + str( mem_size * no_of_pod ))

# Assuming no_of_cpu, no_of_pod, and mem_size are defined
print(f"Total No of CPU = {no_of_cpu * no_of_pod}")
print(f"Total No Of Memory = {mem_size * no_of_pod}")
#format() method:
print("Total No of CPU = {}".format(no_of_cpu * no_of_pod))
print("Total No Of Memory = {}".format(mem_size * no_of_pod))


# This the Age Example
age = 22
AGE = 44
age /= 2
print(age + AGE)
# ++ sign
amount = 4
cost = 2
cost += 2
print(amount * cost)

y = 5
y = "Jack"
print(y)

name = "Sally" # employee name
data = "#123" 
print (name+data)