#Write a python program using function to convert Celsius to Fahrenheit.

def Celsius_to_Farhenheit(C):
    F = (C * (9/5)) + 32
    return F
C = float(input("Please Enter Celsius :"))

print(f"Fahrenheit Value of Celsius {C} is :  {round(Celsius_to_Farhenheit(C),2)}")