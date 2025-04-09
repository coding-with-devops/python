#Snake Watr Gun Game
import random
#computer= -1
game_dict = { -1 : "snake", 
               0 : "water", 
               1 : "gun" }

def game(player, computer):
    if player == computer :
        print (f"⚖️  It's a tie! \n Your: {player} \n Computer: {computer}")
    elif (player == "snake" and computer == "water") or (player == "water" and computer == "gun") or (player == "gun" and computer == "snake"):
        print(f"✅ Your Win : \n Your: {player} \n Computer: {computer}")
    else:
        print(f"💻 Computer wins \n Your: {player} \n Computer: {computer}")

computer = random.choice(["snake","water","gun"])
your_input = int(input(f"Enter Your Input as {game_dict} \n [-1/0/1]: "))

if your_input in game_dict.keys():
    game(game_dict.get(your_input),computer)
else:
    print("Invalid Option")

