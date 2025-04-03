# problem 1
name = input("Enter your name: ")
print(f"Good Afternoon, {name}")
# problem 2
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> 
Thanks & Regards,  '''
print(letter.replace("<|Name|>", name).replace("<|Date|>", "1st Jan 2023"))
# problem 3
des1 = "Ashutosh is a Good Boy and he is 36 years old."
print(des1.find(" "))
#problem 4
letter1 = "Dear Harry, \n this python course is nice. \n Thanks!"
print(letter1)