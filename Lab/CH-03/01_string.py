name = "AshutoshMuduli"

sortname = name[0:4]
firstname = name[0:8]
lastaname = name[8:]
print( len(name) )
print(len(sortname) )
print("Sort Name: ", sortname)
print("First Name: ", firstname)
print("Last Name: ", lastaname)
print("Full Name: ", firstname + " " + lastaname)
print ("Last Name was: ", name[-6:])
print( "Skip Characters: ", name[0:14:2] )