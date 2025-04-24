import random
def game():
    random_no = random.randint(1,100)
    guess_no = 0
    attempt = 0
    while ( guess_no != random_no):
        guess_no = int(input("Enter Your No :"))
        if guess_no > random_no:
            print("\nLower Number Please !! ")
        else:
            print("\nHigher Number Please !! ")
        attempt = attempt + 1
    print(f"\nYour Guess no {guess_no} Is correct after \"{attempt}\" attempt")

            
game()