# function with Arguments

def func1(name, ending):
    print("Good Day,", name)
    print(ending)

def func2(name, ending="Thank You !"):
    print("Good Day,", name)
    print(ending)

func1("Ashutosh", "Bye")
func2("Rocky")

def greet(name): 
	gr = "hello "+ name 
	return gr 
		
a = greet ("harry") 
print(a)