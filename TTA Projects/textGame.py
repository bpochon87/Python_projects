# Python: 3.9.10
#
# Author: Brady Pochon
#
# Purpose: Demonstrating how to pass variables from function to function
#          while producing a functional game


# Importing playsound for ability to play sounds.
from playsound import playsound

def start(nice=0, mean=0, name=""):
    # Get user's name
    name = describeGame(name)
    nice, mean, name = niceMean(nice, mean, name)


def describeGame(name):
    """
        Check if this is a new game or not.
        If it's new, get the user's name.
        If it's not new, thank the player for
        playing again and continue with game.

        Meaning, if we do not already have user's
        name, then they're new and we need to get it.
    """
    if name != "":
        print("\nThanks for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat's your name? \n").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you'll be greeted \nby several different people. \nYou can choose to be nice or mean.")
                    print("However, at the end of the game, your fate \nwill be sealed by your actions.")
                    stop = False
    return name


def niceMean(nice, mean, name):
    stop = True
    while stop:
        showScore(nice, mean, name)
        pick = input("\nA stranger approaches you for conversation.\nWill you be nice or mean?\n(N/M)\n").lower()
        if pick == "n":
            print("\nThe stranger walks away, smiling...")
            playsound('cheer.wav')
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger is ready to fight...")
            playsound('boo.wav')
            mean = (mean + 1)
            stop = False
    score(nice, mean, name) # Pass these 3 variables to the score()


def showScore(nice, mean, name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name, nice, mean))


def score(nice, mean, name):
    # Score function is being passed the values stored within the 3 variables
    if nice > 2: # If condition is true, call win function, passing in variables so it can use them.
        win(nice, mean, name)
    if mean > 2: # If condition is true, call win function, passing in variables so it can use them.
        lose(nice, mean, name)
    else:
                 # Final condition, call niceMean function passing in variables so it can use them.
        niceMean(nice, mean, name)

def win(nice, mean, name):
    # Substitute the {} wildcards with our variable values.
    print("\nNice job, {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # Call again function and pass in our variables.
    again(nice, mean, name)


def lose(nice, mean, name):
    print("\nWow, you may be going to hell, {}!".format(name))
    # Call again function and pass in our variables
    again(nice, mean, name)


def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nWanna play again? (Y/N) \n").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("Peace out!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES' or ( N ) for 'NO'\n")


def reset(nice, mean, name):
    nice = 0
    mean = 0
    # Note: Do not reset the name variable as that same user has elected to play again
    start(nice, mean, name)



    


if __name__ == "__main__":
    start()
