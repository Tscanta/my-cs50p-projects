#Little Professor!
import random

def main():

    level = get_level()
    score = 0

    for i in range (10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0
        correct = False

        while tries < 3:
            try:
                user_ans = int(input(f"{x} + {y} = "))

                if user_ans == x+y: #if the users answer is correct it adds 1 to the score
                    score += 1
                    correct = True
                    break
                else: #if the users answer is not correct then it prints 'EEE' and adds 1 to the tries counter
                    print("EEE")
                    tries += 1

            except ValueError: #Value error counts as a wrong answer
                print("EEE")
                tries += 1

        if tries == 3 and not correct: #after the three tries
            print(f"{x} + {y} = {x+y}") #prints the real answer

    #Score after the loop ends
    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level in [1,2,3]: #only levels 1, 2 and 3 are valid
                return level
        except ValueError: #asks again if there is a value error i.e., if the user tries to enter a string instead of an integer
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9) #a random number between 0-9 when the level is 1
    elif level == 2:
        return random.randint(10, 99) #a random number between 10-99 when the level is 2
    elif level == 3:
        return random.randint(100, 999) #a random number between 100-999 when the level is 3

if __name__ == "__main__":
    main()
