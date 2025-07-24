import random

class GuessNumber:
    def __init__(self, lower=1, upper=100):
        self.lower = lower
        self.upper = upper
        self.the_number_to_guess = random.randint(lower, upper)

    def userguess(self):
        while True:
            try:
                guess = int(input(f"Enter your guess ({self.lower}-{self.upper}): "))
                if self.lower <= guess <= self.upper:
                    return guess
                else:
                    print("Enter in range please!!")
            except:
                print("Please enter numbers only!!")

    def play(self):
        print("Welcome to my Number Guessing Game!!!!")
        while True:
            userguess = self.userguess()
            if userguess < self.the_number_to_guess:
                print("Too low!")
            elif userguess > self.the_number_to_guess:
                print("Too high!")
            else:
                print("Correct!")
                break

if __name__ == "__main__":
    game = GuessNumber()
    game.play()
