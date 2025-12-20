from random import randint
import sys


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            ai_guess = randint(1, level)
            guess = 0
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess <= 0:
                        continue
                    elif guess < ai_guess:
                        print("Too small!")
                    elif guess > ai_guess:
                        print("Too large!") 
                    else:      
                        print("Just right!")
                        sys.exit()
                except ValueError:
                    pass
    except ValueError:
        pass
