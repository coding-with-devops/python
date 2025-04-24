def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
    
ask_ok('Do you really want to quit?')

name = "Ashutosh"
age = 20
print("Hello " + name + "!" + " You are " + str(age) + " years old.")
print("Hello {}! You are {} years old.".format(name, age))
print(f"Hello {name}! You are {age} years old.")
