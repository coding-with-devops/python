try:
    a = int(input("Enter You Input:"))
    print(f"Value : {a}")

except ValueError as t:
    print(t)
except Exception as e:
    print(e)

print("Thanks")