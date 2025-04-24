# game functions
import random
def game():
    print("You are Playing A Game")
    score = random.randint(1, 100)
    with open("score.txt", "r") as file:
        high_score = file.read()
    if high_score != "":
        high_score = int(high_score)
    else:
        high_score = 0
    
    print (f"Your Score is : {score}")
    if score  > high_score:
        with open("score.txt", "w") as file:
            file.write(str(score))
    return score
game()    
