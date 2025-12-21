import random

def main():
    score = 0
    level = get_level()

    # Generate levels 10 times
    for i in range(10):
        first = generate_integer(level)
        second = generate_integer(level)

        sum = first + second
        attempt = 0

        while True:
            try:
                answer = int(input(f"{first} + {second} = "))

                # validates the answer
                if answer == sum:
                    score += 1
                    break

                else:
                    print("EEE")
                    attempt += 1

                    if attempt == 3:
                        print(f"{first} + {second} = {sum}")
                        break

            # handles value error
            except ValueError:
                print("EEE")
                attempt += 1
                if attempt == 3:
                    print(f"{first} + {second} = {sum_val}")
                    break
                pass

    #finally, print the score
    print(f"Score: {score}")

# manages usr input on the level
def get_level():
    while True:
        try:
            n = 0
            while n not in [1, 2, 3]:
                n = int(input("Level: "))
            return n
        except ValueError:
            pass

#generates random integer based on a certain level between 1-3
def generate_integer(level):
    x = 0
    try:
        if level == 1:
            x = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
    except ValueError:
        pass

    return x

if __name__ == "__main__":
    main()
