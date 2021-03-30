import random
random_num = random.randint(1,100)
print(random_num)


guess = input("Guess a number between 1 and 100!: ")
while guess != random_num:
    guess = int(guess)
    if guess == random_num:
        print("Winner!")
        random_num = random.randint(1,100)
        again = input("Would you like to play again? (y or n) ")
        if again == "y":
            random_num = random.randint(1,100)
            print(random_num)
            guess = input("Guess a number between 1 and 100!: ")
        else:
            print("Thanks for playing!")
            exit()
    else:
        guess = input("Incorrect. Try again: ")