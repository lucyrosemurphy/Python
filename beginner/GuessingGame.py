import random

#The user is prompted to guess a number between one and 9, if the number matches the radom number stored by the function
# the user wins.
def guessinGame():
    corectNum = random.randint(1,10)
    win = False
    while win == False:
        Guess = input("Enter a number between 1 and 9")
        if corectNum == int(Guess):
            print("Wow what a guess! You must be pychic!")
            win = True
            break #Once the game is won, you break from the for loop
        else:
            print("Not right this time, but I will let you try again.")
