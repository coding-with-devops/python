def multi_table(number):
    for n in range(1,11):
        with open(f"tables/{number}.txt", "a") as f:
            f.write(f"{number}x{n}= {number * n} \n")
            

for i in range(2,21):
    multi_table(i)