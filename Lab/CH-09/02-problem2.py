# game functions
import random
def game():
    return random.randint(1, 100)

with open("score.txt" , "r") as file:
    high_score = file.read()
if high_score == "":
    high_score = 0
else:
    high_score = int(high_score)
your_score = game()
print(f"You Score :{your_score} \n High Score : {high_score}")
if your_score > high_score:
    with open("score.txt" , "w") as n:
        n.write(str(your_score))
    print (f"Your Score is : {your_score}")
else:
    print (f"Game score {your_score} is less than Your Score {high_score} ")

