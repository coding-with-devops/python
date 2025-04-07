#problem 3
#A spam comment is defined as a text containing following keywords:
#“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.


key1 = "Make a lot of money"
key2 = "buy now"
key3 = "subscribe this"
key4 = "click this"

comment = input("Enter the comment: ")
    

if key1 in comment or key2 in comment or key3 in comment or key4 in comment:
   print("Its a Spam comment " )
else:
   print("Not a spam comment: " )
        
